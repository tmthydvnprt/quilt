#!/usr/bin/bash

# remove trailing whitespace
find . -name "*.py" | xargs sed -i '' -e's/[ ^I]*$//'

pylint quilt > linting_report.txt

echo "project linted"
