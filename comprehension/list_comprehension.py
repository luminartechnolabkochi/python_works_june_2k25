
# comprehension
# easy way for creating list,set,dictionary from an iterable
# syntax
# [expression iteration condition]


arr =[3,4,5,6,7]

# squares_list
# cubes_list

sqaures_list = [num**2 for num in arr ]

print(sqaures_list)

cubes_list = [num**3 for num in arr]

print(cubes_list)

even_numbers =[num for num in arr if num%2==0]

print(even_numbers)

odd_numbers = [num for num in arr if num%2!=0]

print(odd_numbers)

num_gt_five = [num for num in arr if num>5]

print(num_gt_five)