from model import assessment
from model.assessment import Assessment
from model.menu import drink
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
    #append = adiciona | self = objeto |
    def add_drink_menu(self):
        self._menu.append(drink)

    def add_plate_menu(self, plate):
        self._menu.append(plate)
