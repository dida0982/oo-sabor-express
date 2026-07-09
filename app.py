from model.menu import drink
from model.menu import plate
from model.restaurant import Restaurant
from model.menu.drink import Drink
from model.menu.plate import Plate
from model.menu.item_menu import ItemMenu

restaurant_square = Restaurant('Square', 'Gourmet')
drink_juice = Drink('Watermelon Juice', 5.0, 'big')
plate_bread = Plate('Bread', 2.0, 'small')

def main():
    print(drink_juice)
    print(plate_bread)

if __name__ == '__main__':
    main()
