

lst =[1,2,3,4,5,7]
#     0 1 2 3
#     i j
#     1 2  3 4

for i in range(0,len(lst)-1):

    j = i+1

    difference = lst[j] - lst[i]

    if difference!=1:

        print(lst[i]+1,"is missing")

        break








