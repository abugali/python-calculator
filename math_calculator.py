
import math  # Подключаем математические функции и создаём список истории вычислений

history = []


# Функции для выполнения математических операций
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Нельзя делить на ноль!")
    return a / b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Нельзя извлечь действительный корень из отрицательного числа!")
    return math.sqrt(a)


def percentage(a, b):
    return a * b / 100


# Запрашиваем число и повторяем ввод, если пользователь допустил ошибку
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Ошибка: введите корректное число!")


# Главное меню калькулятора и обработка действий пользователя
def calculator():
    while True:
        print("\n===== КАЛЬКУЛЯТОР =====")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Квадратный корень")
        print("7. Процент")
        print("8. История вычислений")
        print("9. Очистить историю")
        print("0. Выход")

        choice = input("Выберите действие: ")

        # Завершаем программу, если пользователь выбрал выход
        if choice == "0":
            print("Калькулятор завершён.")
            break

        # Показываем историю вычислений или очищаем её
        if choice == "8":
            if history:
                for item in history:
                    print(item)
            else:
                print("История пуста.")
            continue

        if choice == "9":
            history.clear()
            print("История очищена.")
            continue

        try:
            # Для квадратного корня требуется только одно число
            if choice == "6":
                a = get_number("Введите число: ")
                result = square_root(a)
                operation = f"√{a}"

            # Для остальных математических операций вводим два числа
            elif choice in ("1", "2", "3", "4", "5", "7"):
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")

                # Выбираем операцию на основе введённой команды
                if choice == "1":
                    result = add(a, b)
                    operation = f"{a} + {b}"

                elif choice == "2":
                    result = subtract(a, b)
                    operation = f"{a} - {b}"

                elif choice == "3":
                    result = multiply(a, b)
                    operation = f"{a} * {b}"

                elif choice == "4":
                    result = divide(a, b)
                    operation = f"{a} / {b}"

                elif choice == "5":
                    result = power(a, b)
                    operation = f"{a} ** {b}"

                elif choice == "7":
                    result = percentage(a, b)
                    operation = f"{b}% от {a}"

            else:
                print("Неизвестная команда. Попробуйте ещё раз.")
                continue

            # Проверяем результат и сохраняем вычисление в историю
            if isinstance(result, (int, float)):
                if not math.isfinite(result):
                    raise OverflowError("Результат слишком большой или не является конечным числом!")
                history.append(f"{operation} = {result}")

            print("Результат:", result)

        # Обрабатываем ошибки, чтобы программа не завершалась неожиданно
        except ValueError as error:
            print("Ошибка:", error)

        except ZeroDivisionError as error:
            print("Ошибка:", error)

        except OverflowError as error:
            print("Ошибка:", error)

        except (TypeError, RecursionError) as error:
            print("Ошибка вычисления:", error)


# Запускаем калькулятор
calculator()
