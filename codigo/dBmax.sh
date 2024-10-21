#!/bin/bash

maximo="/home/pi/DTHIS/dBmax.txt"

/usr/bin/sox /home/pi/DTHIS/audio.wav -n stat 2>&1 | /usr/bin/grep "Maximum amplitude:" | /usr/bin/awk '{print $3}'  > $maximo
