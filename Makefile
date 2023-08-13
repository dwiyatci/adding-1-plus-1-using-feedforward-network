.PHONY: install upgrade

install:
	pip install --upgrade pip
	pip install -r requirements.txt

upgrade:
	pip install --upgrade pip
	pip install upgrade-requirements
	upgrade-requirements

run:
	python main.py
