import items, enemies, actions, world

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MovesEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MovesWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MovesNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MovesSouth())
        return moves

    def available_actions(self):
        """Returns all the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall. You can make out four paths, each equally as dark, and forboding.
        """

    def modify_player(self, player):
        pass

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!

        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x,y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("{} does {} damage. You have {} HP remaining.".format(self.enemy.name, self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. Ypu must forge onwards.
        """

    def modify_player(self, player):
        pass

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a giant dead spider rots on the ground.
            """

class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An ugly ogre stares at you. He sneezes and covers you with ogre snot. Ew.
            """
        else:
            return """
            A big dead ugly ogre is laying in a pile of green blood.
            """

class ClownRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Clown())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A killer clown laughs maniacally, juggling small children's heads.
            """
        else:
            return """
            A stupid dead clown is humped on the ground, some recorded laughter is still playing from a recorder.
            """

class DragonRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Dragon())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A fiery dragon is towering above you. Rawr.
            """
        else:
            return """
            Big dead dragon laying there. A small puff of smoke poofs out of his dead nostrils.
            """

class ChtuluRoom(EnemyRoom):
    def __init__(self, x, y):
        super(),__init__(x, y, enemies.Chtulu())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Mighty Chtulu is the size of a mountain. You start to go crazy as you look into his giant eyes.
            """
        else:
            return """
            A little dead shrunken Chtulu is smooshed on the floor. He's stinky.
            """

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        You notice something shiny in the corner.  It's a dagger! You pick it up.
        """

class FindGoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(25))

    def intro_text(self):
        return """
        Ahhh, more another shiny something laying on the ground. Eureka! It's gold. You pick it up.
        """
