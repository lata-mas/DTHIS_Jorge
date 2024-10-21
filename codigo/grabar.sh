#!/bin/bash

grabar="/home/pi/DTHIS/audio.wav"

arecord -D plughw:2,0 -f cd -t wav -d 15 -r 44100 $grabar
