def get_multiplied_digits(number):  # 1
    number = int(number)            # отсекаем нули в начале number
    str_number = str(number)        # 2
    first = int(str_number[0])      # 3

    while str_number.endswith('0'): # отсекаем нули в конце number
            str_number = str_number[:len(str_number)-1]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

num = input('Введите целое число: ')
print(f'Произведение цифр числа {num} :', get_multiplied_digits(num))