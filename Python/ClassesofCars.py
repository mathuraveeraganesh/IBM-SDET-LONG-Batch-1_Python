"""
Create a car class with the following details:
Properties: manufacturer, model, make, transmission, color
Methods: accelerate(), stop()
accelerate() should print "{Manufacturer} {Model} is moving"
stop() should print "{Manufacturer} {Model} has stopped"
Using this car class, create 3 different car objects."""

class car:

    def __init__(self,manufacturer,model,make,transmission,color):
        self.manufacturer=manufacturer
        self.model=model
        self.make=make
        self.transmission=transmission
        self.color=color

    def accelerate(self):
        print(self.manufacturer+self.model+"is Moving")

    def stop(self):
        print(self.manufacturer+self.model+"is Stopping")
        

p1=car("Maruthi","Alto","2020","Manual","Red")
p2=car("Honda","Jazz","2000","Manual","Red")
p1.accelerate()
p2.stop()