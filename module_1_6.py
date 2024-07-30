my_dict = {'Nina': 1998, 'Anna': 1985, 'Dima': 2000, 'Ivan': 1996}
print(my_dict)
print(my_dict.get('Nina'))
print(my_dict.get('Liza'))
my_dict.update({'Denis': 2002,
                'Svetlana': 1990})
my_dict.pop('Dima')
print(my_dict.get('Denis'))
print(my_dict)


my_set = {123, 17, 'Liza', 17, True, 0.009, 78, 78}
print(my_set)
my_set.add(89)
my_set.add('www')
my_set.discard(123)
print(my_set)