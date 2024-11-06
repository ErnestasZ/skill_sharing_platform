def check_int_input(result):
    while not result.isdigit():
        result = input("Neteisinga ivestis, ivesk skaičiu: ")
    return int(result)
