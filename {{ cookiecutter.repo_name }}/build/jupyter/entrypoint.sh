#!/bin/env sh

# install src packages
pip install --no-deps -e /src/{{cookiecutter.package_name}}

# run jupyter
jupyter-lab --ip=0.0.0.0 --allow-root --no-browser
