
"""
shallow copy(copies top level objects ,share reference of nesetd object)
deep copy(copies both top level object and nesetd object)

"""


from copy import copy,deepcopy


meghana_fvt_foods=[
    ["meals","sambar"],
    ["biriyani","lime"],
    ["burger","cold-coffe"]

]


nandana_fvt_food=deepcopy(meghana_fvt_foods) # deep copy
# nandana_fvt_food=copy(meghana_fvt_foods) # shallow copy


nandana_fvt_food[0][0]="dosa"

print(meghana_fvt_foods)

print(nandana_fvt_food)


sumof_digit()