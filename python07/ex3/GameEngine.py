from typing import List, Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Orchestrates card game turns using a factory and a strategy."""

    def __init__(self) -> None:
        self._factory: Optional[CardFactory] = None
        self._strategy: Optional[GameStrategy] = None
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: List = []

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Attach a factory and a strategy to the engine."""
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        """Generate a hand via the factory and execute a strategy turn."""
        if self._factory is None or self._strategy is None:
            raise RuntimeError("Engine not configured. \
                               Call configure_engine first.")

        hand = [
            self._factory.create_creature("Fire Dragon"),
            self._factory.create_creature("Goblin Warrior"),
            self._factory.create_spell("Lightning Bolt"),
        ]
        self._cards_created.extend(hand)

        battlefield: List = []
        result = self._strategy.execute_turn(hand, battlefield)

        damage = result.get("actions", {}).get("damage_dealt", 0)
        self._total_damage += damage
        self._turns_simulated += 1

        hand_summary = [
            f"{c.name} ({c.cost})" for c in hand
        ]

        return {
            "hand": hand_summary,
            "turn_execution": result,
        }

    def get_engine_status(self) -> dict:
        """Return a summary report of the engine's activity."""
        strategy_name = (
            self._strategy.get_strategy_name()
            if self._strategy else "None"
        )
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self._total_damage,
            "cards_created": len(self._cards_created),
        }
