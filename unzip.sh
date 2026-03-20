#!/bin/bash

# Unzip wiki collection file

collection_dir="wiki"
tar_file="wiki-subset-20140602.tar.gz"

if [ ! -d $collection_dir ]; then

    if [ ! -f $tar_file ]; then
        echo Not Found: \"$tar_file\" 
        echo Download the entire Wiki data for the project here:
        echo https://arizona.box.com/v/wikidata-csc483
        exit 1
    fi

    mkdir $collection_dir
    tar -xzvf $tar_file -C $collection_dir
    rm $collection_dir/._*

else 
    echo Directory exists \"$collection_dir\". Skipping unzip \"$tar_file\".
    exit 0
fi
