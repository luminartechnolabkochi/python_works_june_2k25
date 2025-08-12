

# create a funtion max_odd_number with one param [num] 
# that will return largest odd number from num

# max_odd_number(473)#
# 7
# 3
# 73
# 47
# 473 


# 2374
# 4 4 chk odd 
# 237
# 7 ch odd


def max_odd_number(number):#nu ber =4371

    while(number!=0):#4371 !=0

        digit = number % 10 # 4371%10=1

        if digit %2!=0:

            print(number)#4371
            
            break
        
        number = number//10

max_odd_number(4371)
