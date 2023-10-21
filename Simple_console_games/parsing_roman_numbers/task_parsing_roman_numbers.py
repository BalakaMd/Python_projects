numbers_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def parsing_numbers(numbers):
    value = 0
    for n in numbers:
        if n not in ['I', 'V', 'X', "L", "C", "D", "M"]:
            print("Stop")
            return
    for c, v in enumerate(numbers):
        if c + 1 < len(numbers) and numbers[c] < numbers[c + 1]:
            value -= numbers_dict[v]
        else:
            value += numbers_dict[v]
    return value


print(parsing_numbers("XIV"))
