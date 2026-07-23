class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address  # объект Address (куда)
        self.from_address = from_address  # объект Address (откуда)
        self.cost = cost  # стоимость (число)
        self.track = track  # трек-номер (строка)
