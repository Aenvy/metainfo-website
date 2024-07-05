#!/bin/sh
set -e
# Creating links for ansible metainfo collection
mkdir -p src/ansible_collections/hpe/metainfo/plugins/
ln -s ../../../../module_utils src/ansible_collections/hpe/metainfo/plugins/
ln -s ${1:-../../../ansible-metainfo-collection/plugins/module_utils/ src/}
# Creating the virtual environment for required python modules
mkdir -p venv
python3 -m venv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install bottle ansible requests pymongo pystache waitress
set +e
# Then start the app by
# cd src
# python3 app.py
