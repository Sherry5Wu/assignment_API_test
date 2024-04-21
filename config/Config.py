import os
from utils.YamlUtils import YamlReader

# Get the directories of the project
# get the absolute path of the current project
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))

# Define the path for config directory
_config_path = BASE_DIR + os.sep + "config"
# Define the path for the config.yml file
_config_file_path = _config_path + os.sep + "config.yml"

# define the path for the log file
_log_path = BASE_DIR + os.sep + "logs"

# define the path for the data file
_data_path = BASE_DIR + os.sep + "data"

# define the path for the report file
_report_path = BASE_DIR + os.sep + "report"


def get_config_path():
    return _config_path


def get_config_file_path():
    return _config_file_path


def get_log_path():
    return _log_path


def get_data_path():
    return _data_path


def get_report_path():
    return _report_path


# Read the config file
# create class
class ConfigYaml:
    # initialise
    def __init__(self):
        self.config = YamlReader(get_config_file_path()).data()

    # define method to get information
    def get_config_url(self):
        return self.config["BASE"]["test"]["url"]

    def get_config_log(self):
        return self.config["BASE"]["log_level"]

    def get_config_log_extension(self):
        return self.config["BASE"]["log_extension"]

# if __name__ == "__main__":
#     config_read = ConfigYaml()
#     print(config_read.get_config_url())
#     print(config_read.get_config_log())
#     print(config_read.get_config_log_extension())
