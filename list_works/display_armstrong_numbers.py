

def is_armstrong(number):

    digit_count = len(str(number))

    original = number

    sum =0

    while(number!=0):

        digit = number % 10

        expo = digit ** digit_count

        sum +=expo

        number=number //10
    
    return sum==original

numbers=[151,152,153,1634,8891,345,678]

for num in numbers:

    if is_armstrong(num):

        print(num)



