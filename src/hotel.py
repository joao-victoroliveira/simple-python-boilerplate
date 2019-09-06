class Hotel:
    def __init__(self, name, regularPriceWeek, regularPriceWeekend, rewardPriceWeek, rewardPriceWeekend, rating):
        self.name = name
        self.regularPriceWeek = regularPriceWeek
        self.regularPriceWeekend = regularPriceWeekend
        self.rewardPriceWeek = rewardPriceWeek
        self.rewardPriceWeekend = rewardPriceWeekend
        self.rating = rating

    def getPriceForPeriod(self, clientType, period):
        if clientType == 'regular':
            weekprice, weekendprice = self.regularPriceWeek, self.regularPriceWeekend
        else:
            weekprice, weekendprice = self.rewardPriceWeek, self.rewardPriceWeekend
        
        return self.calculatePrice(weekprice, weekendprice, period)

    def calculatePrice(self, weekprice, weekendprice, period):
        return sum([ weekendprice if self.isWeekend(day) else weekprice for day in period ])
        

    def isWeekend(self, day):
        return day in ['SAT', 'SUN'] 

