from model.menu.item_menu import ItemMenu

class Plate(ItemMenu):
    def __init__(self, name, price, description) :
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        return self.name
