
# num=5

# # 1,2,3,4,5

# fact=1

# for i in range(1,num+1):

#     fact=fact*i

# print(fact)




def factorial(num):#num=5 num=4 num=3 num=2 num=1 num=0

    if num ==0:

        return 1
    
    return num*factorial(num-1)#

print(factorial(5))

# call_stack

"""
5*factorial(4) 
4*factorial(3),
3 factorial(2)
2factorial(1)2
1factorial(0)1"""

# sum_n(5)
# 5+4+3+2+1


def sum_of_n(num):

    if num ==0:

        return 0
    
    return num+sum_of_n(num-1)

print(sum_of_n(6))

# 1 2 3 4 5 6

# 123, 1+2+3=6
# num=234

def sum_of_digit(num):

    if num==0:

        return 0
    
    return num%10+sum_of_digit(num//10) #3+sum_of_digit(123//10),2+sum_of_digit(12//10),1+sum_of_digit(1//10)


print(sum_of_digit(123)) 

print("value in __name__ is",__name__)

__name__

if __name__=="__main__":

    print("code executed from here")

# 
# recursion

# mediaquery
# dictionary,set,nested collection
# store
# mysql