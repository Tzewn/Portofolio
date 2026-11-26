#!/usr/bin/env python3
import subprocess, os, re, json
W=os.path.expanduser('~/workspace/quiet_worlds_full'); os.chdir(W)
timing=json.load(open('timing.json'))
offsets=timing['offsets']; seg_dur=timing['seg_dur']; rw=timing['rating_windows']

# SRT -> ASS (1080x1920)
srt=open('subs_full.srt').read().strip().split('\n\n')
def to_ass_time(s):
    h,m,rest=s.split(':'); sec,ms=rest.split(',')
    return f"{int(h)}:{m}:{sec}.{ms[:2]}"
events=[]
for block in srt:
    lines=block.strip().split('\n')
    if len(lines)<3: continue
    start,end=lines[1].split(' --> ')
    text='\\N'.join(lines[2:])
    events.append(f"Dialogue: 0,{to_ass_time(start)},{to_ass_time(end)},Sub,,0,0,0,,{text}")
ass="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Noto Sans,54,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,4,1,2,60,60,180,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(events) + "\n"
open('subs_full.ass','w').write(ass)

FONT='/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf'
titles={'koala':'Planet 01 — Koala','glowworm':'Planet 02 — Glowworm','puffin':'Planet 03 — Puffin','goose':'Planet 04 — Angsa'}
ratings={'koala':'Danger 1/5 • Supplies 4/5','glowworm':'Danger 4/5 • Supplies 2/5','puffin':'Danger 3/5 • Supplies 4/5','goose':'Danger 5/5 • Supplies 4/5'}
filters=[]
for k,txt in titles.items():
    fn=f'title_{k}.txt'; open(fn,'w').write(txt)
    a=offsets[k]; b=a+5
    filters.append(f"drawtext=fontfile={FONT}:textfile={fn}:fontsize=68:fontcolor=white:borderw=3:bordercolor=black:x=(w-text_w)/2:y=150:enable='between(t\\,{a:.2f}\\,{b:.2f})'")
for k,txt in ratings.items():
    fn=f'rating_{k}.txt'; open(fn,'w').write(txt)
    a,b=rw[k]
    filters.append(f"drawtext=fontfile={FONT}:textfile={fn}:fontsize=58:fontcolor=white:borderw=3:bordercolor=black:x=(w-text_w)/2:y=h-470:enable='between(t\\,{a:.2f}\\,{b:.2f})'")
vf=",".join(filters)+",subtitles=subs_full.ass"
out=os.path.expanduser('~/workspace/your_files/QuietWorlds-4-Planet-Explainer.mp4')
cmd=['ffmpeg','-y','-i','video_silent.mp4','-i','narasi_full.m4a','-vf',vf,
     '-af','loudnorm=I=-14:TP=-1.5:LRA=11',
     '-c:v','libx264','-preset','veryfast','-crf','23','-c:a','aac','-b:a','160k',
     '-movflags','+faststart','-shortest',out]
print('rendering...')
r=subprocess.run(cmd,capture_output=True,text=True)
print('rc',r.returncode)
if r.returncode!=0: print(r.stderr[-4000:])
else:
    import shutil
    shutil.copy('subs_full.srt', os.path.expanduser('~/workspace/your_files/QuietWorlds-4-Planet-Explainer.srt'))
    print('done')
