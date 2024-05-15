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
    str_lenth = len(data)
    if (
        len(list(filter(lambda x: x.isupper() and not x.isdigit(), data)))
        > str_lenth / 2
    ):
        return data.upper()
    elif (
        len(list(filter(lambda x: x.lower() and not x.isdigit(), data)))
        > str_lenth / 2
    ):
        return data.lower()


print(convert("PI31415!"))
