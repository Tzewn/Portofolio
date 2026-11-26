#!/usr/bin/env python3
"""Slice YouTube auto-caption SRT to clip segments, retime 0-based, clean rolling overlap."""
import re, sys

SRC = "~/workspace/gta6_clips/caps.id.srt"

SEGMENTS = {
    1: (3*3600+5*60+20, 3*3600+7*60+13),
    2: (3*3600+37*60+25, 3*3600+39*60+9),
    3: (3*3600+40*60+9, 3*3600+41*60+45),
    4: (3*3600+42*60+50, 3*3600+44*60+40),
}

def parse_ts(s):
    h, m, rest = s.split(":")
    sec, ms = rest.split(",")
    return int(h)*3600 + int(m)*60 + int(sec) + int(ms)/1000

def fmt_ts(sec):
    sec = max(0.0, sec)
    h = int(sec//3600); m = int(sec%3600//60); s = int(sec%60); ms = int(round((sec-int(sec))*1000))
    if ms == 1000:
        s += 1; ms = 0
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def load_cues(path):
    text = open(path, encoding="utf-8").read()
    cues = []
    for b in re.split(r"\n\s*\n", text.strip()):
        lines = [l.strip() for l in b.strip().splitlines() if l.strip()]
        if len(lines) < 3:
            continue
        m = re.match(r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})", lines[1])
        if not m:
            continue
        cues.append((parse_ts(m.group(1)), parse_ts(m.group(2)), " ".join(lines[2:])))
    return cues

FIXES = [
    (r"\bMendz\b", "Mendez"), (r"\bMendes\b", "Mendez"), (r"\bMendez\b", "Mendez"),
    (r"\bGalerki\b", "Galecki"), (r"\bGaleki\b", "Galecki"), (r"\bGaler\b", "Galecki"),
    (r"\bWinda\b", "Windah"), (r"\bLinda\b", "Lucia"),
    (r"\bbuzer\b", "buzzer"), (r"\bpolicy\b", "police"), (r"\bPolis\b", "Police"),
]

def clean_text(t):
    t = re.sub(r"\[\s*__\s*\]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    for pat, rep in FIXES:
        t = re.sub(pat, rep, t)
    return t

def wrap2(text, maxlen=38):
    words = text.split()
    if len(text) <= maxlen:
        return text
    # split near middle
    best = None
    for i in range(1, len(words)):
        l1 = " ".join(words[:i]); l2 = " ".join(words[i:])
        if len(l1) <= maxlen and len(l2) <= maxlen+8:
            score = abs(len(l1)-len(l2))
            if best is None or score < best[0]:
                best = (score, l1 + "\n" + l2)
    if best:
        return best[1]
    return text

def build_segment(cues, start, end):
    # collect overlapping cues, clip to [start,end], retime
    raw = []
    for st, en, tx in cues:
        if en < start or st > end:
            continue
        tx = clean_text(tx)
        if not tx:
            continue
        raw.append([max(st, start)-start, min(en, end)-start, tx])
    # Merge rolling overlaps: if next text starts with / contains previous tail, merge.
    merged = []
    for st, en, tx in raw:
        if merged:
            pst, pen, ptx = merged[-1]
            # exact duplicate or contained
            if tx == ptx:
                merged[-1][1] = max(pen, en)
                continue
            # rolling: new cue repeats previous words then continues -> keep longer, extend start to prev start
            if tx.startswith(ptx) or ptx in tx:
                merged[-1] = [pst, max(pen, en), tx if len(tx) >= len(ptx) else ptx]
                continue
            if ptx.startswith(tx):
                merged[-1][1] = max(pen, en)
                continue
            # word-overlap merge: find overlap of suffix/prefix >=2 words
            pw = ptx.split(); nw = tx.split()
            overlap = 0
            for k in range(min(len(pw), len(nw)), 1, -1):
                if [w.lower().strip(".,!?") for w in pw[-k:]] == [w.lower().strip(".,!?") for w in nw[:k]]:
                    overlap = k
                    break
            if overlap >= 2 and st < pen + 1.0:
                merged[-1] = [pst, max(pen, en), ptx + " " + " ".join(nw[overlap:])]
                continue
        merged.append([st, en, tx])
    # Fix overlaps: cap each end at next start; enforce min duration 0.8s, max 5s; split long cues
    out = []
    for i, (st, en, tx) in enumerate(merged):
        nxt = merged[i+1][0] if i+1 < len(merged) else end-start
        en = min(en, nxt) if nxt > st else en
        if en - st < 0.8:
            en = min(st + 0.8, nxt) if nxt > st+0.4 else st+0.8
        # split very long text into sequential chunks
        if len(tx) > 76 and en - st > 3.0:
            words = tx.split()
            mid = len(words)//2
            tmid = st + (en-st)*0.5
            out.append((st, tmid, " ".join(words[:mid])))
            out.append((tmid, en, " ".join(words[mid:])))
        else:
            out.append((st, en, tx))
    return out

def main():
    cues = load_cues(SRC)
    for n, (s, e) in SEGMENTS.items():
        seg = build_segment(cues, s, e)
        out_path = f"~/workspace/gta6_clips/part{n}.srt"
        with open(out_path, "w", encoding="utf-8") as f:
            for i, (st, en, tx) in enumerate(seg, 1):
                f.write(f"{i}\n{fmt_ts(st)} --> {fmt_ts(en)}\n{wrap2(tx)}\n\n")
        print(f"part{n}: {len(seg)} cues -> {out_path}")
        for st, en, tx in seg:
            print(f"  {fmt_ts(st)}-{fmt_ts(en)} {tx}")

if __name__ == "__main__":
    main()
