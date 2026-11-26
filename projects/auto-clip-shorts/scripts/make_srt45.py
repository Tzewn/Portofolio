#!/usr/bin/env python3
"""Generate per-clip .srt for the 10 kandidat 15-45s clips from caps.id.srt."""
import sys
sys.path.insert(0, "~/workspace/gta6_clips")
from clean_subs import load_cues, build_segment, fmt_ts, wrap2, SRC

def ts(h, m, s):
    return h*3600 + m*60 + s

SEGMENTS = {
    1: (ts(0,19,24), ts(0,20,2)),
    2: (ts(0,22,14), ts(0,22,56)),
    3: (ts(0,37,7),  ts(0,37,52)),
    4: (ts(0,48,12), ts(0,48,56)),
    5: (ts(1,1,16),  ts(1,1,56)),
    6: (ts(1,40,2),  ts(1,40,44)),
    7: (ts(1,43,59), ts(1,44,43)),
    8: (ts(3,11,41), ts(3,12,16)),
    9: (ts(3,16,3),  ts(3,16,47)),
    10:(ts(3,32,57), ts(3,33,41)),
}

SLUGS = {
    1: "ampun-bang-jangan-bunuh",
    2: "hampir-mati-ditembakin",
    3: "udah-jatuh-ditabrak-motor",
    4: "dibegal-pas-kabur-dari-polisi",
    5: "disesatin-bocil-lompat",
    6: "m4-hilang-lori-diculik",
    7: "lompat-epic-kena-kipas",
    8: "bintang-4-darah-tinggal-dikit",
    9: "rumah-dihancurin-ular-gua",
    10:"hampir-nembak-suster",
}

OUTDIR = "~/workspace/goals/gta-vi-windah-basudara-shorts/files"

def main():
    cues = load_cues(SRC)
    only = [int(a) for a in sys.argv[1:]] or list(SEGMENTS)
    for n in only:
        s, e = SEGMENTS[n]
        seg = build_segment(cues, s, e)
        out_path = f"{OUTDIR}/GTA6-Windah-Klip{n}-{SLUGS[n]}.srt"
        with open(out_path, "w", encoding="utf-8") as f:
            for i, (st, en, tx) in enumerate(seg, 1):
                f.write(f"{i}\n{fmt_ts(st)} --> {fmt_ts(en)}\n{wrap2(tx)}\n\n")
        print(f"klip{n}: {len(seg)} cues -> {out_path}")

if __name__ == "__main__":
    main()
