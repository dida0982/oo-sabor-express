import os

class  Restaurant:
    def __init__(self,name,category):
        self.name = name
        self.category = category
        self.active = False

restaurant_square = Restaurant('Square','Gourmet' )
restaurant_pizza = Restaurant('Pizza Express', 'Italiana')

Restaurant = [restaurant_square, restaurant_pizza]

os.system('cls')
print(vars(restaurant_square))
print(vars(restaurant_pizza))
