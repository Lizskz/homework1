immutable_var = ('строка', 12, True, [21, 22,23])
print(immutable_var)
# immutable_var[1] = 3
# print(immutable_var)
# кортеж не поддерживает обращение по элементам
mutable_list = ['строка', 13, False]
mutable_list[1] = 14
print(mutable_list)
