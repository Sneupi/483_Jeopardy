# Overview

IBM’s Watson is a Question Answering (QA) system that “can compete at the human champion level in real time on the TV quiz show, Jeopardy.” While this is a complex undertaking, many of the answers to these Jeopardy questions are actually titles of Wikipedia pages. In these situations, the task reduces to
the classification of Wikipedia pages; AKA which page is the most likely answer to the given clue. This project acts as a simplified implementation of IBM's "Watson" under this premise.

This project was designed utilizing 100 questions from previous Jeopardy games, whose answers appear as Wikipedia pages, and a collection of approximately 280,000 Wikipedia pages, which include the correct answers for the above 100 questions. These questions were extracted from j-archive.com, from shows that took place between 2013-01-01 and 2013-01-07.

# Install

For replicability and simplicity on Linux systems (or WSL) run
```bash
./install.sh
```
This file will setup a Python virtual environment, the document collection of wiki pages, and the index automatically.

> [!IMPORTANT]
> To run this project as-designed, you should have access to a copy of the wiki document collection [`wiki-subset-20140602.tar.gz`](https://arizona.box.com/v/wikidata-csc483). This file will be unzipped to a folder `.wiki` during install, to be used by the system. If you cannot access the required `tar.gz`, you may create your own files in the format of `assets/corpus-example/wiki-example.txt` to folder `.wiki` and it should work the same.

# Run

Once you are successfully installed, run the project via `Makefile` commands 
```bash
make run   # Type queries by hand
```
```bash
make test  # Run pytests
```