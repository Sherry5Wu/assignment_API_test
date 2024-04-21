# <h1>API Automation using Python Pytest<h1>
-  API testing for signup, renew, validate, user, quote and weather, using Python Pytest.

## <h2>Setup:<h2>
- Download and install Python3 from [here](https://www.python.org/downloads/) (Ignore the step if you already have python installed)
- Clone this repo, navigate to assignment_API_test folder.
- Execute requirements.txt file to install all the dependent python libraries using following command and make it pass without any error: pip3 install -r requirements.txt

## <h2>Running the tests:<h2>
- Run below command to execute all the tests. This will generate log file(with name: <YY-MM-DD_HH-MM-SS>.log) in logs folder.
pytest -vs Test\test_requests.py
- Run below command to execute and generate pytest html report: 
pytest -vs --capture sys Test\test_requests.py --html=report.html
