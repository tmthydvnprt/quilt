#!/usr/bin/bash

nosetests tests -v -d --with-coverage --cover-package=quilt,tests --cover-tests --cover-erase --cover-inclusive --cover-branches &> test_report.txt

rm .coverage

echo "project tested"
