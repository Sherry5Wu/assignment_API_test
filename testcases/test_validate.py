from config import Config
import os
from utils.YamlUtils import YamlReader
import pytest
from config.Config import ConfigYaml
from utils.RequestsUtils import Request
from utils.AssertUtils import AssertUtil

# 1. get test data
# 1.1 get the path of test_signup.yml
test_data_file = os.path.join(Config.get_data_path(), "test_validate.yml")

# 1.2 read the file using tools
test_data_list = YamlReader(test_data_file).data_all()


@pytest.mark.parametrize("validate", test_data_list)
def test_validate(validate):
    # initialise url, data
    url = ConfigYaml().get_config_url() + validate["url"]
    token = validate["data"]["token"]
    url_parameter = f'{url}?token={token}'
    # post request
    request = Request()
    res = request.get(url_parameter)
#    print(res)
    testcase_name = validate["case_name"]
    case_scenario = validate["case_scenario"]
    expected_code = validate["expect_code"]
    code = res["code"]
    print("testcase name =", testcase_name)
    print("Scenario =", case_scenario)
    print("return code =", code)
    print("expected code =", expected_code)
    print("parameter token =", token)
    print("response =", res)
    AssertUtil().assert_code(code, expected_code)
    if code == 200:
        body = res["body"]
        print("body =", body)
        expected_body = validate["expect_body"]
        print("expect body=", expected_body)
#        AssertUtil().assert_body(body, expected_body)