#!/usr/bin/bash

# test project
nosetests tests -v -d --with-coverage --cover-package=quilt,tests --cover-tests --cover-erase --cover-inclusive --cover-branches &> test_report.txt.temp

# test report
echo '' > test_report.txt
echo 'Quilt Testing Report' >> test_report.txt
echo `date` >> test_report.txt
echo '=========================================' >> test_report.txt
echo '' >> test_report.txt
cat test_report.txt.temp >> test_report.txt

rm .coverage
rm test_report.txt.temp

echo "project tested"
