from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    """Abstract interface for entities that participate in ranked play."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Compute and return the current numeric rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Increment the win counter by the given amount."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Increment the loss counter by the given amount."""
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict:
        """Return a dictionary describing the current rank state."""
        pass
