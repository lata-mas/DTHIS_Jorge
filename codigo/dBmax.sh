#!/bin/bash

chale="/home/pi/DTHIS_jorge/dBmax.txt"

/usr/bin/sox /home/pi/DTHIS_jorge/audio.wav -n stat 2>&1 | /usr/bin/grep "Maximum amplitude:" | /usr/bin/awk '{print $3}'  > $chale
