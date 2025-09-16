"""
Error handling 

1)syntax error
2)run time error (Exceptions)

try
except
finally
raise
assert

# blocks try ,except,finally

try:
    doubtful code 

except:
    handling code 



"""



num1=int(input("enter number1"))#10

num2=int(input("enter number2"))#0


try:
    div_res = num1/num2

    print(div_res)

except Exception as e:

    print(e)


print("send text message to user phone number")

print("send email confirmation")




