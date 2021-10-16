class Products:
    def __init__(self, place):
        self.place = place
        self.delivery = Delivery()
    
    def check_paper(self):
        print(f"\nToilet paper at {self.place} is finished.")
    
    def check_water(self):
        print(f"There is enough water at {self.place}.")

class Delivery:
    def __init__(self, water=5, day='Tuesday'):
        self.water = water
        self.day = day
    
    def check_delivery(self):
        print(f"The carrier is going to deliver {self.water} boxes of water on {self.day.title()}.")