# Quiet Worlds — video explainer animasi narasi

Video explainer vertikal (1080×1920) tentang planet-planet fiksi, diceritakan dengan narasi Bahasa Indonesia, subtitle terbakar, judul planet, dan overlay rating "Danger / Supplies" per planet.

## Isi folder

- `naskah.txt` — naskah lengkap; `seg_*.txt` — naskah per segmen (intro, Koala, Glowworm, Puffin, Angsa, closing)
- `build.py` — merakit klip animasi + gambar (Ken Burns) menjadi segmen video per planet dengan FFmpeg
- `final.py` — menggabungkan segmen, narasi, subtitle (SRT → ASS), judul, dan overlay rating menjadi video final
- `timing.json` — offset dan durasi segmen
- `subs_full.srt`, `subs_full.ass` — subtitle final
- `title_*.txt`, `rating_*.txt` — judul dan rating per planet

## Hasil

- Video panjang 4 planet: 210 detik
- Dipotong lagi menjadi 4 Shorts per planet (Koala 73 dtk, Glowworm 44 dtk, Puffin 39 dtk, Angsa 54 dtk) lengkap dengan kit posting

File media (klip animasi, gambar planet, audio narasi) tidak disertakan di repo ini; script di atas adalah referensi pipeline-nya. Path `~/workspace/...` di script perlu disesuaikan.
