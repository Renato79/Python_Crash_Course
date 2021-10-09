class Bills:
    def __init__(self, place):
        self.place = place
    
    def check_gas(self):
        print(f"\n{self.place.title()} gas bill must be paid.")
    
    def check_el(self):
        print(f"{self.place.title()} electricity bill has been paid. No further bills.")