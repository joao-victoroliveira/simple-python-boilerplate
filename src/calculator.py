class Calculator:
    def __init__(self, hotels = []):
        self.hotels = hotels

    def getCheappest(self, customerType, period):
        cheapestHotel = None
        if self.hotels == []:
            return ''        
        cheapestHotel = self.hotels[0]
        for hotel in self.hotels:
            current_cheapest = cheapestHotel.getPriceForPeriod(customerType, period)
            hotel_price = hotel.getPriceForPeriod(customerType, period)
            if current_cheapest > hotel_price or (current_cheapest == hotel_price and cheapestHotel.rating < hotel.rating):
                cheapestHotel = hotel
        return cheapestHotel.name
