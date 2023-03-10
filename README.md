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
├── build                                   -> Docker building files & utils
│   ├── core
│   └── jupyter
├── notebooks                               -> Notebooks with experimentes and examples
│   └── ...
├── reports                                 -> Reports generated by results from experiments
│   └── ...
├── resources                               -> general resources: models, datasets, cache, etc
│   ├── cache
│   ├── models
│   ├── datasets
│   └── ...
├── scripts                                 -> utils
└── src                                     -> main root of packages
    └── {{cookiecutter.package_name}}                             -> main package
```


