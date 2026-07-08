from model.restaurant import Restaurant

restaurant_square = Restaurant('Square', 'Gourmet')
restaurant_square.receive_assessment('Gui', 10)
restaurant_square.receive_assessment('Lais', 8)
restaurant_square.receive_assessment('Emy', 5)

def main():
    Restaurant.restaurants_list()

if __name__ == '__main__':
    main()
