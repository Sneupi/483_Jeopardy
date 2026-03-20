# Get Started:

For replicability and simplicity, all you need to setup is run `install.sh`. This file will setup a Python virtual environment, as well as the document collection of wiki pages used by Watson.

All project collaborators should have access to a copy of the wiki document collection `wiki-subset-20140602.tar.gz`. This file will be unzipped to a folder `wiki` during install, to be used by Watson. Unfortunately this file is too large and makes the repo lag, otherwise I'd just include it.

Alternatively, if you:
- Rather not use venv, you can install `requirements.txt` directly. 
- Cannot access the required `tar.gz`, you may create your own document collection in the format of `example/wiki-example.txt` into a folder named `wiki`.

Once you have successfully setup your environment, make sure you are in the virtual environment with `source .venv/bin/activate`, then use the `Makefile` commands to `make <run/test/clean>`.

# Project Notes:
The questions were extracted from j-archive.com, from shows that took place between 2013-01-01 and 2013-01-07.


