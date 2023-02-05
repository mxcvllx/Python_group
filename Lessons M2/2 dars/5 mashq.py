class Country():
    def __init__(self, sum):
        self.sum = sum
        if sum > 10000000:
            self.sum = ">10M"
        elif sum < 10000000:
            self.sum = "<10M"
        elif sum == 10000000:
            self.sum = "10M"


sum = int(input("Aholi sonini kiriting: "))
object = Country(sum)

print(object.sum)
