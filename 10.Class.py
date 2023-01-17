class product:
    items = 'food_items'
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
p1=product("Milk","50","1 kg")
p2=product("Flour","70","100 gram")
print("\nProduct Name : ",p1.name)
print("Product Price : ",p1.price)
print("Product Quantity : ",p1.quantity)
print("\nProduct 2 Details : ")
print("\nProduct Name : ",p2.name)
print("Product Price : ",p2.price)
print("Product Quantity : ",p2.quantity)
print("\nClass Name Accessing Class Variable")
print(product.items)
