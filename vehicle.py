class vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

Bmw = vehicle(300, 26)
print("Bmw's max speed:", Bmw.max_speed)
print("Bmw's mileage:", Bmw.mileage)