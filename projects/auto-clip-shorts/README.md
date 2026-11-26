# Auto-Clip Shorts — pipeline video vertikal

Workflow dan script untuk mengubah video panjang (livestream/gameplay/podcast) menjadi klip vertikal 1080×1920 siap Shorts/Reels/TikTok.

## Gaya yang dipakai (MotionStyle)

- Panel atas 40%: facecam proporsional di tengah, di atas latar gameplay blur
- Panel bawah 60%: gameplay center-crop mengisi panel penuh edge-to-edge
- Tanpa teks hook di tengah, tanpa subtitle terbakar (file `.srt` tetap dibuat terpisah)
- Audio dinormalisasi ke -14 LUFS

## Isi folder

- `SKILL.md` + `skill.yaml` — workflow lengkap: pilih momen dari caption/transcript dulu, buat daftar kandidat untuk dipilih, render hanya segmen yang dipakai, berhenti saat kena rate-limit/bot-check (tidak retry membabi buta)
- `scripts/clean_subs.py`, `clean_reels8.py` — membersihkan caption mentah jadi baris subtitle yang rapi
- `scripts/make_srt45.py`, `make_kai_ass.py` — membuat file subtitle `.srt`/`.ass` per klip
- `scripts/dl45_all.sh` — mengunduh hanya segmen yang akan dirender
- `scripts/render45.sh`, `render.sh`, `render_fast.sh` — render vertikal dengan FFmpeg (crop facecam + gameplay, hook text, loudnorm) + cek durasi/resolusi/audio dengan ffprobe
- `scripts/kandidat-15-45s-2026-11-26.txt` — contoh daftar kandidat momen (menegangkan/lucu/seru) beserta timestamp

## Contoh hasil

- https://youtube.com/shorts/mWWHQ3jTOh8
- https://youtube.com/shorts/USLnIBNBRfw

Catatan: script memakai path contoh `~/workspace/...` — sesuaikan dulu. Hak atas video sumber milik pemiliknya; repo ini tidak menyertakan file video apa pun.
