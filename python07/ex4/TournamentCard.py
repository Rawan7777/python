from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


_K_FACTOR = 32


class TournamentCard(Card, Combatable, Rankable):
    """
    A card suitable for tournament play.
    Combines Card, Combatable, and Rankable interfaces.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, defense: int, rating: int) -> None:

        Card.__init__(self, name, cost, rarity)

        self.attack_power = attack_power
        self.defense = defense
        self._wins: int = 0
        self._losses: int = 0
        self.rating: int = rating

    # card

    def get_card_info(self) -> Dict:

        info = super().get_card_info()
        info["type"] = "TournamentCard"
        info["attack_power"] = self.attack_power
        info["defense"] = self.defense

        return info

    def play(self, game_state: dict) -> dict:

        return {
            "card_played": self.name,
            "mana_used": game_state.get('mana'),
            "effect": "Tournament card enters the arena",
        }

    # combatable

    def attack(self, target) -> dict:

        target_name = target.name if hasattr(target, "name") else str(target)

        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "tournament",
        }

    def defend(self, incoming_damage: int) -> dict:

        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": taken < self.defense,
        }

    def get_combat_stats(self) -> Dict:

        return {
            "name": self.name,
            "attack_power": self.attack_power,
            "defense": self.defense,
        }

    # rankable

    def calculate_rating(self) -> int:
        """Return the stored ELO-style rating."""
        return self.rating

    def update_wins(self, wins: int) -> None:

        self._wins += wins
        self.rating += _K_FACTOR * wins

    def update_losses(self, losses: int) -> None:

        self._losses += losses
        self.rating = max(0, self.rating - _K_FACTOR * losses)

    def get_rank_info(self) -> Dict:

        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self._wins,
            "losses": self._losses,
            "record": f"{self._wins}-{self._losses}",
        }

    # ------

    def get_tournament_stats(self) -> Dict:

        return {
            **self.get_card_info(),
            **self.get_rank_info(),
            "interfaces": ["Card", "Combatable", "Rankable"],
        }
