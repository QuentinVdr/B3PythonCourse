class player:
    def __init__(self, name, hp, atk, df, catchphrase)
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.atk = atk
        self.df = df
        self.catchphrase = catchphrase

    def attack(self, player):
        player.hp -= (self.atk - player.df)

    def greet(self):
        print(f'My name is {self.name}, {self.catchphrase}')


class warrior(player):
    def __init__(self, name, hp, atk, df, catchphrase):
        super().__init__(name, hp, atk, df, catchphrase)

    def battle_cry(self):
        print('{catchphrase}!!!')


class clerk(player):
    def __init__(self, name, hp, atk, df, catchphrase):
        super().__init__(name, hp, atk, df, catchphrase)

    def heal(self, player):
        player.hp += 10
        if player.hp > player.maxhp:
            player.hp = player.maxhp


class paladin(player, warrior, clerk):
    def __init__(self, name, hp, atk, df, catchphrase):
        super().__init__(name, hp, atk, df, catchphrase)


class mage(player):
    def __init__(self, name, hp, atk, df, catchphrase, mp):
        super().__init__(name, hp, atk, df, catchphrase)
        self.mp = mp

    def cast_spell(self, player):
        player.hp -= self.atk
        self.hp += self.atk
        self.mp -= 10


class archer(player):
    def __init__(self, name, hp, atk, df, catchphrase):
        super().__init__(name, hp, atk, df, catchphrase)

    def shoot(self, player):
        player.hp -= self.atk
