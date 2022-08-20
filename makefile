SHELL := /bin/bash

manage_py := python3 MySite/manage.py

runserver:
	$(manage_py) runserver