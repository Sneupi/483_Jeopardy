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
collection_dir=".wiki"
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
fi

# Create bm25s index
index_dir=".bm25s"
if [ ! -d "$index_dir" ]; then

    echo -e '\033[32m'
    echo Creating index \"$index_dir\" using \"$collection_dir\".
    echo -e '\033[0m'

    ./.venv/bin/python3 utils/indexer.py $index_dir $collection_dir

else 
    echo -e '\033[32m'
    echo Directory exists \"$index_dir\". Skipping index creation.
    echo -e '\033[0m'
fi

# Create TF-IDF index
tfidf_index_dir=".tfidf"
if [ ! -d "$tfidf_index_dir" ]; then

    echo -e '\033[32m'
    echo Creating TF-IDF index \"$tfidf_index_dir\" using \"$collection_dir\".
    echo -e '\033[0m'

    ./.venv/bin/python3 utils/tfidf_indexer.py $tfidf_index_dir $collection_dir

else 
    echo -e '\033[32m'
    echo Directory exists \"$tfidf_index_dir\". Skipping TF-IDF index creation.
    echo -e '\033[0m'
fi
