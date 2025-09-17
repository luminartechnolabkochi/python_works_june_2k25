


def is_palindrome(word):

    flag=True

    if word!=word[::-1]:

        flag=False       


    return flag



assert is_palindrome("madam")==True,"test case 1 failed expecting True returned False"

assert is_palindrome("man")==False,"test case 2 failed expecting False returned True"

print("test case running completed")

