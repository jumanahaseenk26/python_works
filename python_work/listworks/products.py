items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":5},
    {"id":5,"name":"potatto","price":45,"avl_qty":70},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":50,"avl_qty":50},]

# print total number of products
#print(len(items),"products")
# print all product names
#list comprehention
All_product_names=[i.get("name") for i in items]
print(All_product_names)
#for i in items:
 #   print(i.get("name"))
# print all in stock product names   
in_stock=[i.get("name") for i in items if i.get("avl_qty")>0]
print("stocks:",in_stock)
#for i in items:
 #   if i.get("avl_qty")>0:
  #      print(i.get("name"))
# print product names avaialble under rs 50
price_filter=[i.get("name") for i in items if i.get("price")>50]
print("price filter is: ",price_filter)
#for i in items:
 #   if i.get("price")<50:
  #      print(i.get("name"))
# print all product names avilable in ranage of 20 to 100
range_filter=[i.get("name") for i in items if i.get("price") in range(20,100)]
print("range filter: ",range_filter)
#for i in items:
#    if i.get("price") in range(20,100):
 #       print(i.get("name"))
#costly product in the list
#costly_product=max([i.get("price") for i in items])
#print(costly_product)

print("costly product is: ")
costly_product=max(items,key=lambda i:i.get("price"))
print(costly_product)

print("sorted items: ")
product_sort=sorted(items,reverse=True,key=lambda i:i.get("avl_qty"))
print(product_sort)
