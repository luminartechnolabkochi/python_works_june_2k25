



num1=int(input("enter number1"))#10

num2=int(input("enter number2"))#0


try:
    div_res = num1/num2

    print(div_res)

except Exception as e:

    num2=int(input("enter num2 "))

    div_res = num1/num2

    print(div_res)

finally:

    print("send text message to user phone number")

    print("send email confirmation")

# ZeroDivionError
# IndexOutrange
# keyerror
# valueerror
# fnf

# raise

num1=int("ten")

