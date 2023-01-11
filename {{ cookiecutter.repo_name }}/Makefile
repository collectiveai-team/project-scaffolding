include .env
export $(shell sed 's/=.*//' .env)


core-build:
	docker-compose build {{cookiecutter.repo_name}}-core

vastai-build: core-build
	docker-compose build {{cookiecutter.repo_name}}-vastai

vastai-push:
	docker-compose push {{cookiecutter.repo_name}}-vastai

jupyter-build: core-build
	docker-compose build {{cookiecutter.repo_name}}-jupyter

jupyter-run: jupyter-build
	docker-compose run {{cookiecutter.repo_name}}-jupyter-gpu

jupyter-run-cpu: jupyter-build
	docker-compose run {{cookiecutter.repo_name}}-jupyter-cpu
