# Project scaffolding for data science

A scaffolding data science project generator following _Collective AI_ standards


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or >3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip or conda depending on how you manage your Python packages:

``` bash
$ pip3 install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter git@github.com:collectiveai-team/project-scaffolding.git



### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── build-scripts
│   ├── install_script.sh
│   └── update_pkgs
├── docker-compose.yml
├── Dockerfile
├── docs
│   ├── commands.rst
│   ├── conf.py
│   ├── getting-started.rst
│   ├── index.rst
│   ├── make.bat
│   └── Makefile
├── LICENSE
├── Makefile
├── notebooks
│   ├── pipeline-example.ipynb
│   └── tips_and_tricks.ipynb
├── README.md
├── references
├── reports
│   └── figures
├── requirements.txt
├── setup.py
├── src
│   ├── {{\ cookiecutter.package_name\ }}_common
│   │   ├── {{\ cookiecutter.repo_name\ }}
│   │   │   ├── __init__.py
│   │   │   ├── serving.py
│   │   │   └── tests
│   │   │       ├── __init__.py
│   │   │       └── test_serving.py
│   │   └── setup.py
│   ├── {{\ cookiecutter.package_name\ }}_model
│   │   ├── {{\ cookiecutter.repo_name\ }}
│   │   │   ├── __init__.py
│   │   │   └── variant.yml
│   │   └── setup.py
│   └── {{\ cookiecutter.package_name\ }}_training
│       ├── {{\ cookiecutter.repo_name\ }}
│       │   ├── config.yml
│       │   ├── data
│       │   │   ├── __init__.py
│       │   │   ├── make_dataset.py
│       │   │   └── read_dataset.py
│       │   ├── features
│       │   │   ├── build_features.py
│       │   │   └── __init__.py
│       │   ├── __init__.py
│       │   ├── models
│       │   │   ├── __init__.py
│       │   │   └── train_model.py
│       │   └── reports
│       │       ├── __init__.py
│       │       └── visualize.py
│       └── setup.py
├── test_environment.py
└── tox.ini
```

### Launching Docker Container
------------
```
docker-compose build
docker-compose up -d
```

### Launching Docker Container for GPU
------------
```
docker-compose build
docker run --network host --gpus all -it -v pwd:/srv/src/ -p 8888:8888
```
