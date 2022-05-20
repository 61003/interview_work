'''
Создать два класса. Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре:
название и цену. Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
отвечающую за отображение информации о товаре в одной строке вида (“{название товара} {цена товара}”).
Создать экземпляры родительского класса и дочернего. Распечатать информацию о товаре.
'''


class ItemDiscount:
    def __init__(self, price, name):
        self.price = price
        self.name = name


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.name} {self.price}')


new_report = ItemDiscountReport(4345, 'Keyboard MX Keys').get_parent_data()
