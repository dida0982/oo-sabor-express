import os
class  Restaurant:
    restaurants = []

    def __init__(self,name,category):
        #title() deixa todas as primeiras letras em maiusculas.
        self._name = name.title()
        #upper() deixa todas as primeiras letras em maiusculas.
        self._category = category.upper()
        self._active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self._name} | {self._category}'

    @classmethod
    def restaurants_list(cls):
        print(f'{'Name of restaurant'.ljust(25)} | {'Category'.ljust(25)} | {'Status'}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.active}')

    @property
    def active(self):
        return '✔️' if self._active else '❌'

    def toggle_state(self):
        self._active = not self._active

restaurant_square = Restaurant('Square','Gourmet' )
restaurant_square.toggle_state()
restaurant_pizza = Restaurant('Pizza Express', 'Italiana')

os.system('cls')
Restaurant.restaurants_list()
