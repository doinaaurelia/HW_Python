# # 3 Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением. 
# # Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
# def to_dict(lst):
#     new_dict = {}
#     for elem in lst:
#         new_dict[elem] = elem
#     return new_dict

# lst = ["1", "two", "3", "four", "5"]
# print(to_dict(lst))

# # 4. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs),
# # которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict,
# #  состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

# my_dict = {"first_one": "we can do it"}

# def biggest_dict(**kwargs):
#     global my_dict
#     for key in kwargs:
#         my_dict[key] = kwargs[key]
#     return my_dict

# biggest_dict(one=1, two=2, three=3, four = 4)
# biggest_dict(five=5)
# print(biggest_dict(six=6, seven=7, eight=8))

# # 5. Дана строка в виде случайной последовательности чисел от 0 до 9.
# # Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# #  а в качестве значений – количество этих чисел в имеющейся последовательности.
# #  Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# #  Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

# sequence = "123451232233"
# def count_it(sequence):
#     my_dict = {int(elem): sequence.count(elem) for elem in sequence}
#     sorted_tuple = sorted(my_dict.items(), key=lambda item: item[1],reverse=True)
#     sorted_dict = {key: value for key, value in sorted_tuple}
#     i = 0
#     res_dict = {}
#     for key in sorted_dict:
#         res_dict[key] = sorted_dict[key]
#         i = i + 1
#         if i == 3:
#             break
#     return res_dict

# print(count_it(sequence))


