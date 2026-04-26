class car:
    def __init__(self):
        self.seat_type = ""
        self.color = ""
        self.automatic_or_manual = ""
        self.seats = ""
        self.interior_color = ""
    def change(self):
        self.interior_color = "black"
jeep = car()
jeep.change()
print(jeep.interior_color)
