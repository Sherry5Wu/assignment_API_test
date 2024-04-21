import os
import yaml

class YamlReader:
    #initialise, checking if the file exists
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("The File is not found")
        # define a parameter to save if the file is called
        self._data = None
        self._data_all = None
    # read a single file
    def data(self):
        # If it is the first time call, then read the file; otherwise, return the saved data
        if not self._data:
            with open(self.yamlf, "rb") as f:
                self._data = yaml.safe_load(f)
        return self._data
    # read multiple files
    def data_all(self):
        # If it is the first time call, then read the file; otherwise, return the saved data
        if not self._data_all:
            with open(self.yamlf, "rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all