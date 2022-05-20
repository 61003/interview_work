'''
Реализовать возможность переустановки значения цены товара в родительском классе.
Проверить, распечатать информацию о товаре.
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
    def get_parent_data(self):
        print(f'{self.get_name()} {self.get_price()}')


new_report = ItemDiscountReport(4345, 'Keyboard MX Keys')
new_report.get_parent_data()
new_report.set_name('Mouse MX')
new_report.set_price(7842)
new_report.get_parent_data()
