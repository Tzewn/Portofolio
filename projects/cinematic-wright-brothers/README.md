# Cinematic: Wright Brothers — "Twelve Seconds"

Dokumenter pendek 79 detik (1280×720) tentang penerbangan pertama Wright bersaudara, dibuat **seluruhnya dari kode**: satu gerakan kamera di atas papan berisi foto, peta, dan kartu dokumen, dengan setiap elemen muncul tepat pada kata narator yang bersangkutan.

## Isi folder

- `scene.py` — definisi film: peta AS, foto penerbangan pertama, counter "12 detik / 120 kaki", stempel FAILED untuk Langley, rute Dayton → Kill Devil Hills
- `script.json` — naskah narasi per baris
- `photos.json`, `map.json` — daftar foto dan data peta
- `audio/segments.json`, `audio/timing.json` — timing narasi per kata/baris (film me-retiming dirinya sendiri mengikuti voiceover)
- `tts_wrapper.py` — wrapper kecil untuk memberi makan TTS ke pipeline
- `fonts/LICENSES.txt` — lisensi font yang dipakai

## Kredit & lisensi

- Dibuat dengan skill **cinematic-film** dari [Moh4696/cinematic-skill](https://github.com/Moh4696/cinematic-skill) (Python + Skia)
- 7 foto public domain dari Wikimedia Commons
- Font Bebas Neue (OFL) dan Homemade Apple (Apache 2.0), diunduh dengan `get_fonts.py` dari skill tersebut
- Narasi: TTS Bahasa Inggris

Hasil render ini adalah versi "draft" sesuai alur contoh repo: audio narasi saja, belum termasuk sound effect dan caption terbakar. File video tidak disertakan di repo ini (ukuran besar).
