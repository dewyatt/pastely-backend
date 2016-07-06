#!/bin/bash
set -e -u

virtualenv3 env
./env/bin/pip install -r requirements/test.txt
./env/bin/python3 manage.py test --settings=pastely.settings.test
