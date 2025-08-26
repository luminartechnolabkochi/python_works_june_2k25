# class dict:

#     def get(key) 
#     def pop(key)
#     def keys()
#     def values()
#     def items()
#     def update()




fruits = {"a":"apple","b":"banana","c":"cherry","d":"dragon-fruit"}




print(fruits["ab"])#error stop


print(fruits.get("ab"))#none





for k,v in fruits.items():

    print(k,v)

fruits.update(o="orange")

fruits.update(e="egg-fruit")

print(fruits)

# for v in fruits.values():

#     print(v)

# for k in fruits.keys():

#     print(k)




# popped_value=fruits.pop("d")

# print(fruits)



# # print(fruits["ba"]) #error stop
# print(fruits.get("ba")) #recommonded method for fetching value usig key


# print("tear down")



# print(fruits.get("b")) # return value for key 

