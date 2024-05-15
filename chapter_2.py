def hide_card(card_number):
    # Заменяем первые 12 цифр на *
    hidden_card = "*" * 12 + card_number[12:]

    return hidden_card


print(hide_card("1234567890123456"))


##############################################################################


def same_parity(numbers):
    if not numbers:
        return []  # Возвращаем пустой список, если входной список пустой

    first_num_parity = numbers[0] % 2  # Определяем четность первого элемента

    result = []
    for num in numbers:
        if num % 2 == first_num_parity:
            result.append(num)

    return result


print(same_parity([6, 0, 67, -7, 10, -20]))

##############################################################################


def is_valid(string):
    if len(string) not in [4, 5, 6]:
        return False
    if not string.isdigit():
        return False
    if " " in string:
        return False
    return True


print(is_valid("4367"))

##############################################################################


def print_given(*args, **kwargs):
    for arg in args:
        print(f"{arg} {type(arg)}")
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: x[0])
    for key, value in sorted_kwargs:
        print(f"{key} {value} {type(value)}")


print_given(
    [1, 2, 3, 4], ("a", "b", "c", "d"), name="Timur", age=29, city="Moscow"
)

##############################################################################


def convert(data):
    upper = sum(map(str.isupper, data))
    lower = sum(map(str.islower, data))
    if upper > lower:
        return data.upper()
    elif upper < lower:
        return data.lower()
    elif upper == lower:
        return data.lower()
    return data


print(convert("ABCdef"))

##############################################################################


def filter_anagrams(word, anagrams):
    result = []
    for i in anagrams:
        if sorted(i) == sorted(word):
            result.append(i)
    return result


print(filter_anagrams("отсечка", ["сеточка", "стоечка", "тесачок", "чесотка"]))

##############################################################################


def likes(name_list):
    if len(name_list) == 0:
        return "Никто не оценил данную запись"
    elif len(name_list) == 1:
        return f"{name_list[0]} оценил(а) данную запись"
    elif len(name_list) == 2:
        return f"{name_list[0]} и {name_list[1]} оценили данную запись"
    elif len(name_list) == 3:
        return f"{name_list[0]}, {name_list[1]} и {name_list[2]} оценили данную запись"
    else:
        return f"{name_list[0]}, {name_list[1]} и {len(name_list) - 2} других оценили данную запись"


print(likes(["Дима", "Алиса"]))

##############################################################################


def index_of_nearest(num_list, number):
    temp_list = []
    if not num_list:
        return -1
    else:
        for i in num_list:
            temp_list.append(abs(i - number))
        min_num = min(temp_list)
        for j in range(len(temp_list)):
            if temp_list[j] == min_num:
                return j


print(index_of_nearest([9, 5, 3, 2, 11], 4))

##############################################################################
