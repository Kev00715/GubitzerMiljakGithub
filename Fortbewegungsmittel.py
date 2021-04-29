class Auto:
    def __init__(self, number_wheels, name, durchschnitt):
        self.wheels = number_wheels
        self.name = name
        self.durchschnitt = durchschnitt

    

    def Go(self):
        print("driving")

class Bike:
    wheels = 2

    def Go(self):
        print("pedalling")

class Airplanes:
    wheels = 2

    def Go(self):
        print("pedalling")

a = Auto(4, "Toyota", 90)
print("Number of wheels:", a.wheels)
print("Name of the car:", a.name)
print("Durchschnittgeschwindigkeit:", a.durchschnitt,"km/h")
a.Go()
