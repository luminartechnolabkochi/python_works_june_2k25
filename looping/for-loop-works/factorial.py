

from builtins import int
from builtins import print


num = int(input("enter number"))#4

fact = 1

for i in range(1,num+1):

    fact = fact * i

print(fact)