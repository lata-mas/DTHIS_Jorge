#!/bin/bash

media="/home/pi/DTHIS/rms.txt"

/usr/bin/sox /home/pi/DTHIS/audio.wav -n stat 2>&1 | /usr/bin/grep "RMS     amplitude:" | /usr/bin/awk '{print $3}' > $media
