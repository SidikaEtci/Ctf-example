import os
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

# Ana portal: Spotifly Müzik Sızıntı Arayüzü
@app.route("/")
def index():
    track_meta = {
        "title": "Kusursuz Plan (Yayınlanmamış Sızıntı)",
        "artist": "JANTİ",
        "album": "Single 2026",
        "audio_file": "audio/janti_leak_demo.wav"
    }
    return render_template("index.html", track=track_meta)

# Spektrogram üzerinden keşfedilen ikincil portal: Kulis Dedikodu Akışı
@app.route("/backstage-feed")
def backstage_feed():
    blog_posts = [
        {
            "id": 1,
            "title": "JANTİ'nin Sızdırılan Parçası: Master Kayıt İhlali mi?",
            "author": "DeepVibe_Insider",
            "date": "2026-09-01",
            "snippet": "Sızıntı şirket içi bir miksaj seansından kaynaklandı. Ses mühendisinin arkasında bıraktığı yorum imzalarını ve metaveri izlerini kontrol edin."
        }
    ]
    return render_template("blog.html", posts=blog_posts)

# Adli bilişim (forensic) ses analizi için indirme rotası
@app.route("/download/audio")
def download_audio():
    audio_dir = os.path.join(app.root_path, "static", "audio")
    filename = "janti_leak_demo.wav"
    if not os.path.exists(os.path.join(audio_dir, filename)):
        abort(404)
    return send_from_directory(audio_dir, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)