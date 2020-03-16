#!/usr/bin/env python

import csv

class UserData:
    def __init__(self):
        self._user_data = {}

    def read(self,data_path):
        with open(data_path) as file:
            self._data_list = list(csv.reader(file))
            for i in range(len(self._data_list)):
                self._user_id = self._data_list[i][0]
                self._user_salary = self._data_list[i][1]
                self._user_data[self._user_id] = self._user_salary

    def get_user_data(self):
        return self._user_data


if __name__ == "__main__":
    print("UserData test")
    userdata = UserData()
    userdata.read("./userdata.csv")
    data = userdata.get_user_data()
    for user_id,salary in data.items():
        print("id:{},salary:{}".format(user_id,salary))
