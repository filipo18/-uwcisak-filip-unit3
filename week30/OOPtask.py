# OOP practise


class Bicycle:
    # How do i increse number of bycicles every time by 1 when new bycicle is created
    def __init__(self, size=29, chain=11, tire_size='M'):
        self.size = size
        self.chain = chain
        self.tire_size = tire_size

    def circumference(self):
        print(self.tire_size * 3.14)

    def spares(self):
        print(f"Tyre size is {self.tire_size} inch and chain has {self.chain} speed ")
    # How do i increse number of bycicles every time by 1 when new bycicle is created


class MountainBike(Bicycle):
    def __init__(self, size=27.5, front_fork=100, rear_shock=80):
        # How do I set default value in this class for atribute from parent class
        self.front_fork = front_fork
        self.rear_shock = rear_shock
        self.size = size


# How do i create a list that stores the objects of bicycles and mountain bikes created
