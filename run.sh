rm -rf allu/*
pytest --alluredir=allu
allure serve allu
