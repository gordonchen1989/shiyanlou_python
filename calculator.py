#!/usr/bin/env python

import argparse,sys,incomtaxcaculator,save_csv,config,user

if __name__ == "__main__":
    
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

    user_data = user.UserData()
    user_data.read(user_data_path)
    itc = incomtaxcaculator.IncomTaxCaculator()
    data_list = []

    for user_id,salary in user_data.get_user_data().items():
        data = itc.salary_after_tax(user_id,salary,shebao,jishul,jishuh)
#        print(data)
        data_list.append(data)

    data_list.reverse() 
#    print(data_list)
    sc = save_csv.SaveCSV()
    sc.save_user_data(output_path,data_list)



#    a = itc.salary_after_tax(5000,0.165,2193,16446)
#    print(a)
