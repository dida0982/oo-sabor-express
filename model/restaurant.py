from model.assessment import Assessment
from model.menu.item_menu import ItemMenu
class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._assessment =[]
        self._menu = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self._name} | {self._category}'

    @classmethod
    def restaurants_list(cls):
        print(f'{"Name of restaurant".ljust(25)} | {"Category".ljust(25)} | {'Assessment'.ljust(25)} | Status')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.average_assessment).ljust(25)} | {restaurant.active}')

    @property
    def active(self):
        return '✔️' if self._active else '❌'

    def change_status(self):
        self._active = not self._active

    def receive_assessment(self, costomer, score):
        if 0 < score <= 5:
            assessment = Assessment(costomer, score)
            self._assessment.append(assessment)

    @property
    def average_assessment(self):
        if not self._assessment:
            return '-'
        sum_of_scores = sum(assessment._score for assessment in self._assessment)
        amount_of_scores = len(self._assessment)
        average = round(sum_of_scores / amount_of_scores, 1)
        return average

    def add_menu(self, item):
        if isinstance(item, ItemMenu):
            self._menu.append(item)

    @property
    def display_menu(self):
        print(f'Menu of resteurant {self._name}\n')
        for i, item in enumerate(self._menu, start=1):
            message = f'{i}. Name:{item._name} | Price: R${item._price}'
            print(message)
