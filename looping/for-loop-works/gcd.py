

# GCD | HCF of two numbers
# greatest common divisor 


num1=int(input("enter num1"))#8

num2=int(input("enter number2"))#72

gcd = 1

limit = min(num1,num2)

for i in range(1,limit+1):

    if num1 % i ==0 and num2 % i==0:

        gcd = i

print(gcd)