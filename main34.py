# First class
import datetime


class Hotels:

    booking_raiting = 'Recommended'

    def __init__(self, name, star, season):
        self.name = name
        self.star = star
        self.season = season

    def get_info(self):
        return f'Hotel name: {self.name}, Star rating: {self.star}, Season: {self.season}'

    @staticmethod
    def season(date):
        if date.month in range(4, 11):
            return 'summer'
        elif date.month in range(11, 13) or date.month in range(1, 4):
            return 'winter'

    def booking_possibility(self):
        season = Hotels.season(date)
        if season == 'winter' and self.season == 'winter' or self.season == 'fullseason':
            return f'Hotel {self.name}, {self.star}, {date}'
        elif season == 'summer' and self.season == 'summer' or self.season == 'fullseason':
            return f'Hotel {self.name}, {self.star}, {date}'
        else:
            return 'Not available for booking'


hotel1 = Hotels('Venera', '5*', 'fullseason')
hotel2 = Hotels('Apolon', '5*', 'summer')
hotel3 = Hotels('Zevs', '4*', 'fullseason')
hotel4 = Hotels('Artemida', '3*', 'winter')
hotel5 = Hotels('Gera', '4*', 'fullseason')

print(hotel1.get_info())

print(hotel1.booking_raiting)

date = datetime.date(2023, 12, 1)
print(Hotels.season(date))

print(hotel1.booking_possibility())


# Second class
class Rooms:

    SNGL = 1
    DBL = 2
    TRPL = 3

    def __init__(self, type_n, view):
        self.type_n = type_n
        self.view = view

    @classmethod
    def accomodation(cls, pax):
        if pax == Rooms.SNGL:
            return "SNGL or DBL"
        elif pax == Rooms.DBL:
            return "DBL"
        elif pax == Rooms.TRPL:
            return "TRPL"
        else:
            return 'Choose another accommodation'

    def cange_vip(self, date):
        if date.year >= 2024:
            self.type_n = 'Luxury'
            return f"VIP was changed to Luxury"
        else:
            return f"{self.type_n} room"

    def rooms_in_hotel(self):
        return f'Room\'s type: {self.type_n}, View from the window: {self.view}'


room1 = Rooms('Standard', 'sea view')
room2 = Rooms('Standard', 'seaside view')
room3 = Rooms('Standard', 'garden view')
room4 = Rooms('Economy', 'pool view')
room5 = Rooms('Family', 'sea view')
room6 = Rooms('Family', 'garden view')
room7 = Rooms('VIP', 'sea view')

print(Rooms.accomodation(5))

print(room7.cange_vip(datetime.date(2025, 1, 1)))

print(room1.rooms_in_hotel())
