#!/bin/bash

home_path=`pwd`
pu_dir="${home_path}/pu/*"
image_dir="${home_path}/images"

files=`find $pu_dir -maxdepth 0 -type f -name *.pu`

for file in $files;
do
    echo "${file}を変換しています。\n"
    java -jar /java/plantuml.jar -o $image_dir -tsvg $file
done

echo "\n${image_dir}の中身を表示します。"
ls $image_dir

svgs=`find $image_dir -maxdepth 0 -type f -name *.svg`
echo "\n${image_dir}の中のSVGファイルを表示します。"
echo $svgs
for svg in $svgs;
do
    echo "\n${svg}の内容は以下の通りです。"
    cat $svg
done