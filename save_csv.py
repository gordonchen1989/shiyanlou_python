#!/usr/bin/env python

import csv

class SaveCSV():
    def __init__(self):
        pass

    def save_user_data(self,file_path,data):
        with open(file_path,"w") as file:
            csv.writer(file).writerows(data)



if __name__ == "__main__":
    data = [[101,3500,577.50,0.00,2922.50],
            [203,5000,825.00,20.25,4154.75],
            [309,15000,2475.00,1251.25,11273.75]
            ]

    sc = SaveCSV()
    sc.save_user_data("test.cvs",data)
