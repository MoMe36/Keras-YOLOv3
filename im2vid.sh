#!/bin/bash 

# Move to the images folder. With this command, images should be named 0.jpg, 1.jpg.... 12.jpg, 13.jpg and so on. 
# Concatenated video is named output.mp4 

ffmpeg -framerate 30 -i %0000d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
