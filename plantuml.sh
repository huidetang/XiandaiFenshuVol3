#!/bin/bash

home_path=`pwd`
pu_dir="${home_path}/pu/*"
image_dir="${home_path}/images"

files=`find $pu_dir -maxdepth 0 -type f -name *.pu`

for file in $files;
do
    echo "${file}を変換しています。"
    java -jar /java/plantuml.jar -o $image_dir -tsvg $file
done

svgs=`find "${image_dir}" -maxdepth 0 -type f -name *.svg`
for svg in $svgs;
do
    echo "${svg}の内容は以下の通りです。"
    cat $svg
done