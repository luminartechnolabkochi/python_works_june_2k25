
def greetings(name):

    print(f"Hello {name}")


greetings("Jhon")


# function with parameter and return value

def add_numbers(num1,num2):

    result = num1 + num2

    return result

add_result = add_numbers(100,200)

print(add_result)



# create a function odd_even with one parameter [num] 
#  function return odd if num is odd else return even

def odd_even(num):

    return f"even" if num % 2==0 else "odd"
    

print(odd_even(12))


# create a function last_digit_max with two parameter num1,num2
# function should return num1 if last digit of num1 is > last digit of num2 else 
# return num2
# print(last_digit_max(872,179)) #179
# print(last_digit_max(872,171)) #872


def last_digit_max(num1,num2):

    return num1 if num1%10 > num2%10 else num2

print(last_digit_max(872,179))









def smart_div(num1=10,num2=8):

    return num1-num2


print(smart_div(20,8))


# create a function exponent with two parms base,power


# exponent(3,3)


def exponent(base,power=1):

    return base ** power
  
print(exponent(3))




# write a function is_leap_year with one parameter year 
# return True if year is leap year else return False

def is_leap_year(year):

    if year % 100==0 and year%400==0 or year%100!=0 and year%4==0:

        return True
    else:

        return False
    
print(is_leap_year(2024))


"""
Q1)
    create a function is_prime with one parameter num
    return True if number is prime else return False
"""

"""
Q2
    create a function gcd with two param num2,num2
    return gcd of num1,num2 
"""

"""
Q3

create a function is_palindrome with one parameter num
retiurn True if num is palindrom else return False

"""










