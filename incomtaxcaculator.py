#!/usr/bin/env python

import sys

class IncomTaxCaculator():
    def __init__(self):
        pass

    def salary_after_tax(self,user_id,salary,shebao,jishul,jishuh):

     #   try:
        salary = float(salary)
        shebao = float(shebao)
        jishul = float(jishul)
        jishuh = float(jishuh)

        shebao_cost = 0
        tax = 0
        sat = 0

        #if salary < 0:
        #    raise ValueError
        
        if salary < jishul:
            shebao_cost = jishul * shebao
            salary_tax = salary - shebao_cost
        elif salary > jishuh:
            shebao_cost = jishuh * shebao
            salary_tax = salary - shebao_cost
        else:
            shebao_cost = salary * shebao
            salary_tax = salary - shebao_cost - 3500


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
        
        tax = tax
        sat = salary - shebao_cost - tax
        
#        user_salary_tax = {"shebao_cost":format(shebao_cost,".2f"),"tax":format(tax,".2f"),"sat":format(sat,".2f")}
        
        user_salary_tax = [user_id,salary,format(shebao_cost,".2f"),format(tax,".2f"),format(sat,".2f")]

        return user_salary_tax

#    except:
#        print("Parameter Error")


if __name__ == "__main__":
    itc = IncomTaxCaculator()
    a = itc.salary_after_tax(203,5000,0.165,2193,16446)
    print(a)
