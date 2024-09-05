$(shell touch .env)
include .env
export $(shell sed 's/=.*//' .env)


core-build:
	docker-compose build {{cookiecutter.repo_name}}-core