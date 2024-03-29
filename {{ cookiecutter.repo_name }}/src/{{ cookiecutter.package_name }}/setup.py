from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='{{ cookiecutter.package_name }}',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    url='{{ cookiecutter.git_repo_url }}',
    install_requires=required,
    package_data={'': ['*.yml', '*.yaml']},
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 3"],
)
