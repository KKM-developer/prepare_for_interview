class ItemDiscount:

    def __init__(self, name, price):
        self._name = name

        self._price = price


class ItemDiscountRepor(ItemDiscount):

    def __init__(self, name, price, discont):
        super().__init__(name, price)

        self.discont = discont / 100

    def __str__(self):
        return f'Цена со скидкой {self._price - self._price * self.discont}'

    def get_parent_data(self):
        return f'{self._name}\n{self._price} руб/кг'


green_apple = ItemDiscount(name='Granny Smith', price=50)

print(green_apple._name)

cucumber = ItemDiscountRepor(name='cucumber', price=100, discont=10)

print(cucumber.get_parent_data())

cucumber._name = 'carrot'

cucumber._price = 100

print(cucumber.get_parent_data())

print(cucumber)