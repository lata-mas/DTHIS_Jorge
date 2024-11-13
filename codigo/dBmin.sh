#!/bin/bash

minimo="/home/pi/DTHIS/txt/dBmin.txt"

/usr/bin/sox /home/pi/DTHIS/audio.wav -n stat 2>&1 | /usr/bin/grep "Minimum amplitude:" | /usr/bin/awk '{print $3}' > $minimo
