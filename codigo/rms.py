#!/bin/bash

puesya="/home/pi/DTHIS_jorge/rms.txt"

/usr/bin/sox /home/pi/DTHIS_jorge/audio.wav -n stat 2>&1 | /usr/bin/grep "RMS     amplitude:" | /usr/bin/awk '{print $3}' > $puesya
