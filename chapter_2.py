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


print_given([1, 2, 3, 4], ("a", "b", "c", "d"), name="Timur", age=29, city="Moscow")


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
        return (
            f"{name_list[0]}, {name_list[1]} и {len(name_list) - 2} других оценили данную запись"
        )


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
words = [
    "Россия",
    "Австрия",
    "Австралия",
    "РумыниЯ",
    "Украина",
    "КИТай",
    "УЗБЕКИСТАН",
]


def spell(*args):
    lowercase_args = [i.lower() for i in args]
    temp_arr = []
    result = {}
    for i in lowercase_args:
        first_letter = i[0]
        for j in lowercase_args:
            if first_letter == j[0]:
                temp_arr.append(j)
        longest_word = max(temp_arr, key=len)
        longest_word_first_letter = longest_word[0]
        longest_word_len = len(longest_word)
        result[longest_word_first_letter] = longest_word_len
        temp_arr = []
    return result


print(spell(*words))


##############################################################################


def best_route(d1, d2, d3):
    return min(d1 + d2 + d3, 2 * (d1 + d2), 2 * (d2 + d3), 2 * (d1 + d3))


print(best_route(10, 10, 45))

##############################################################################

ru_str = "АаВСсЕеНКМОоРрТХху"
en_str = "AaBCcEeHKMOoPpTXxy"


def check_lang(l1, l2, l3):
    letter_list = [l1, l2, l3]
    ru_common_elements = list(filter(lambda i: i in letter_list, list(ru_str)))
    en_common_elements = list(filter(lambda i: i in letter_list, list(en_str)))
    if len(ru_common_elements) >= 1 and len(en_common_elements) >= 1:
        result = "mix"
    elif len(ru_common_elements) >= 1 and len(en_common_elements) == 0:
        result = "ru"
    else:
        result = "en"
    return result


print(check_lang("а", "а", "а"))

##############################################################################

data = "9 3 6 5 8"
data = list(map(int, data.split()))
x, y, a, b = data[1], data[2], data[3], data[4]
arr = list(range(1, data[0] + 1))
arr[x - 1 : y] = reversed(arr[x - 1 : y])
arr[a - 1 : b] = reversed(arr[a - 1 : b])

result = " ".join(str(num) for num in arr)

print(result)

##############################################################################

arr = [3, 1, 3, 2, 3, 11, 4, 3, 5, 3, 6, 3, 7, 3, 8, 3, 9, 3, 10, 3, 11, 3, 3, 12, 13, 1]
duplicate_values = sorted(set(x for x in arr if arr.count(x) > 1))
result = " ".join(map(str, duplicate_values))
print(result)
