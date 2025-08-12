



# step1:set sum as 0
# step2: last_digit 
# step3:add lst_digit with sum
# step4 : floor 

number = 174

sum = 0

while (number !=0):# 174 != 0  17!=0 1!=0 0!=0

    digit = number % 10# 174%10=4 7 1

    sum += digit # sum =0+ 4+7=11+1=12

    number = number // 10 # 174//10=  17//10=1 1//10=0

print(sum)





