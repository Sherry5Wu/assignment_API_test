import json

from utils.LogUtils import my_log


# 1. define encapsulated class
class AssertUtil:

    # 2. initialise data and log
    def __init__(self):
        self.log = my_log("AssertUtil")

    def assert_code(self, code, expected_code):
        """
        Verify that the returned codes are equal
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("Code error. Code is %s, expected code is %s." % (code, expected_code))
            raise

    def assert_body(self, body, expected_body):
        """
        Verify that the returned bodies are equal
        :param body:
        :param expected_body:
        :return:
        """
        try:
            assert body == expected_body
            return True
        except:
            self.log.error("Body error. Body is %s, expected body is %s." % (body, expected_body))
            raise

    def assert_in_body(self, body, expected_body):
        """
        Verify that the returned body includes expected body
        :param body:
        :param expected_body:
        :return:
        """
        try:
            body = json.dumps(body)  # if the body isn't json type , then convert it into json type
            assert expected_body in body
            return True
        except:
            self.log.error("Body isn't included. Body is %s, expected body is %s." % (body, expected_body))
            raise

