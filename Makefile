PYTHON ?= python3

help:
	@echo
	@echo "clean       - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc   - remove Python file artifacts"
	@echo "clean-test  - remove test and coverage artifacts"
	@echo
	@echo "lint     - check style with flake8"
	@echo "test     - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo
	@echo "docs    - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist    - package"
	@echo "install - install the package to the active Python's site-packages"
	@echo

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

zart:
	@echo "rendering zart"
#	python generators/

zahar:
	@echo "rendering zahar"

commands:
	@echo "rendering commands"

options:
	@echo "rendering options"

engine:
	@echo "rendering engine"

generate:
	@echo "rendering generate"

test:
	@echo "test"

docs:
	@pip3 install --quiet cogapp
	@cog.py -d -c -o README.md README.md.cog

.PHONY: clean-pyc clean-build docs clean
