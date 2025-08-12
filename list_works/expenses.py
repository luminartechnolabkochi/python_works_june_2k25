# create a list expenses [10000,12000,13000,14000]
# update 12000 as 12500
# display all expenses
# display total expenses
# dispaly highest expense
# display avg expense
 
# -ve       -4    -3    -2    -1
expenses= [10000,12000,13000,14000]
# +ve        0      1     2     3

total_exp = sum(expenses)

print(total_exp)

costly_exp = max(expenses)

print(costly_exp)


avg_expe = total_exp /len(expenses)

print(avg_expe)

