input_x_coord = input("Введите х координату вектора: ")
input_y_coord = input("Введите y координату вектора: ")
input_z_coord = input("Введите z координату вектора: ")

if input_x_coord.isdigit() and input_y_coord.isdigit() and input_z_coord.isdigit():
    vector_length = (int(input_x_coord)**2 + int(input_y_coord)**2 + int(input_z_coord)**2)**0.5
    print(f"Длина заданного вектора: {vector_length}")
else:
    print("Введены неверные данные")
