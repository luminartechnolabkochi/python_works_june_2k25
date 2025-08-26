
# given an array of numbers  find the closest number to zero

arr = [-2,-3,-4,-1,1,2,3,4,5]

closest_number = arr[0]

for num in arr:

    if abs(num) < abs(closest_number):

        closest_number = num

if closest_number < 0 and abs(closest_number) in arr:

    closest_number = abs(closest_number)

print(closest_number)   


