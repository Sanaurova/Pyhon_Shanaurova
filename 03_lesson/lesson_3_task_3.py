from Address import Address
from Mailing import Mailing

# Создаём адреса


from_address = Address("665776", "Братск", "Калужская", "8", "5")
to_address = Address("660125", "Красноярск", "9 Мая", "28", "2")

# Создаём отправление


mailing = Mailing(to_address, from_address, 1420.30, "TRACK123456789")

# Печатаем в требуемом формате


print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
