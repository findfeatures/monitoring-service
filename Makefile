SHELL := /bin/bash

ALLURE_DIR ?= .allure
COVERAGE_DIR ?= .coverage-html

export ARGS

test: coverage check-coverage

static:
	pre-commit run --all-files

coverage:
	coverage run --concurrency=eventlet --source monitor --branch -m pytest --alluredir=$(ALLURE_DIR) tests$(ARGS)
	coverage html -d $(COVERAGE_DIR)

check-coverage:
	coverage report -m --fail-under 100

run:
	nameko run --config config.yml monitoring.service:MonitoringService

build-image:
	docker build -t calumwebb/monitoring-service:$(TAG) .;

push-image:
	docker push calumwebb/monitoring-service:$(TAG)