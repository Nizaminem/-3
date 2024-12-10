# Максимум изсписка
def find_max(list_):
    max_= list_[0]
    for i in list_:
        if i > max_:
            max_=i
    return max_
print(find_max([1, 3, 4, 0, 5, 6, 22, 2]))

# Подсчет четных чисел в списке
def count_even(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter
print(count_even([1, 4, 5, 6, 66, 4, 3, 33, 31, 8]))

#Уникальный список
def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(unique([1, 3, 4, 5, 5, 4, 3, 6, 7]))