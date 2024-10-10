#!/bin/bash

quetal="/home/pi/DTHIS_jorge/dBmin.txt"

/usr/bin/sox /home/pi/DTHIS_jorge/audio.wav -n stat 2>&1 | /usr/bin/grep "Minimum amplitude:" | /usr/bin/awk '{print $3}' > $quetal
