import random

import requests


def main():
    URL = "http://localhost:8080/orders/create"

    names = ['Iphone', 'Компьютер', 'HP-ноутбук', 'PS5', 'Набор для вышивания', 'Lego', 'Карты', 'CD-диск', 'Дудка',
             'Часы',
             'Кружка для пива']
    places = ['Ваи', 'Отрожка', 'ГЧ', 'Памятник славы', 'Машмет', 'ВГУ', 'ЮЗЫ', 'Динамо', 'Аллые Паруса', '13 rules']

    items = []

    for step in range(0, 5):
        for _ in range(0, random.choice(range(1, 3))):
            items.append(
                {
                    "name": random.choice(names),
                    "count": random.choice(range(1, 10)),
                    "price": random.choice(range(150, 10000)),
                    "weight": random.choice(range(50, 4000))
                }
            )
        data = {
            "deliveryAddress": random.choice(places),
            "arrivalDate": '28.10.2023 18:00',

            "items": items
        }
        print(data)

        r = requests.post(url=URL, json=data)
        print(r.status_code)
        if r.status_code == 200:
            print("Data added successfully")
        else:
            print("Error added data")


if __name__ == "__main__":
    main()
