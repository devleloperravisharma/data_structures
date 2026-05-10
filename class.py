import time

class car:
    def __init__(self):
        self.seat_type = ""
        self.color = ""
        self.automatic_or_manual = ""
        self.seats = ""
        self.interior_color = ""
        self.when = ""
        self.__type = ""
        self.brand = ""
    #def change(self):
        #self.interior_color = "black"
    def getting_values(self):
        self.seat_type = input("what type of seats do you have?")
        self.color = input("what color is the exterior of your car?")
        self.automatic_or_manual = input("is your car manual or automatic?")
        self.seats = input("how many seats are in your car?")
        self.interior_color = input("what is the color of your cars interior?")
        self.when = input("when did you get your car?")
        self.type = input("what model car do you have?")
        self.brand = input("what brand is your car from?")
    def load(self):
        print("loading car details...")
    def set_up(self):
        print("setting up car profile...")
    def ready(self):
        print("car profile is now ready!")
    def displayy(self):
        print(f"CAR PROFILE \nseat type: {self.seat_type}\ncar color: {self.color}\ngear transmission type: {self.automatic_or_manual}\nseat number: {self.seats}\ninterior color: {self.interior_color}\nwhen car was bought: {self.when}\nbrand: {self.brand}\ntype of car: {self.type}")

class SportsCar(car):
    def __init__(self):
        super().__init__()
        self.top_speed = ""
    def get_speed(self):
        self.top_speed = input("what is the top speed of your sports car in miles per hour?")

    def ready(self):
        print("sports car profile is now ready!!!!")
    
    def displayy(self):
        super().displayy()
        print(f"top speed: {self.top_speed} mph")

# object of the child class -- the sports car one
ferrari = SportsCar()

ferrari.getting_values()
ferrari.get_speed()
ferrari.load()
time.sleep(0.6)
ferrari.set_up()
time.sleep(0.6)
ferrari.ready()
time.sleep(0.6)
ferrari.displayy()

"""
jeep = car()
#jeep.change()
#print(jeep.type)
jeep.getting_values()
jeep.load()
time.sleep(0.6)
jeep.set_up()
time.sleep(0.6)
jeep.ready()
time.sleep(0.6)
#jeep.displayy()"""