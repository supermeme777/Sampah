
import random

class Accessory:
    def __init__(self, name, rarity, probability):
        self.name = name
        self.rarity = rarity  # "Common", "Rare", "Epic", "Legendary"
        self.probability = probability

    def __repr__(self):
        return f"{self.name} [{self.rarity}]"

class SpecialEgg:
    def __init__(self, accessories):
        self.accessories = accessories
        self.__normalize_probabilities__()

    def __normalize_probabilities__(self):
        total = sum(item.probability for item in self.accessories)
        if total == 0:
            raise ValueError("Total probability can't be zero.")
        for item in self.accessories:
            item.probability /= total

    def open(self):
        return random.choices(
            self.accessories,
            weights=[item.probability for item in self.accessories],
            k=1
        )[0]

# Default accessory pool
default_accessories = [
    Accessory("Hat","Common", 0.5),
    Accessory("snapback cap", "Rare", 0.25),
    Accessory("cinnabon roll clip", "Epic", 0.15),
    Accessory("cheekskawa beanie", "Legendary", 0.10),
]

# Test it out
if __name__ == "_main_":
    egg = SpecialEgg(default_accessories)
    print("🐣 You bought a special egg!")
    reward = egg.open()
    print(f"🎁 You got: {reward}")