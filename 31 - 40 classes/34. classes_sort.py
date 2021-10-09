# My on exercise - not on the book
#
# CREATING A METHOD TO SORT AN ARRAY
class Ordina:
    
    def __init__(self):
        self.numbers = []
    
    def order(self, numbers):
        self.numbers = numbers
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                if self.numbers[i] > self.numbers[j]:
                    self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]
        return self.numbers


my_list = [1, 45, 12, 34, 95, 90, 13, 55]

sort = Ordina()

result = sort.order(my_list)

print(result)
