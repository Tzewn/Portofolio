# Portofolio Tzewn

Halo, saya **Tzewn** (Pelrr) dari Indonesia. Saya membuat video vertikal, video animasi narasi, dan aplikasi web kecil — dibantu AI sebagai tim produksi.

Repo ini berisi kode dan dokumen dari proyek-proyek yang sudah saya kerjakan. File media besar (video/audio/gambar) tidak disertakan di repo ini; yang ditampilkan adalah script, data, dan dokumentasinya. Contoh hasil videonya bisa dilihat di channel **Bagaga**.

> English summary: I'm Tzewn, an Indonesian creator building vertical short-form videos, narrated animation videos, and small web apps with AI-assisted production. This repo collects the code and docs behind those projects. Large media binaries are intentionally excluded.

## Proyek

| Proyek | Isi | Teknologi |
|---|---|---|
| [Auto-Clip Shorts](projects/auto-clip-shorts/) | Pipeline memotong video panjang jadi Shorts/Reels vertikal 1080×1920 gaya MotionStyle (facecam di atas, gameplay mengisi panel), lengkap dengan skill/workflow dan script render | FFmpeg, Python, Bash |
| [Cinematic: Wright Brothers](projects/cinematic-wright-brothers/) | Dokumenter pendek "Twelve Seconds" (79 detik, 1280×720) yang seluruhnya digambar dari kode: foto public domain, peta AS, counter dan stempel yang jatuh tepat di kata narator | Python (Skia), FFmpeg, TTS |
| [Quiet Worlds](projects/quiet-worlds/) | Video explainer animasi narasi 4 planet (Koala, Glowworm, Puffin, Angsa) + versi Shorts per planet, dengan subtitle terbakar dan overlay rating | Python, FFmpeg, TTS Bahasa Indonesia |
| [Simulasi Kehidupan](projects/simulasi-kehidupan/) | Game simulasi kehidupan 3D voxel: penduduk AI berciri khas yang berkembang biak, belajar, sakit, lapar, berinovasi, dan membangun kota ala city-builder | TypeScript, 3D voxel, server-backed |
| [mp3 Galer](projects/mp3-galer/) | Web app konverter YouTube ke MP3 (128–320 kbps) dengan pemutar dan riwayat unduhan | TypeScript, server-backed |

### Contoh hasil

- Shorts MotionStyle 1: https://youtube.com/shorts/mWWHQ3jTOh8
- Shorts MotionStyle 2: https://youtube.com/shorts/USLnIBNBRfw

## Jasa yang saya tawarkan

- Edit Shorts/Reels dari video panjang (streamer, podcast, gameplay) — paket per 10/20/30 klip, siap upload dengan judul dan caption. Daftar harga lengkap: [JASA.md](JASA.md)
- Video animasi narasi / explainer pendek
- Web mini / landing page untuk UMKM dan creator

Untuk diskusi proyek, silakan buka Issue di repo ini atau hubungi saya lewat profil GitHub.

## Catatan lisensi & kredit

- Kode dan dokumen buatan saya di repo ini berlisensi MIT (lihat `LICENSE`).
- Proyek cinematic memakai skill **cinematic-film** dari [Moh4696/cinematic-skill](https://github.com/Moh4696/cinematic-skill); foto-foto Wright Brothers berasal dari Wikimedia Commons (public domain); font Bebas Neue (OFL) dan Homemade Apple (Apache 2.0) — detail di `projects/cinematic-wright-brothers/fonts/LICENSES.txt`.
- Script auto-clip adalah alat bantu editing umum. Hak atas video sumber tetap milik pemiliknya masing-masing; repo ini tidak menyertakan file video sumber apa pun.
- Beberapa script memakai path contoh `~/workspace/...` dari mesin kerja asal — sesuaikan dengan struktur foldermu sebelum menjalankan.
