
food_items=[
    ["tea","veg",12],
    ["coffe","veg",20],
    ["dosa","veg",60],
    ["gheeroast","veg",80],
    ["masalaroast","veg",120],
    ["eggfriedrice","non-veg",160],
    ["vegfriedrice","veg",120]
]


all_item_names= [it[0] for it in food_items]

print(all_item_names)


# display veg item names

veg_item_names =[it[0] for it in food_items if it[1]=="veg"]


print(veg_item_names)

# items available under rs 100


price_filter = [it[0] for it in food_items if it[2]<100]

print(price_filter)




bikes=[
    ["passion-pro","hero",89000,"petrol",125],
    ["passion-plus","hero",89000,"petrol",125],
    ["activa","honda",120000,"petrol",125],
    ["xpulse","hero",139000,"petrol",150],
    ["hunter","re",200000,"petrol",350],
    ["metor","re",430000,"petrol",350],
    ["triumph-speed-400x","triumph",300000,"petrol",400],
]

# lst > lst

# define a functin wich receives 1 parameter that is list return list[2]


def get_price(lst):

    return lst[2]

costly_bike = max(bikes,key=get_price)

print("costly bike",costly_bike)

