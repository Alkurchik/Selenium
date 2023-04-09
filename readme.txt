pytest -s -v --browser chrome  --alluredir=./allure-results
pytest -s -v tests_API\test_getting_records.py  --alluredir=./allure-results
allure serve allure-results


docker build -t automation-tests .
docker run automation-tests
docker cp $(docker ps -a -q | head -1):usr/lessons/allureResults .
