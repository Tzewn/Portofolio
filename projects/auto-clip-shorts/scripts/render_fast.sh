#!/bin/bash
# Render one vertical short. Usage: render.sh <partN> <raw.mp4> <partN.srt> <output.mp4>
set -e
RAW="$1"; SRT="$2"; OUT="$3"
STYLE="FontName=Noto Sans,FontSize=54,Bold=1,PrimaryColour=&H00FFFFFF,SecondaryColour=&H0000FFFF,OutlineColour=&H00000000,BackColour=&H64000000,Outline=3,Shadow=1,BorderStyle=1,Alignment=2,MarginL=60,MarginR=60,MarginV=400,PlayResX=1080,PlayResY=1920"
ffmpeg -y -i "$RAW" -filter_complex \
"[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:6,eq=brightness=-0.18:saturation=0.65[bg];[b]scale=1080:608[fg];[bg][fg]overlay=0:400,subtitles=filename='${SRT}':force_style='${STYLE}',format=yuv420p[vout]" \
-map "[vout]" -map 0:a -af "loudnorm=I=-14:TP=-1.5:LRA=11" \
-c:v libx264 -preset veryfast -crf 24 -r 30 -c:a aac -b:a 160k -movflags +faststart -shortest "$OUT" 2>&1 | tail -n 20
ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_type,codec_name,width,height -of default=noprint_wrappers=1 "$OUT"
