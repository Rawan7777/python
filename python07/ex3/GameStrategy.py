from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract interface defining a playing strategy."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute a full turn using the current hand and battlefield."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the human-readable name of this strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Return the target list ordered by priority for this strategy."""
        pass
