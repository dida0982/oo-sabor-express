import os
from model import assessment
from model.assessment import Assessment
class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._assessment =[]
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self._name} | {self._category}'

    @classmethod
    def restaurants_list(cls):
        print(f'{"Name of restaurant".ljust(25)} | {"Category".ljust(25)} | Status')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.active}')

    @property
    def active(self):
        return '✔️' if self._active else '❌'

    def change_status(self):
        self._active = not self._active

    def receive_assessment(self, costomer, notice):
        assessment = Assessment(costomer, notice)
        self._assessment.append(assessment)
