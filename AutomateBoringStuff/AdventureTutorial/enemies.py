class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp &amp;gt; 0

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)

class Clown(Enemy):
    def __init__(self):
        super().__init__(name="Clown", hp=50, damage=20)

class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=100, damage=30)

class Chtulu(Enemy):
    def __init__(self):
        super().__init__(name="Chtulu", hp=1000, damage=100)
