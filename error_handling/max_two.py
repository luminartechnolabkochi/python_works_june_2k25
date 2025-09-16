
"""
Error handling
1)syntax error
2)run time error

try:

except:

finally:

raise
assert



"""



def max_two(num1,num2):

    return 10


# return max of these two numbers 

# assert max_two(5,10)==10 , "test case 1 failed with second number is largest"


# assert max_two(10,5)==10 , "test case 2 failed with first number is largset"

# assert max_two(5,7) == 7,"test cae 3 failed with two diiferent parameter"


def exponent(base,power):

    result = base**power

    return result


assert exponent(5,2)==25,"test case1 failed"

assert exponent(2,3)==8,"test case2 failed"


assert exponent(2,0)==1,"test case3 failed with power as 0"

print("completed")
