# Virtual Environments

Note: venv only available with python 3. For python 2, use conda
or virtualenv

## Create virtual environment

    python3 -m venv venv/alchemy
    source venv/alchemy/bin/activate
    pip install -U pip
    pip install -r venv/requirements.txt

## Using virutal environment

Once the venv is created, you only need to run

    source venv/alchemy/bin/activate


## For jupyter dev
To develop using juyter notebooks, use the
requirements.txt file in the root folder.
This file is also used for creating binder
images (https://mybinder.org)
