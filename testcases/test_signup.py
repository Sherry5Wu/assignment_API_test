from config import Config
import os
from utils.YamlUtils import YamlReader
import pytest
from config.Config import ConfigYaml
from utils.RequestsUtils import Request
from utils.AssertUtils import AssertUtil

# 1. get test data
# 1.1 get the path of test_signup.yml
test_data_file = os.path.join(Config.get_data_path(), "test_signup.yml")

# 1.2 read the file using tools
test_data_list = YamlReader(test_data_file).data_all()


@pytest.mark.parametrize("signup", test_data_list)
def test_signup(signup):
    # initialise url, data
    url = ConfigYaml().get_config_url() + signup["url"]
    name = signup["data"]["username"]
    password = signup["data"]["password"]
    url_parameter = f'{url}?name={name}&passwd={password}'
    # post request
    request = Request()
    res = request.post(url_parameter)
#    print(res)
    testcase_name = signup["case_name"]
    case_scenario = signup["case_scenario"]
    expected_code = signup["expect_code"]
    expect_body = signup["expect_body"]
    code = res["code"]
    body = res["body"]
    print("testcase name =", testcase_name)
    print("Scenario =", case_scenario)
    print("return code =", code)
    print("expected code =", expected_code)
    print("expected body =", expect_body)
    AssertUtil().assert_code(code, expected_code)
    AssertUtil().assert_in_body(body, expect_body)