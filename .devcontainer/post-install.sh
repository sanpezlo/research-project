#!/bin/bash
set -ex

echo 'alias ll="ls -alF"' >> $HOME/.bashrc
echo 'alias la="ls -A"' >> $HOME/.bashrc
echo 'alias l="ls -CF"' >> $HOME/.bashrc

WORKSPACE_DIR=$(pwd)

poetry config cache-dir ${WORKSPACE_DIR}/.cache
poetry config virtualenvs.in-project true
poetry install

echo "Done!"