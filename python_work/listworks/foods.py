foods=[{"id":1,"name":"ghee-roast","price":70,"category":"veg"},
       {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
       {"id":3,"name":"cb","price":170,"category":"non-veg"},
       {"id":4,"name":"bb","price":190,"category":"non-veg"},
       {"id":5,"name":"fried-rice","price":140,"category":"veg"},
       {"id":6,"name":"chicken-friedrice","price":670,"category":"non-veg"},
       {"id":7,"name":"nan","price":70,"category":"veg"},
       {"id":8,"name":"alfham","price":370,"category":"non-veg"},]

# total number of items
print(len(foods),"products")
# print name whose category = veg
veg_items=[i.get("name") for i in foods if i.get("category")=="veg"]
print("veg items are: ",veg_items)
# food names available under rs 100
price_filter=[i.get("name") for i in foods if i.get("price")<100]
print("food under rs 100 are: ",price_filter)
# costly item
print("costly product is: ")
costly_product=max(foods,key=lambda i:i.get("price"))
print(costly_product)
# costly non-veg food
print("costly non veg is: ")
non_veg_foods=[f for f in foods if f.get("category")=="non-veg"]
costly_nonveg=max(foods,key=lambda f:f.get("price"))
#costly_non_veg=max(foods,key=lambda i:i.get("category")=="non-veg" and i.get("price"))
print(costly_nonveg)

categories={f.get("category") for f in foods}
print("categories are: ",categories)