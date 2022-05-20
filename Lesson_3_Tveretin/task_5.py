'''
Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть
строковых значений (выбирается случайно) заменить на значения типа 345example
(в обратном порядке, число и строка). Реализовать функцию поиска определенных подстрок в файле
по следующим условиям: вывод первого вхождения, вывод всех вхождений. Реализовать функцию
замену всех найденных подстрок на новое значение и вывод измененных строк.
'''
from random import randint


def make_file(path):
    try:
        with open(path, mode='x') as file:
            list_1 = [i for i in range(1, 15)]
            list_2 = [chr(i) for i in range(100, 120)]
            for l1, l2 in zip(list_1, list_2):
                rand = randint(0, 1)
                print(rand)
                if rand == 0:
                    file.write(f'{l1}{l2}\n')
                else:
                    file.write(f'{l2}{l1}\n')
    except Exception as err:
        print(err)


def open_file(path):
    with open(path, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())


def find_in_file(path, find_str, first_input=True):
    with open(path, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(find_str) > -1:
                print(line.strip())
                if first_input:
                    break


def replace_in_file(path, find_str, new_str):
    new_lines = []
    with open(path, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(find_str) > -1:
                new_line = line.replace(find_str, new_str)
                new_lines.append(new_line)
            else:
                new_lines.append(line)
    with open(path, mode='w') as file:
        for line in new_lines:
            file.write(line)


file = 'test.txt'
my_file = make_file(file)
open_file(file)
find_in_file(file, '1', first_input=True)
replace_in_file(file, '1', '999')
