# from ipaddress import summarize_address_range
#
#
# def calculate_structure_sum(data_structure):
#     summa = 0
#     if isinstance(data_structure, dict):
#         for key, value in data_structure.items():
#             summa += calculate_structure_sum(key)
#             summa += calculate_structure_sum(value)
#     elif isinstance(data_structure, (list, tuple, set)):
#         for item in data_structure:
#             summa += calculate_structure_sum(item)
#     elif isinstance(data_structure, (int, float)):
#         summa += data_structure
#     elif isinstance(data_structure, str):
#         summa += len(data_structure)
#     return summa


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calc(data):
    summa = 0

    for elem in data:
        if isinstance(elem, (int, float)):
            summa += elem
        elif isinstance(elem, str):
            summa +=len(elem)
        elif isinstance(elem, (list, tuple, set)):
            summa += calc(elem)
        elif isinstance(elem, dict):
            summa += calc(elem.items())
    return summa

print(calc(data_structure))