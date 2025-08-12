

loan_amount =  int(input("enter loan amount:"))

interest = int(input("enter interest"))


loan_tenure_year = int(input("enter loan tenure in years"))

p = loan_amount

r = interest/12*100

n = loan_tenure_year * 12

"""
EMI = [P x R x (1+R)^N] / [(1+R)^N – 1]
"""

EMI = (p * r *(1+r)**n)/((1+r)**n-1)

print(EMI)

