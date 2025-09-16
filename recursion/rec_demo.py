


# iterative approach
# 5 to 1  count
# for i in range(5,0,-1):

#     print(i)


# recursive approach


"""
function call itself is called recursion

def function_name(parameter):

    base condition

    function_name(parameter)

"""



def count(n):
    if n==0:
        return
    print(n)

    return count(n-1)

count(5)

