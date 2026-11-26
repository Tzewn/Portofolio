import re
from pathlib import Path

def parse_srt(path):
    text = Path(path).read_text(encoding='utf-8', errors='ignore')
    blocks = re.split(r'\n\s*\n', text.strip())
    cues=[]
    for b in blocks:
        lines=b.strip().splitlines()
        ts=None; txt=[]
        for ln in lines:
            if '-->' in ln: ts=ln.strip()
            elif ts is not None: txt.append(ln.strip())
        if not ts: continue
        m=re.match(r'(\d+):(\d+):(\d+),(\d+)\s+-->\s+(\d+):(\d+):(\d+),(\d+)', ts)
        if not m: continue
        h1,m1,s1,ms1,h2,m2,s2,ms2=map(int,m.groups())
        cues.append((h1*3600+m1*60+s1+ms1/1000, h2*3600+m2*60+s2+ms2/1000, ' '.join(txt)))
    return cues

def ass_time(sec):
    h=int(sec//3600); m=int((sec%3600)//60); s=sec%60
    return f"{h}:{m:02d}:{s:05.2f}"

cues=parse_srt(Path.home()/"workspace/gta6_reels8/reel1.srt")
events=[]
for start,end,text in cues:
    words=text.split()
    if not words: continue
    # chunks of 2 words (last may be 1)
    chunks=[]
    for i in range(0,len(words),2):
        chunks.append(words[i:i+2])
    total_words=len(words)
    dur=end-start
    t=start
    for ch in chunks:
        cdur=dur*len(ch)/total_words
        label=' '.join(ch)
        # Title Case: capitalize first letter of each word, keep rest as-is lower? Use .title() carefully
        label=' '.join(w[:1].upper()+w[1:] if w else w for w in label.split())
        # ASS escape braces
        label=label.replace('{','(').replace('}',')')
        events.append((t,t+cdur,label))
        t+=cdur

header="""[Script Info]
Title: Reel1 Kai Karaoke
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Karaoke,Noto Sans,72,&H0000FFFF,&H0000FFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,4,1,2,40,40,500,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
out=Path.home()/"workspace/gta6_reels8/reel1_kai.ass"
with open(out,'w',encoding='utf-8') as f:
    f.write(header)
    for s,e,t in events:
        f.write(f"Dialogue: 0,{ass_time(s)},{ass_time(e)},Karaoke,,0,0,0,,{t}\n")
print(f"Wrote {out} with {len(events)} karaoke events from {len(cues)} cues")
for s,e,t in events[:8]:
    print(ass_time(s), ass_time(e), t)
print("...")
# show around 30s
for s,e,t in events:
    if 29 < s < 35:
        print(ass_time(s), ass_time(e), t)
