def s_block(input_data):
    # Таблиця констант для S-блоку
    constants = [0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]

    # Розбиваємо вхідні дані на дві тетради
    t1 = (input_data >> 4) & 0xF
    t2 = input_data & 0xF

    # Застосовуємо перетворення за таблицею констант
    t1 = constants[t1 % len(constants)]
    t2 = constants[t2 % len(constants)]

    # Об'єднуємо тетради та повертаємо результат
    result = (t1 << 4) | t2
    return result

def p_block(input_data):
    # Алгоритм P-блоку з реверсуванням бітів
    output_data = 0
    for i in range(8):
        bit = (input_data >> i) & 1
        output_data |= (bit << (7 - i))

    return output_data

def s_block_inverse(input_data):
    # Обернена таблиця констант для S-блоку
    constants_inverse = [0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1]

    # Розбиваємо вхідні дані на дві тетради
    t1 = (input_data >> 4) & 0xF
    t2 = input_data & 0xF

    # Застосовуємо обернене перетворення за таблицею констант
    t1 = constants_inverse[t1 % len(constants_inverse)]
    t2 = constants_inverse[t2 % len(constants_inverse)]

    # Об'єднуємо тетради та повертаємо результат
    result = (t1 << 4) | t2
    return result


# Приклад використання S-блоку та P-блоку
input_data = 0b11011010
s_box_result = s_block(input_data)
p_block_result = p_block(s_box_result)

# Вивід результатів
print(f'Input:  {bin(input_data)}')
print(f'S-Box:  {bin(s_box_result)}')
print(f'P-Block: {bin(p_block_result)}')

# Зворотнє перетворення
s_box_inverse_result = s_block_inverse(input_data)
print(f'S-Box Inverse: {bin(s_box_inverse_result)}')