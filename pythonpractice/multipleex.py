class Bird:
    def __init__(self, birdname, eat):
        self.birdname = birdname
        self.eat = eat

    def birds_fly(self):
        print(f"name: {self.birdname}, eat: {self.eat}")

class Animal:
    def __init__(self, animalname):
        self.animalname = animalname

    def animal_run(self):
        print(f"animalname: {self.animalname}")

class Fly(Bird, Animal):
    def __init__(self, birdname, eat, animalname):
        Bird.__init__(self, birdname, eat)
        Animal.__init__(self, animalname)


g = Fly("parrot", "guava", "lion")


g.birds_fly()
g.animal_run()
print(Fly.__mro__)
