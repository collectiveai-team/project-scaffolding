#!/bin/env sh

# Clone the repo
git clone -b dev git@{{cookiecutter.git_repo_url}}.git
ln -s $PWD/{{cookiecutter.repo_name}}/resources /resources

# Install packages
pip install --no-deps -e $PWD/{{cookiecutter.package_name}}/src/{{cookiecutter.package_name}}


# Jupyter
jupyter-lab --ip=0.0.0.0 --allow-root --no-browser --port=8080
