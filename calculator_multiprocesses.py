#!/usr/bin/env python

import argparse,sys,incomtaxcaculator,save_csv,config,user
from multiprocessing import Process, Queue
import time

#if __name__ == "__main__":

def read_data(q1,user_data_path):
    user_data = user.UserData()
    user_data.read(user_data_path)

    q1.put(user_data):

def calculator_tax(q1,q2)
    while True: 
        user_data = q1.get()
        if user_data is not None:
            break
        time.sleep(1)

    itc = incomtaxcaculator.IncomTaxCaculator()
    data_list = []

    for user_id,salary in user_data.get_user_data().items():
        data = itc.salary_after_tax(user_id,salary,shebao,jishul,jishuh)
        data_list.append(data)

    data_list.reverse()

    q2.put(data_list)

def output_data(q2,output_path):
    sc = save_csv.SaveCSV()
    while True:
        data_list = q2.get()
        if data_list is not None:
            break
        time.sleep(1)

    sc.save_user_data(output_path,data_list)

def main():
    q1 = Queue()
    q2 = Queue()
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('-c', type=str,help='config file path')
    parser.add_argument('-d', type=str,help='user data path')
    parser.add_argument('-o', type=str,help='outputpath')
    args = parser.parse_args()
    
    config_path = args.c
    user_data_path = args.d
    output_path = args.o

    config = config.Config()
    config.read(config_path)

    shebao = float(config.get("YangLao")) + float(config.get("YiLiao")) + float(config.get("ShiYe")) + float(config.get("GongShang")) + float(config.get("ShengYu")) + float(config.get("GongJiJin"))

    jishul = float(config.get("JiShuL"))
    jishuh = float(config.get("JiShuH"))

    p1 = Process(target=read_data, args=(q1,user_data_path,)).start()
    p2 = Process(target=calculator_tax, args=(q1,q2,)).start()
    p3 = Process(target=output_data, args=(q2,output_path,)).start()

    p1.join()
    p2.join()
    p3.join()


if __name__ == "__main__":
    main()
