import datetime
import logging
import os

from config import Config
from config.Config import ConfigYaml

# define a mapping of log level
log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}


# encapsulate log tool class
# 1. create class
class Logger:
    # 2. define parameters
    # the file name for output, loggername, the level of log
    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file  # extension name, configure in config file
        self.log_name = log_name  # parameter
        self.log_level = log_level  # configure in config file

        # 3. write the output console or a file
        # output to console
        # 1. set logger name
        self.logger = logging.getLogger(self.log_name)
        # 2. set the level of log
        self.logger.setLevel(log_l[self.log_level])

        # check if the handler exists
        if not self.logger.handlers:
            # 3.1 output to the console
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
            fh_stream.setFormatter(formatter)

            # 3.2 output to a file
            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)

            # 4 add handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)


# 1. initialise the data of parameters: the name of log, the level of the log
# 1.1 the format of the log name = path of the file logs + time + extension name
# path of the file logs
log_path = Config.get_log_path()

# time
current_time = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
# extension name
log_extension = ConfigYaml().get_config_log_extension()
logfile_path = os.path.join(log_path, current_time + log_extension)

# 1.2 the level of the log
loglevel = ConfigYaml().get_config_log()


# 2. external methods: initialise the log class that using by other classes
def my_log(log_name=__file__):
    return Logger(log_file=logfile_path, log_name=log_name, log_level=loglevel).logger

# if __name__ == "__main__":
#     my_log().debug("this is a debug")
