class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value  = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                        description="A round coin with {} stamped on the front.".format(str(self.amt)),
                        value="self.amt"
                        )

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.decription, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                        description="A fist-sized rock, suitable for bludgeoning.",
                        value=0,
                        damage=5
                        )

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                        description="A small rusty dagger. Somewhat more dangerous than a rock.",
                        value=10,
                        damage=10
                        )

class Axe(Weapon):
    def __init__(self):
        super().__init__(name="Axe",
                        description="A sharp axe. Swing at bad guys.",
                        value=20,
                        damage=20)

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                        description="A super-sharp sword. This should do some damage!",
                        value=50,
                        damage=50)
