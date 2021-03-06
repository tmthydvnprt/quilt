#!/usr/bin/bash

# remove trailing whitespace
find . -name '*.py' | xargs sed -i '' -e's/[ ^I]*$//'

# lint project
echo '' > linting_report.txt
echo 'Quilt Linting Report' >> linting_report.txt
echo `date "+%Y-%m-%d %H:%M:%S %z"` >> linting_report.txt
echo '=========================================' >> linting_report.txt
echo '' >> linting_report.txt
pylint quilt >> linting_report.txt

echo >> linting_report.txt
echo 'Tests Linting Report' >> linting_report.txt
echo `date "+%Y-%m-%d %H:%M:%S %z"` >> linting_report.txt
echo '=========================================' >> linting_report.txt
echo '' >> linting_report.txt
pylint tests >> linting_report.txt

echo 'project linted'