
# 1
# 1 2
# 1 2  3
# 1 2  3  4
# 1 2  3  4  5  


# for row in range(1,6):

#     for col in range(1,row+1):

#         print(col,end="\t")
    
#     print()

# 1 2 3 4 5 (5)
# 1 2 3 4(4)
# 1 2 3(3)
# 1 2 (2)
# 1(1)


for row in range(1,6):

    for col in range(1,7-row):

        print(col,end="\t")
    
    print()
