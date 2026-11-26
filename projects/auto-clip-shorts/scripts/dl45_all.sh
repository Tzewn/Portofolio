#!/bin/bash
cd ~/workspace/gta6_clips
YT=~/workspace/tools/venv/bin/yt-dlp
declare -a SEGS=(
"2 00:22:14 00:22:56"
"3 00:37:07 00:37:52"
"4 00:48:12 00:48:56"
"5 01:01:16 01:01:56"
"6 01:40:02 01:40:44"
"7 01:43:59 01:44:43"
"8 03:11:41 03:12:16"
"9 03:16:03 03:16:47"
"10 03:32:57 03:33:41"
)
for entry in "${SEGS[@]}"; do
  set -- $entry
  n=$1; start=$2; end=$3
  echo "=== SEGMENT $n $start-$end $(date +%H:%M:%S) ===" >> dl45.log
  $YT --js-runtimes node:/usr/bin/node --download-sections "*$start-$end" -f "bv*[height<=720]+ba/b[height<=720]" --merge-output-format mp4 -o "raw45_$n.mp4" "https://www.youtube.com/watch?v=03qhcshfeMY" >> dl45.log 2>&1
  rc=$?
  echo "SEGMENT $n exit=$rc" >> dl45.log
  if [ $rc -ne 0 ]; then
    echo "STOP: segment $n failed rc=$rc" >> dl45.log
    echo "STOPPED_AT_$n"
    exit 1
  fi
  echo "OK_$n"
  sleep 10
done
echo "ALL_DONE"
