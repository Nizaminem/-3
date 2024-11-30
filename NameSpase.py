calls = 0

def count_calls():
    global calls
    calls+=1

def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return length, upper_case, lower_case

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower
    return string_lower in (a.lower() for a in list_to_search)

result1 = string_info("Привет МИР")
result2 = is_contains("mIR", ["привет", "мир","москва"])

print("Результат функции string_info: ", result1)
print("Результат функции is_comstains:", result2)

print("Количество вызовов функций: ", calls)