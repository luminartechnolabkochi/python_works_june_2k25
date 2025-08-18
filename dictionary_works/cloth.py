

product = {"code":"sku1234","title":"linen shirt","brand":"peterengland","price":17000,"offer":200}


# add offer as 1000 if offer not exist else update offer as current offer + 500



if "offer" in product:

    product["offer"]+=500# update

else:

    product["offer"] = 1000 #add

print(product)



