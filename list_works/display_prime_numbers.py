



def is_prime(number):

    is_prime = True

    for i in range(2,number):

        if number%i==0:

            is_prime = False

            break
    
    return is_prime

numbers =[11,12,13,33,131,343,12321,1234]

for num in numbers:

    if is_prime(num):

        print(num)