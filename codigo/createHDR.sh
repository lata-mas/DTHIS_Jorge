#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")
IMG_DIR="/home/pi/DTHIS/Luminance/images"
HDR_IMG="/home/pi/DTHIS/Luminance/HDR_images"
MAPS_DIR="/home/pi/DTHIS/Luminance/maps"
OUTPUT_DIR="/home/pi/DTHIS/Luminance"

# Loop through shutter speeds and capture images
SHUTTERS=(100 500 1000 5000 10000 50000 100000 500000 1000000 2000000)

for i in "${!SHUTTERS[@]}"; do
  rpicam-still --raw -n --gain 1 -t 500 --shutter "${SHUTTERS[$i]}" -o "$IMG_DIR/$(printf "%02d" $((i+1))).jpg"
done

# Run raw2hdr with the path to the images and save as image.hdr
raw2hdr -a -e -g -f -h -w -o "$HDR_IMG/image_$DATE.hdr" "$IMG_DIR"/*dng

# Get info about the final HDR
getinfo "$HDR_IMG/image_$DATE.hdr"

# Nullify exposure value
ra_xyze -r -o "$HDR_IMG/image_$DATE.hdr" > "$OUTPUT_DIR/image_nullEV_$DATE.hdr"

# Resize image
pfilt -1 -x 1000 -y 1000 "$OUTPUT_DIR/image_nullEV_$DATE.hdr" > "$OUTPUT_DIR/image_resize_$DATE.hdr"

# Make photometric adjustment
pcomb -s 1.8 "$OUTPUT_DIR/image_resize_$DATE.hdr" > "$OUTPUT_DIR/image_photometric_$DATE.hdr"

# Change view angle for fisheye
getinfo -a "VIEW= -vta -vv 160 -vh 160" < "$OUTPUT_DIR/image_photometric_$DATE.hdr" > "$IMG_DIR/image_final_$DATE.hdr"

# Print illuminance value
echo "Total illuminance is: "
evalglare -V "$IMG_DIR/image_final_$DATE.hdr"
evalglare -V "$IMG_DIR/image_final_$DATE.hdr" > "$OUTPUT_DIR/illuminance_$DATE.txt"

# Move final HDR image to HDR_images
mv "$IMG_DIR/image_final_$DATE.hdr" "$HDR_IMG/image_final_$DATE.hdr"

# Crop to a 160
pcomb -e 'Cx:xmax/2;Cy:ymax/2;R:444.44;sq(x):x*x' -e 'inC=sq(R)-sq(x-Cx)-sq(y-Cy)' -e 'ro=if(inC,ri(1),0);go=if(inC,gi(1),0);bo=if(inC,bi(1),0)' "$HDR_IMG/image_final_$DATE.hdr" > "$HDR_IMG/image_crop_$DATE.hdr"

# Make the luminance map with configurations and save it
falsecolor -s 5000 -d 1 -i "$HDR_IMG/image_crop_$DATE.hdr" --log 3 > "$MAPS_DIR/image_map_$DATE.hdr"
