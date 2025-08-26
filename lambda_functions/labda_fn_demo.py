
# lambda function

# def function_name(p1,p1):

#     function defnition

#     return value

# short one line function without name : lambda function (anonymous=> without name)

# syntax

# lambda p1,p2,,pn:expression

cube=lambda n:n**3

print(cube(4))

sub=lambda n1,n2 :n1-n2

print(sub(10,20))


# last_digit_max(125,872)

last_digit_max=lambda n1,n2:n1 if n1%10 > n2%10 else n2 

print(last_digit_max(127,872))

