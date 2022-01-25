

class HotelModel:

    def __init__(self, hotel_id: str, name: str, stars: float, daily_charge: float, city: str) -> None:
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__daily_charge = daily_charge
        self.__city = city

    def json(self):
        return {
            'hotel_id': self.__hotel_id,
            'name': self.__name,
            'stars': float(self.__stars),
            'daily_charge': float(self.__daily_charge),
            'city': self.__city
        }
