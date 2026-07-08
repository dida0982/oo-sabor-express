from model.restaurant import Restaurant

restaurant_square = Restaurant('Square', 'Gourmet')
restaurant_mexicano = Restaurant('Mexican Food', 'Mexicana')
restaurant_japones = Restaurant('Japa', 'Japonesa')

restaurant_mexicano.change_status()

def main():
    Restaurant.restaurants_list()

if __name__ == '__main__':
    main()
