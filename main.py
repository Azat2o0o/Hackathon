from views import CreateMixin, ListingMixin, RetriveMixin, UpdateMixin, DeleteMixin
class Cars(CreateMixin, ListingMixin, RetriveMixin, UpdateMixin, DeleteMixin):
    def __init__(self, brand=str, model=str, year=int, engine=int or float, color=str, body_type=str, mileage=int, price=int):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = round(engine, 1)
        self.color = color
        self.body_type = body_type
        self.mileage = mileage
        self.price = price

car1 = Cars('Mercedes', 'S class', 2020, 6.0, 'black', 'Седан', 0, 100000)
car2 = Cars('Toyota', 'camry', 2022, 3.0, 'black', 'Седан', 0, 25000)
# car1.create
# car2.create
# car2.listing
# car2.retrive(2)
# car2.update(2)   --- Не работает!!!
# car2.delete()    --- Тоже не работает!!!