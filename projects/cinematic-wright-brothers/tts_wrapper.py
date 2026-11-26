#!/usr/bin/env python3
"""TTS wrapper for tts_say.py --cmd: synthesizes each paragraph (line) separately
with /opt/hatch/bin/tts, then joins them with 0.65s of silence so split_takes.py
has clean pauses to cut on. Usage: tts_wrapper.py <txt> <out.wav>"""
import pathlib
import subprocess
import sys
import tempfile


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        sys.exit(f"FAILED: {' '.join(map(str, cmd))}\n{r.stderr[-1500:]}\n{r.stdout[-500:]}")
    return r


def main():
    txt, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    lines = [p.strip() for p in txt.read_text().split("\n\n") if p.strip()]
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        wavs = []
        for i, line in enumerate(lines):
            mp3 = tmp / f"line{i}.mp3"
            run(["/opt/hatch/bin/tts", "speak", "--output", str(mp3), "--text-stdin",
                 "--language", "en"], input=line)
            wav = tmp / f"line{i}.wav"
            run(["ffmpeg", "-y", "-v", "error", "-i", str(mp3), "-ar", "48000", "-ac", "1", str(wav)])
            wavs.append(wav)
        sil = tmp / "sil.wav"
        run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i",
             "anullsrc=r=48000:cl=mono", "-t", "0.65", str(sil)])
        lst = tmp / "list.txt"
        entries = []
        for i, w in enumerate(wavs):
            entries.append(f"file '{w}'")
            if i < len(wavs) - 1:
                entries.append(f"file '{sil}'")
        lst.write_text("\n".join(entries) + "\n")
        run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
             "-ar", "48000", "-ac", "1", str(out)])


if __name__ == "__main__":
    main()
