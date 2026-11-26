#!/bin/bash
# Usage: render45.sh <n> <slug> <HOOK TEXT UPPERCASE>
set -e
n=$1; slug=$2; hook=$3
cd ~/workspace/gta6_clips
OUT=~/workspace/goals/gta-vi-windah-basudara-shorts/files/GTA6-Windah-Klip${n}-${slug}.mp4
mkdir -p ~/workspace/goals/gta-vi-windah-basudara-shorts/files
printf '%s' "$hook" > /tmp/hook45_${n}.txt
ffmpeg -y -v error -i "raw45_${n}.mp4" -filter_complex "\
[0:v]split=2[fc][gp];\
[fc]crop=250:230:1030:390,scale=1080:720:flags=lanczos[face];\
[gp]crop=648:720:316:0,scale=1080:1200:flags=lanczos[game];\
[face][game]vstack=inputs=2,drawtext=fontfile=/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf:textfile=/tmp/hook45_${n}.txt:fontsize=56:fontcolor=white:borderw=7:bordercolor=black:shadowcolor=black@0.6:shadowx=3:shadowy=3:x=(w-text_w)/2:y=720-text_h/2[vout];\
[0:a]loudnorm=I=-14:TP=-1.5:LRA=11[aout]" \
-map "[vout]" -map "[aout]" -c:v libx264 -preset veryfast -crf 24 -c:a aac -b:a 160k -movflags +faststart "$OUT"
ffmpeg -y -v error -ss 10 -i "$OUT" -frames:v 1 "preview45_${n}.jpg"
echo "DONE $OUT"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -show_entries format=duration,size -of default=noprint_wrappers=1 "$OUT"
ffprobe -v error -select_streams a -show_entries stream=codec_name -of csv=p=0 "$OUT"
