from unittest import TestCase
from context import src
from src.hotel import Hotel


class HotelTest(TestCase):
    
    def test_return_0_when_get_price_for_period(self):
        lakeWood = Hotel('LakeWood', 8, 10, 20, 25, 1)
        hotelPrice = lakeWood.getPriceForPeriod('regular',['SUN','MON','TUE'])
        self.assertEqual(hotelPrice,26)

    def test_if_day_is_a_weekend_day(self):
        day = 'FRI'
        lakeWood = Hotel('LakeWood', 8, 10, 20, 25, 1)
        self.assertEqual(lakeWood.isWeekend(day), False)

