#!/usr/bin/env python


class Config:
    def __init__(self):
        pass

    def read(self,config_path):
        self._params = {}
        with open(config_path) as file:
            for line in file:
                param_list = line.split("=")
                self._params[param_list[0].strip()] = param_list[1].strip()

    def get(self,param):
        return self._params[param]

    def set(self,param,value):
        self._params[param] = value



if __name__ == "__main__":
    import sys
    print('test class Config')
    param = sys.argv[1]
    config = Config()
    config.read('./default.cfg')
    print('{} is {}'.format(param,config.get(param)))
