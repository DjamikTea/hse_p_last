def divide(a: float, b: float) -> float:
    """
    Делит число a на b

    :param a: Делимое
    :param b: Делитель
    :return: Результат деления
    :raises ValueError: Если делитель равен нулю
    """
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a / b


def factorial(n: int) -> int:
    """
    Вычисляет факториал числа n

    :param n: N число
    :return: Факториал числа n
    :raises ValueError: Если n отрицательно
    """
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def read_integer_from_string(s: str) -> int:
    """
    Преобразует строку s в целое число

    :param s: Строка
    :return: Целое число, полученное из строки s
    :raises ValueError: Если строку s нельзя преобразовать в целое число
    """
    return int(s)