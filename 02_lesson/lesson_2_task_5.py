def month_to_season(month):
    
    # Принимает номер месяца (1-12) и возвращает название сезона.
    # Если номер месяца некорректен, возвращает сообщение об ошибке.
    
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Неверный номер месяца"

# Примеры вызова функции с разными месяцами
print(month_to_season(5))   # Весна
print(month_to_season(7))   # Лето
print(month_to_season(9))  # Осень
print(month_to_season(13))  # Неверный номер месяца