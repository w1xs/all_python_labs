input_first_number = input("Введите первое число: ")
input_second_number = input("Введите второе число: ")

if input_first_number[0:1] == "-":
    input_first_number = input_first_number[1:]
if input_second_number[0:1] == "-":
    input_second_number = input_second_number[1:]

if input_first_number.isdigit() and input_second_number.isdigit():
    if len(input_first_number) > len(input_second_number):
        print("В первом числе больше цифр")
    elif len(input_first_number) < len(input_second_number):
        print("Во втором числе больше цифр")
    elif len(input_first_number) == len(input_second_number):
        print("В числах равное количество цифр")
else:
    print("Введены не верные данные")