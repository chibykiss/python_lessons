class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def moves(self):
        print('Moves along ...')

    def getMakeModel(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla','Model3')

print(my_car.make)
my_car.moves()
my_car.getMakeModel()

your_car = Vehicle('Mercedez Benz','Gle')
your_car.getMakeModel()

class Aeroplane(Vehicle):
    def __init__(self, make, model, faaid):
        super().__init__(make, model)
        self.faaid = faaid
    def moves(self):
        print('Flies along')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')

class Jeep(Vehicle):
    pass

falconfire = Aeroplane('Falconfire','XF-29 Stealthstrike','NCX-374748')
print(falconfire.faaid)
falconfire.moves()

ironclad = Truck('Ironclad','Titan T900X')
ironclad.moves()

trailHawk = Jeep('TrailHawk','Vortex V4 Recon')
trailHawk.getMakeModel()

print('\n\n')

for v in (my_car, your_car, falconfire, ironclad, trailHawk):
    v.getMakeModel()
    v.moves()
