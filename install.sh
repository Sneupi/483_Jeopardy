#!/bin/bash

# Install Python virtual environment  
if [ ! -d ".venv" ]; then
    
    echo -e '\033[32m'
    echo 'Creating Python venv to ".venv"'
    echo -e '\033[0m'

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt  
else
    echo -e '\033[32m'
    echo 'Directory exists ".venv". Skipping venv creation.'
    echo -e '\033[0m'
fi

# Unzip wiki collection file
collection_dir="wiki"
tar_file="wiki-subset-20140602.tar.gz"
if [ ! -d $collection_dir ]; then

    echo -e '\033[32m'
    echo Unzipping wiki collection \"$tar_file\" to \"$collection_dir\".
    echo -e '\033[0m'

    if [ ! -f $tar_file ]; then
        echo -e '\033[31m'
        echo Not Found: \"$tar_file\" 
        echo -e '\033[0m'
        echo Download the entire Wiki data for the project here:
        echo https://arizona.box.com/v/wikidata-csc483
        exit 1
    fi

    mkdir $collection_dir
    tar -xzvf $tar_file -C $collection_dir
    rm $collection_dir/._*

else 
    echo -e '\033[32m'
    echo Directory exists \"$collection_dir\". Skipping unzip \"$tar_file\".
    echo -e '\033[0m'
    exit 0
fi
