from utils.requests_utils import Request

def happy_test_1():
    name = "sherry"
    password = "sherry123"
    url = f'http://127.0.0.1:8080/api/v1/signupsrv/signup?name={name}&passwd={password}'
    request = Request()
    response = request.post(url)
    print(response)

if __name__ == "__main__":
    happy_test_1()
