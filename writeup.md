# 📝 JANTİ Leak — Official CTF Writeup

---

## 🇬🇧 English Writeup

### Challenge Overview
* **Category:** Steganography / Forensics / Web Discovery
* **Target:** http://localhost:5000
* **Total Flags:** 2

---

### Stage 1: Spotifly Audio Breach (Spectrogram Steganography)

1. **Reconnaissance:**
   Navigate to the landing page at `http://localhost:5000`. The application presents a music player interface dubbed "Spotifly" featuring the unreleased pre-master track *"Flawless Scheme"* by **JANTİ**.

2. **Asset Extraction:**
   Click the **Download Master Audio (WAV)** button to download `janti_leak_demo.wav`.

3. **Audio Spectrum Analysis:**
   Open the file using an audio analysis suite such as **Audacity**, **Sonic Visualiser**, or run a terminal tool like `sox`:
   * In Audacity, open `janti_leak_demo.wav`.
   * Click the track drop-down menu (next to the track name on the left).
   * Select **Spectrogram** view.
   * In Spectrogram Settings, ensure the display covers upper ultrasonic frequencies up to 20,000 Hz (Linear display mode recommended).

4. **Decoding the Payload:**
   Within the first 6 seconds, in the high frequency band between 13.5 kHz and 19.8 kHz, two stacked text lines appear clearly rendered in the spectrum:

       TUGA{4ud10_sp3ctr0gr4m_j4nt1_l34k}
       ROUTE: /backstage-feed

* **Flag 1:** TUGA{4ud10_sp3ctr0gr4m_j4nt1_l34k}
* **Discovered Route:** /backstage-feed

---

### Stage 2: Backstage Portal & Image Forensics

1. **Accessing the Hidden Endpoint:**
   Navigate to `http://localhost:5000/backstage-feed`.
   The page displays a dark purple blog post titled *"EXCLUSIVE: Surveillance Snapshot of the Suspect Who Leaked JANTİ's Track"*, featuring an embedded photo of the workstation.

2. **Acquiring the Evidence:**
   Right-click the surveillance image and save it as `photo.jpg` (or fetch directly via `curl -O http://localhost:5000/static/img/photo.jpg`).

3. **Forensic Metadata Inspection:**
   Run `exiftool` on the captured file:

       exiftool photo.jpg

   Alternatively, filter for strings:

       strings photo.jpg | grep -iE "TUGA|hilal"

4. **Artifact Extraction:**
   The EXIF metadata contains the investigator notes and the second flag:
   * **Artist:** Rogue Computer Engineer
   * **Copyright:** TUGA{h1l4l_pr0duc3r_bu5t3d_f0r_j4nt1_fr4ud}
   * **UserComment:** INTERNAL AUDIT: Suspect identified during unauthorized breach. Evidence tag: TUGA{h1l4l_pr0duc3r_bu5t3d_f0r_j4nt1_fr4ud}

* **Flag 2:** TUGA{h1l4l_pr0duc3r_bu5t3d_f0r_j4nt1_fr4ud}

---
---

## 🇹🇷 Türkçe Çözüm (Writeup)

### Soru Özeti
* **Kategori:** Steganography / Forensics / Web Keşfi
* **Erişim Adresi:** http://localhost:5000
* **Toplam Bayrak:** 2 Adet

---

### 1. Aşama: Spotifly Ses Analizi (Spektrogram Steganografisi)

1. **İlk İnceleme:**
   Tarayıcıdan `http://localhost:5000` adresine gidilir. JANTİ grubuna ait sızdırılmış *"Flawless Scheme"* parçasını çalan "Spotifly" arayüzü ile karşılaşılır.

2. **Dosyanın İndirilmesi:**
   Sayfadaki **Download Master Audio (WAV)** butonuna tıklanarak `janti_leak_demo.wav` dosyası bilgisayara indirilir.

3. **Spektrogram İncelemesi:**
   İndirilen dosya **Audacity** veya **Sonic Visualiser** programı ile açılır:
   * Audacity'de sol taraftaki parça adı menüsüne tıklanıp **Spectrogram (Spektrogram)** modu seçilir.
   * Spektrogram ayarlarından frekans üst sınırının 20.000 Hz'e kadar görüntülendiğinden emin olunur.

4. **Metnin Okunması:**
   İlk 6 saniye içerisinde, 13.5 kHz ile 19.8 kHz yüksek frekans bandında iki satır metin belirir:

       TUGA{4ud10_sp3ctr0gr4m_j4nt1_l34k}
       ROUTE: /backstage-feed

* **1. Bayrak:** TUGA{4ud10_sp3ctr0gr4m_j4nt1_l34k}
* **Keşfedilen Gizli Rota:** /backstage-feed

---

### 2. Aşama: Gizli Sayfa ve Görsel Adli Bilişimi (EXIF/Metadata)

1. **Gizli Sayfaya Erişim:**
   Tarayıcıdan spektrogramda bulunan adrese gidilir: `http://localhost:5000/backstage-feed`.
   Sayfada sızıntıyı yapan mühendisin güvenlik kamerası kaydının paylaşıldığı bir blog yazısı yer almaktadır.

2. **Görselin Alınması:**
   Yazıda yer alan fotoğraf (`photo.jpg`) sağ tıklanarak bilgisayara kaydedilir.

3. **Metadata (EXIF) Taraması:**
   Terminal üzerinden `exiftool` aracı çalıştırılır:

       exiftool photo.jpg

   (veya doğrudan metin araması yapılır: `strings photo.jpg | grep "TUGA{"`)

4. **Bayrağın Çıkarılması:**
   Metadata etiketleri incelendiğinde `Copyright` ve `UserComment` alanlarında 2. bayrak açıkça görülür:
   * **Artist:** Rogue Computer Engineer
   * **Copyright:** TUGA{h1l4l_pr0duc3r_bu5t3d_f0r_j4nt1_fr4ud}

* **2. Bayrak:** TUGA{h1l4l_pr0duc3r_bu5t3d_f0r_j4nt1_fr4ud}