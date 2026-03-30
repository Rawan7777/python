from typing import List
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    Aggressive strategy: play low-cost creatures first,
    then attack the enemy player directly.
    """

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Place 'Enemy Player' at the top of the target list."""

        try:

            prioritized = [t for t in available_targets if t == "Enemy Player"]
            others = [t for t in available_targets if t != "Enemy Player"]
            return prioritized + others

        except Exception:
            return []

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Play lowest-cost cards first and attack with all units."""

        sorted_hand = hand[:]
        n = len(sorted_hand)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if sorted_hand[j].cost < sorted_hand[min_index].cost:
                    min_index = j

            temp = sorted_hand[i]
            sorted_hand[i] = sorted_hand[min_index]
            sorted_hand[min_index] = temp

        mana = 9
        cards_played: List[str] = []
        mana_used = 0
        damage_dealt = 0

        for card in sorted_hand:
            if card.is_playable(mana):
                cards_played.append(card.name)
                mana -= card.cost
                mana_used += card.cost
                damage_dealt += card.cost

        targets = self.prioritize_targets(["Enemy Player", "Alias Creature"])

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": [targets[0]],
                "damage_dealt": damage_dealt,
            },
        }
