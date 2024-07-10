def remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed")
    return dividend % divisor


# Тесты
def test_remainder():
    # Тесты на корректные значения
    assert remainder(10, 3) == 1, "10 % 3 должно быть 1"
    assert remainder(25, 4) == 1, "25 % 4 должно быть 1"
    assert remainder(17, 5) == 2, "17 % 5 должно быть 2"
    assert remainder(0, 1) == 0, "0 % 1 должно быть 0"
    assert remainder(15, 1) == 0, "15 % 1 должно быть 0"
    assert remainder(16, 4) == 0, "16 % 4 должно быть 0"

    # Тесты на отрицательные значения
    assert remainder(-10, 3) == 2, "-10 % 3 должно быть 2"
    assert remainder(10, -3) == -2, "10 % -3 должно быть -2"
    assert remainder(-10, -3) == -1, "-10 % -3 должно быть -1"

    # Тесты на деление на ноль
    try:
        remainder(10, 0)
    except ValueError as e:
        assert str(e) == "Division by zero is not allowed", "Исключение должно быть 'Division by zero is not allowed'"
    else:
        assert False, "Должно было быть вызвано исключение ValueError"

    print("Все тесты пройдены успешно!")


# Запуск тестов
test_remainder()