def is_year_leap(year):

    # Проверяет, является ли год високосным.
    # Возвращает True, если год делится на 4 без остатка, иначе False.

    return year % 4 == 0

# Выберите любой год для проверки


year = 2024

result = is_year_leap(year)
print(f"год {year}: {result}")
