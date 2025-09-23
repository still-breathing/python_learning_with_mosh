# learning about oop from https://www.youtube.com/watch?v=Ej_02ICOIgs

print("**************Learning about OOP**************")


# creation of a class
class Item:
    def __init__(self,name:str,price:float,quamtity=0): # __ magic method also as 0 is already added so no need to define type here
        print("\n__I am in init method__\n")
        print(f"\n{name} costs {price}")
        self.name = name
        self.price = price # attributes find out why auto suggestion gave 0 but tutorial gave self.price = price -> because by default setting price to 0
        self.quantity = quamtity
        self.total_price = 0 # is it needed ??
        # pass
    # def calcuate_total_price(self, x,y):
    #     #return self.price * self.quantity
    #     return x * y
    # need to define another method to get the current quantity of the item
    # def get_current_quantity(self):
    def calculate_total_price(self):
        return self.price * self.quantity # method to calculate total price
        # need to somehow set the quantity if user send purchase  yes then reduce the quantity

    
print("Creating an object of the class Item")
item1 = Item("Phone",13000,7) # creating an object of the class Item

#item1.name = "Phone"
# item1.price = 1000
# item1.quantity = 5
# total_price = item1.calcuate_total_price(item1.price, item1.quantity)
# print(f"Total price of {item1.quantity} {item1.name}s  \n are {total_price}")
# x = item1.calculate_total_price()
print(f"Total price of {item1.quantity} {item1.name}s are {item1.calculate_total_price()}")

item2 = Item("Laptop",150000,1) # creating another object of the class Item
# item2.name = "Laptop"
# item2.price = 2000
# item2.quantity = 3
# y= item2.calculate_total_price()
print(f"Total price of {item2.quantity} {item2.name}s are {item2.calculate_total_price()}")


# print(type(item1), item1)
# print(type(item1.name), item1.name)
# print(item1.price, type(item1.price))
# print(item1.quantity, type(item1.quantity))

# ctrl + k and then ctrl + / -> comment multiple lines