import re

def find_max_substring(s):
    tokens = re.findall(r'(\d+|[A-Z]+)', s)
    max_len = 0
    current_numbers = []
    current_length = 0
    last_alpha_len = 0

    for token in tokens:
        if token.isdigit():
            num = int(token)

            if not current_numbers:
                # Начало новой последовательности
                current_numbers.append(num)
                current_length = len(token) + last_alpha_len
                last_alpha_len = 0
            else:
                # Проверяем условие четности суммы
                if (current_numbers[-1] + num) % 2 == 0:
                    current_numbers.append(num)
                    current_length += len(token)
                    last_alpha_len = 0
                else:
                    # Сохраняем максимальную длину
                    if len(current_numbers) >= 2:
                        max_len = max(max_len, current_length)

                    # Начинаем новую последовательность с последнего числа
                    if len(current_numbers) > 0:
                        current_numbers = [current_numbers[-1]]
                        current_length = len(str(current_numbers[0])) + last_alpha_len
                        last_alpha_len = 0

                    # Добавляем текущее число
                    current_numbers.append(num)
                    current_length += len(token)
        else:
            # Запоминаем длину буквенного фрагмента
            last_alpha_len += len(token)
            current_length += len(token)

        # Обновляем максимум
        if len(current_numbers) >= 2:
            max_len = max(max_len, current_length)

    # Проверяем последнюю последовательность
    if len(current_numbers) >= 2:
        max_len = max(max_len, current_length)

    return max_len
with open("24_22448.txt") as file:
    data = file.read().strip()

print(find_max_substring(data))

# 171