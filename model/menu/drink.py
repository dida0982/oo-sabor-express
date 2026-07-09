from model.menu.item_menu import ItemMenu
#heritage
class Drink(ItemMenu):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
