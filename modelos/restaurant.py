import os

class  Restaurant:
    name =''
    category = ''
    active = False

Restaurant_square = Restaurant()
Restaurant_square.name = 'Square'
Restaurant_square.category = 'Gourmet'

Restaurant_pizza = Restaurant()

Restaurant = [Restaurant_square, Restaurant_pizza]

print(vars(Restaurant_square))
os.system('cls')
print(vars(Restaurant_square))
