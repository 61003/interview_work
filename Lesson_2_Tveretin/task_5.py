'''
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс
ItemDiscountReport на два класса. Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод
названия товара, а вторая — его цены. Далее реализовать вызов каждой из функции get_info.
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


class ItemDiscountReportName(ItemDiscountReport):

    def get_info(self):
        return self.get_name()


class ItemDiscountReportPrice(ItemDiscountReport):

    def get_info(self):
        return self.get_price()


new_report_price = ItemDiscountReportPrice(4345, 'Keyboard MX Keys', 10)
new_report_name = ItemDiscountReportName(4345, 'Keyboard MX Keys', 10)

new_lst = [new_report_name, new_report_price]
for item in new_lst:
    print(item.get_info())
