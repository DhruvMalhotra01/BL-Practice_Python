class Monster:
    def __init__(self, name: str, health: int, attack: int, reward: int):
        self.name = name
        self.health = health
        self.attack = attack
        self.reward = reward

    def calculate_battle_score(self) -> int:
        return int(self.reward + (self.health / 10) - self.attack)

# Monster database
monsters = {
    "Goblin": Monster("Goblin", 100, 20, 50),
    "Dragon": Monster("Dragon", 500, 80, 500),
    "Orc": Monster("Orc", 250, 40, 150),
    "Troll": Monster("Troll", 350, 60, 300),
}

def func5(chosen_name="Dragon"):
    monster = monsters[chosen_name]
    battle_score = monster.calculate_battle_score()

    print(f"Monster: {monster.name}")
    print(f"Battle Score: {battle_score}")
    return battle_score


if __name__ == "__main__":
    func5()
