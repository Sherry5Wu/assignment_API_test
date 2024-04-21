import requests
from utils.LogUtils import my_log

# Refactor requests

# Create class request
class Request:
    # Define public method
    def __init__(self):
        self.log = my_log("Requests")
    def requests_api(self, url, data=None, json=None, headers=None, cookies=None, method="get"):
        if method == "get":
            # send get request
            self.log.debug("Send get type request")
            response = requests.get(url, data=data, json=json, headers=headers, cookies=cookies)
        elif method == "post":
            # send post request
            self.log.debug("Send post type request")
            response = requests.post(url, data=data, json=json, headers=headers, cookies=cookies)
        elif method == "patch":
            # send patch request
            self.log.debug("Send patch type request")
            response = requests.patch(url, data=data, json=json, headers=headers, cookies=cookies)

        # Get the content of the response
        code = response.status_code
        try:
            body = response.json()
        except Exception as e:
            body = response.text

        # Put the content of the response to dictionary
        res = dict()
        res["code"] = code
        res["body"] = body

        # Return the dictionary
        return res

# refactor get/post/patch method

    # define get request
    def get(self, url, **kwargs):

    # define arguments
        #url, method
    # Call public method
         return self.requests_api(url, method="get", **kwargs)

    # define post request
    def post(self, url, **kwargs):

    # define arguments
        #url, method
    # Call public method
        return self.requests_api(url, method="post", **kwargs)

    # define patch request
    def patch(self, url, **kwargs):

    # define arguments
        #url, method
    # Call public method
        return self.requests_api(url, method="patch", **kwargs)