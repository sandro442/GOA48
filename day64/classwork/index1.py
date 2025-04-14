class Human:
    def init(self, name, age):
        self.name = name
        self.age = age
    def str(self):
        return f"{self.name} {self.age}"
p2 = Human("Sandro", 17)
print(p2)