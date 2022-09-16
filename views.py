import json
FILE = 'db.json'
class CreateMixin:
    @property
    def create(self):
        with open(FILE, 'r') as file:
            try:
                data = json.load(file)
                id = data[-1]['id'] + 1
            except:
                data = []
                id = 1
        with open(FILE, 'w') as file:
            data.append({'id': id, 'brand': self.brand, 'model': self.model, 'year': self.year, 'engine': self.engine, 'color': self.color, 'body_type': self.body_type, 'mileage': self.mileage, 'price': self.price})
            json.dump(data, file)
            print('Автомобиль успешно сохранён на сайт!')
class ListingMixin:
    @property
    def listing(self):
        with open(FILE, 'r') as file:
            data = json.load(file)
            print(data)
class RetriveMixin:
    def retrive(self, id):
        with open(FILE, 'r') as file:
            data = json.load(file)
            is_car_in_db = list(filter(lambda x: x['id'] == id, data))
            if is_car_in_db:
                print(is_car_in_db)
            else:
                print('Автомобиль не найден!')
class UpdateMixin:
    def update(self, id):
        with open(FILE, 'r') as file:
            data = json.load(file)
            is_car_in_db = list(filter(lambda x: x['id'] == id, data))
            if not is_car_in_db:
                raise ValueError('Нет такого автомобиля!')
            else:
                data[is_car_in_db]['brand'] = input('Введите новое название бренда: ')
                data[is_car_in_db]['model'] = input('Введите новое название модели: ')
                data[is_car_in_db]['year'] = input('Введите год выпуска: ')
                data[is_car_in_db]['color'] = input('Введите новый цвет: ')
                data[is_car_in_db]['price'] = input('Введите новую ценну: ')
                data[is_car_in_db]['engine'] = input('Введите новый объём двигателя: ')
        with open(FILE, 'w') as file:
            json.dump(data, file)

class DeleteMixin:
    def delete(self):
        with open(FILE, 'r') as file:
            data = json.load(file)
            inp = input('Введите айди продукта которую хотите удалить: ')
            is_product = any([x['id'] == inp for x in data])
            if is_product:
                data.pop(data[is_product])
        with open(FILE, 'w') as file:
            json.dump(data, file)
