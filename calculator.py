#!/usr/bin/env python

import sys

def salary_after_tax(salary):

 #   try:
    salary = float(salary)
    if salary < 0:
        raise ValueError

    salary_tax = salary - (salary * 0.165) - 3500

    tax = 0
    sat = 0

    if salary_tax < 0:
        tax = 0
    elif salary_tax <= 1500:
        tax = salary_tax * 0.03 - 0
    elif salary_tax <= 4500:
        tax = salary_tax * 0.1 - 105
    elif salary_tax <= 9000:
        tax = salary_tax * 0.2 - 555
    elif salary_tax <= 35000:
        tax = salary_tax * 0.25 - 1005
    elif salary_tax <= 55000:
        tax = salary_tax * 0.3 - 2755
    elif salary_tax <= 80000:
        tax = salary_tax * 0.35 - 5505
    else:
        tax = salary_tax * 0.45 - 13505
    
    sat = salary - (salary * 0.165) - tax
    return format(sat,".2f")

#    except:
#        print("Parameter Error")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Parameter Error")

#    salary_dict = {}
    try:
        for i in sys.argv[1:]:
            temp = i.split(":")
#            salary_dict[temp[0]] = int(temp[1])
            print(temp[0]+":"+salary_after_tax(int(temp[1])))
    except:
        print("Parameter Error")

#    for k,v in salary_dict.items():
#        print(k+":"+salary_after_tax(v))



