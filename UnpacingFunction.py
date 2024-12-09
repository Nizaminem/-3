def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = (3, 'ZZ', True)
values_dict = {'a' : 8, 'b' : 'AA', 'c' : True}

values_list_2 = (1.33, 'ЯтакДумаю!')

# print_params(a = 3, c = 'dadada')
# print_params()
# print_params(b = 25)
# print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2,42)
