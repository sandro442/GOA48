class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def lower(self):
        return self.name.lower()
p1 = Person("Sandro", 17)
print(p1.lower())