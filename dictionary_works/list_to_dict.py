

numbers=[2,3,4,5,6]

square_dict={}

for num in numbers:

    # square_dict[num]=num**2
    square_dict.update({num:num**2})

print(square_dict)


