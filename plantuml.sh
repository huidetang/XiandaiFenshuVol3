#!/bin/bash

home_path=`pwd`
pu_dir="${home_path}/pu/*"
image_dir="${home_path}/images"

files=`find $pu_dir -maxdepth 0 -type f -name *.pu`

for file in $files;
do
    echo $file
    java -jar plantuml.jar -o $image_dir -tsvg $file
done