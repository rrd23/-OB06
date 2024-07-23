import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print(f"Битва начинается! {self.player.name} против {self.computer.name}")

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            damage = self.player.attack(self.computer)
            print(
                f"{self.player.name} атакует и наносит {damage} урона. У {self.computer.name} осталось {self.computer.health} здоровья.")

            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

            # Ход компьютера
            damage = self.computer.attack(self.player)
            print(
                f"{self.computer.name} атакует и наносит {damage} урона. У {self.player.name} осталось {self.player.health} здоровья.")

            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break

        print("Игра окончена!")


def main():
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()


if __name__ == "__main__":
    main()