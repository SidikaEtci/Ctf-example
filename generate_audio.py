import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.io import wavfile

def generate_spectrogram_audio(text: str, output_path: str = "app/static/audio/janti_leak_demo.wav") -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 1. Canvas setup
    width, height = 1600, 150
    img = Image.new("L", (width, height), color=0)
    draw = ImageDraw.Draw(img)

    font = None
    possible_fonts = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf"
    ]
    for font_path in possible_fonts:
        if os.path.exists(font_path):
            try:
                font = ImageFont.truetype(font_path, 38)
                break
            except Exception:
                continue

    if font:
        draw.text((30, 50), text, fill=255, font=font)
    else:
        fallback_font = ImageFont.load_default()
        for dx in range(3):
            for dy in range(3):
                draw.text((30 + dx, 55 + dy), text, fill=255, font=fallback_font)

    img_data = np.array(img)[::-1, :] / 255.0

    # 2. Audio synthesis parameters (Target: exactly 10.0 seconds)
    sample_rate = 44100
    target_duration = 10.0  # seconds
    duration_per_col = target_duration / width  # 0.00625 seconds per column
    samples_per_col = int(sample_rate * duration_per_col)

    min_freq = 14000.0
    max_freq = 19500.0
    freq_bins = np.linspace(min_freq, max_freq, height)

    audio_signal = []
    t = np.linspace(0, duration_per_col, samples_per_col, endpoint=False)

    print(f"[*] Synthesizing {target_duration}s spectrogram audio...")

    for col in range(width):
        col_pixels = img_data[:, col]
        active_indices = np.where(col_pixels > 0.3)[0]

        col_sound = np.zeros(samples_per_col)
        for idx in active_indices:
            freq = freq_bins[idx]
            amp = col_pixels[idx]
            col_sound += amp * np.sin(2 * np.pi * freq * t)

        audio_signal.extend(col_sound)

    audio_arr = np.array(audio_signal)
    max_val = np.max(np.abs(audio_arr))
    if max_val > 0:
        audio_arr = audio_arr / max_val
    audio_arr = (audio_arr * 32767).astype(np.int16)

    wavfile.write(output_path, sample_rate, audio_arr)
    print(f"[+] 10-second audio successfully generated at: {output_path}")

if __name__ == "__main__":
    payload_message = "TUGA{4ud10_sp3ctr0gr4m_j4nt1_l34k} | ROUTE: /backstage-feed"
    generate_spectrogram_audio(payload_message)