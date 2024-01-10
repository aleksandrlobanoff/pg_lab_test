import random


# Найти выражения, результат которых равен целевой сумме
def find_expression(numbers, remaining_sum, current_sum, expression):
    # Если не осталось цифр (чисел) для обработки
    if not numbers:
        # Проверка, что остаточная сумма равна 0
        if remaining_sum == 0:
            # Вычислить результат выражения
            result = eval(expression)
            # Проверка, что результат равен 200
            if result == target_sum:
                # Вывести выражение и результат
                print(f"{expression} = {result}")
        return

    # Обработка цифр (чисел)
    for i in range(1, len(numbers) + 1):
        # Получить текущее число
        num = int(numbers[:i])

        # Пропустить число, если оно равно нулю
        if num == 0:
            continue

        # Оставшиеся числа для обработки
        remaining_numbers = numbers[i:]

        # Если текущее выражение пустое
        if expression == "":
            # Рекурсивно вызвать функцию, передавая оставшиеся числа и текущую сумму
            find_expression(remaining_numbers, remaining_sum - num, current_sum + num, str(num))
        else:
            # Рекурсивно вызвать функцию, передавая оставшиеся числа, текущую сумму и обновленное выражение с "+" для текущего числа
            find_expression(remaining_numbers, remaining_sum - num, current_sum + num, expression + f" + {num}")
            # Рекурсивно вызвать функцию, передавая оставшиеся числа, текущую сумму и обновленное выражение с "-" для текущего числа
            find_expression(remaining_numbers, remaining_sum + num, current_sum - num, expression + f" - {num}")


if __name__ == "__main__":
    # Исходная последовательность цифр (чисел)
    number_sequence = "0123456789"
    # Перемешать последовательность
    shuffled_numbers = "".join(random.sample(number_sequence, len(number_sequence)))

    # Целевая сумма
    target_sum = 200

    # Запуск функции для поиска выражений
    find_expression(shuffled_numbers, target_sum, 0, "")
