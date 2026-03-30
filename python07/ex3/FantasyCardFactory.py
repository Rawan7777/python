import random
from typing import List, Union
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Concrete factory that produces fantasy-themed cards."""

    _CREATURES = [
        {
            "name": "Fire Dragon", "cost": 5, "rarity": "Legendary",
            "attack": 7, "health": 5,
        },
        {
            "name": "Goblin Warrior", "cost": 2, "rarity": "Common",
            "attack": 2, "health": 1,
        },
    ]

    _SPELLS = [
        {
            "name": "Fireball", "cost": 4, "rarity": "Rare",
            "effect_type": "damage"
        },
        {
            "name": "Lightning Bolt", "cost": 3, "rarity": "Rare",
            "effect_type": "damage",
        },
    ]

    _ARTIFACTS = [
        {
            "name": "Mana Ring", "cost": 2, "rarity": "Rare", "durability": 5,
            "effect": "+1 mana per turn",
        },
    ]

    def create_creature(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if isinstance(name_or_power, str):
            data = next(
                (c for c in self._CREATURES
                 if c["name"].lower() == name_or_power.lower()),
                self._CREATURES[0],
            )
        else:
            data = random.choice(self._CREATURES)
        return CreatureCard(
            data["name"], data["cost"], data["rarity"],
            data["attack"], data["health"],
        )

    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if isinstance(name_or_power, str):
            data = next(
                (s for s in self._SPELLS
                 if s["name"].lower() == name_or_power.lower()),
                self._SPELLS[0],
            )
        else:
            data = random.choice(self._SPELLS)
        return SpellCard(
            data["name"], data["cost"], data["rarity"], data["effect_type"]
        )

    def create_artifact(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        if isinstance(name_or_power, str):
            data = next(
                (a for a in self._ARTIFACTS
                 if a["name"].lower() == name_or_power.lower()),
                self._ARTIFACTS[0],
            )
        else:
            data = random.choice(self._ARTIFACTS)
        return ArtifactCard(
            data["name"], data["cost"], data["rarity"],
            data["durability"], data["effect"],
        )

    def create_themed_deck(self, size: int) -> dict:

        cards: List[Card] = []
        creators = [
            self.create_creature,
            self.create_spell,
            self.create_artifact
        ]

        try:

            for i in range(size):
                cards.append(creators[i % 3]())
            return {
                "theme": "Fantasy",
                "size": len(cards),
                "cards": cards,
            }

        except Exception:
            return {}

    def get_supported_types(self) -> dict:
        return {
            "creatures": [crea['name'] for crea in self._CREATURES],
            "spells": [crea['name'] for crea in self._SPELLS],
            "artifacts": [crea['name'] for crea in self._ARTIFACTS]
        }
