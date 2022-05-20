'''
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента
в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса (метод __init__,
в который должна передаваться переменная — скидка), и перегрузку метода __str__ дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
'''


class ItemDiscount:
    def __init__(self, price, name):
        self.__price = price
        self.__name = name

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

    def set_price(self, price):
        self.__price = price

    def set_name(self, name):
        self.__name = name


class ItemDiscountReport(ItemDiscount):
    def __init__(self, price, name, discount):
        self.set_price(price)
        self.set_name(name)
        self.discount = discount

    def __str__(self):
        return str(self.get_price() - self.get_price() / 100 * self.discount)

    def get_parent_data(self):
        print(f'{self.get_name()} {self.get_price()}')


new_report = ItemDiscountReport(4345, 'Keyboard MX Keys', 10)
new_report.get_parent_data()
print(new_report)
