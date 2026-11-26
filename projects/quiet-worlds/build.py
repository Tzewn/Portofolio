#!/usr/bin/env python3
import subprocess, os, re, glob, json

W = os.path.expanduser('~/workspace/quiet_worlds_full')
S = os.path.expanduser('~/workspace/quiet_worlds_sample')
os.chdir(W)
FPS = 30

def run(cmd):
    print(' '.join(cmd[:6]), '...')
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:]); raise SystemExit('ffmpeg gagal')
    return r

def dur(path):
    r = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',path],capture_output=True,text=True)
    return float(r.stdout.strip())

segs = ['intro','koala','glowworm','puffin','goose','closing']
seg_dur = {s: dur(f'seg_{s}.mp3') for s in segs}
print(seg_dur)

koala_clips = sorted(glob.glob(f'{S}/media-generation-koala-anim-*.mp4'))
koala_img1 = glob.glob(f'{S}/media-generation-koala-planet-1-*.webp')[0]
koala_img2 = glob.glob(f'{S}/media-generation-koala-planet-2-*.webp')[0]
glow_img = glob.glob('media-generation-glowworm-planet-*.webp')[0]
glow_clip = glob.glob('media-generation-glowworm-anim-*.mp4')[0]
puf1_img = glob.glob('media-generation-puffin-planet-1-*.webp')[0]
puf2_img = glob.glob('media-generation-puffin-planet-2-*.webp')[0]
puf_clip = glob.glob('media-generation-puffin-anim-*.mp4')[0]
goose_img = glob.glob('media-generation-goose-planet-*.webp')[0]
goose_clip = glob.glob('media-generation-goose-anim-*.mp4')[0]

def kb(img, seconds, out, zoom_in=True):
    frames = int(seconds*FPS)
    if zoom_in:
        z = f"1+0.15*on/{frames}"
    else:
        z = f"1.15-0.15*on/{frames}"
    vf = (f"scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,"
          f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps={FPS},format=yuv420p")
    run(['ffmpeg','-y','-loop','1','-framerate',str(FPS),'-i',img,'-vf',vf,'-t',str(seconds),
         '-c:v','libx264','-preset','veryfast','-crf','20','-an',out])

def clip(src, seconds, out, slow=1.0, loops=0):
    vf = f"scale=1080:1920:flags=lanczos,fps={FPS},setpts=PTS*{slow},format=yuv420p"
    cmd = ['ffmpeg','-y']
    if loops: cmd += ['-stream_loop', str(loops)]
    cmd += ['-i',src,'-vf',vf,'-t',str(seconds),'-c:v','libx264','-preset','veryfast','-crf','20','-an',out]
    run(cmd)

scenes = []
# INTRO: 2 KB
d = seg_dur['intro']
kb(koala_img1, d/2, 'sc_intro1.mp4', True); scenes.append('sc_intro1.mp4')
kb(koala_img2, d-d/2, 'sc_intro2.mp4', True); scenes.append('sc_intro2.mp4')
# KOALA: 4 clips slowed
d = seg_dur['koala']; slow = d/40.0
for i,c in enumerate(koala_clips):
    out = f'sc_koala{i+1}.mp4'
    clip(c, d/4, out, slow=slow); scenes.append(out)
# GLOWWORM: clip looped + KB
d = seg_dur['glowworm']
clip(glow_clip, 22.0, 'sc_glow1.mp4', slow=1.1, loops=3); scenes.append('sc_glow1.mp4')
kb(glow_img, d-22.0, 'sc_glow2.mp4', True); scenes.append('sc_glow2.mp4')
# PUFFIN: clip looped + KB kitchen
d = seg_dur['puffin']
clip(puf_clip, 19.0, 'sc_puf1.mp4', slow=1.05, loops=3); scenes.append('sc_puf1.mp4')
kb(puf2_img, d-19.0, 'sc_puf2.mp4', True); scenes.append('sc_puf2.mp4')
# GOOSE: clip looped + KB
d = seg_dur['goose']
clip(goose_clip, 20.0, 'sc_goose1.mp4', slow=1.05, loops=3); scenes.append('sc_goose1.mp4')
kb(goose_img, d-20.0, 'sc_goose2.mp4', True); scenes.append('sc_goose2.mp4')
# CLOSING
kb(koala_img1, seg_dur['closing'], 'sc_closing.mp4', False); scenes.append('sc_closing.mp4')

# concat video
with open('concat_v.txt','w') as f:
    for s in scenes: f.write(f"file '{s}'\n")
run(['ffmpeg','-y','-f','concat','-safe','0','-i','concat_v.txt','-c','copy','video_silent.mp4'])

# concat audio
with open('concat_a.txt','w') as f:
    for s in segs: f.write(f"file 'seg_{s}.mp3'\n")
run(['ffmpeg','-y','-f','concat','-safe','0','-i','concat_a.txt','-c:a','aac','-b:a','160k','narasi_full.m4a'])

# ---- SRT ----
def sentences(text):
    parts = re.split(r'(?<=[.?!])\s+', text.strip())
    cues = []
    for p in parts:
        words = p.split()
        # chunk into <=8 words
        for i in range(0, len(words), 8):
            cues.append(' '.join(words[i:i+8]))
    return cues

def fmt(t):
    h=int(t//3600); m=int(t%3600//60); s=t%60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace('.',',')

def wrap(text, width=34):
    words=text.split(); lines=[]; cur=''
    for w in words:
        if len(cur)+len(w)+1<=width: cur=(cur+' '+w).strip()
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return '\n'.join(lines[:2])

offsets={}; t=0
for s in segs: offsets[s]=t; t+=seg_dur[s]
total=t

srt_lines=[]; idx=1
rating_windows={}
planet_titles={'koala':'Planet 01 — Koala','glowworm':'Planet 02 — Glowworm','puffin':'Planet 03 — Puffin','goose':'Planet 04 — Angsa'}
ratings={'koala':'Danger 1/5 • Supplies 4/5','glowworm':'Danger 4/5 • Supplies 2/5','puffin':'Danger 3/5 • Supplies 4/5','goose':'Danger 5/5 • Supplies 4/5'}
for s in segs:
    text=open(f'seg_{s}.txt').read()
    cues=sentences(text)
    total_words=sum(len(c.split()) for c in cues)
    ct=offsets[s]
    for c in cues:
        cd=seg_dur[s]*len(c.split())/total_words
        srt_lines.append(f"{idx}\n{fmt(ct)} --> {fmt(ct+cd)}\n{wrap(c)}\n")
        idx+=1; ct+=cd
    if s in ratings:
        # rating spoken in last sentence: last ~2 cues worth; use final 18% of segment
        rating_windows[s]=(offsets[s]+seg_dur[s]*0.82, offsets[s]+seg_dur[s])

open('subs_full.srt','w').write('\n'.join(srt_lines))
json.dump({'offsets':offsets,'seg_dur':seg_dur,'rating_windows':rating_windows,'total':total}, open('timing.json','w'), indent=1)
print('total', total)
print('scenes ok', scenes)
