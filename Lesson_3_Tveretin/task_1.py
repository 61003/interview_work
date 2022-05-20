'''
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться путь и имя файла с расширением.
В функции необходимо реализовать поиск имени файла (с расширением), а затем «выделение» имени файла
(без расширения). Расширений может быть несколько (например testfile.tar.gz).
'''


def get_file_name(path):
    ln = len(path)
    for key, val in enumerate(reversed(path)):
        if val == '.':
            point_ind = ln - key - 1
        if val == '/':
            slash_ind = ln - key
            break
    return path[slash_ind:point_ind]


print(get_file_name('C:/Program Files/7-Zip/readme.txt'))
