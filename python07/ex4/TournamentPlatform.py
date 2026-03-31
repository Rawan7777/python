import random
from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages card registration, match creation, and leaderboard tracking."""

    def __init__(self) -> None:

        self._cards: Dict[str, TournamentCard] = {}
        self._matches: List[dict] = []

    def _generate_id(self, card: TournamentCard) -> str:
        """Produce a short deterministic ID from the card name."""

        prefix = card.name.split()[1].lower()
        suffix = f"{random.randint(100, 999):03d}"

        return f"{prefix}_{suffix}"

    def register_card(self, card: TournamentCard) -> str:
        """Register a card in the platform and return its assigned ID."""

        card_id = self._generate_id(card)

        while card_id in self._cards:
            card_id = self._generate_id(card)

        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulate a match between two registered cards."""

        if card1_id not in self._cards:
            raise KeyError(f"Card ID '{card1_id}' not registered.")
        if card2_id not in self._cards:
            raise KeyError(f"Card ID '{card2_id}' not registered.")

        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]

        score1 = card1.attack_power + card1.defense
        score2 = card2.attack_power + card2.defense

        if score1 > score2:
            winner_id, loser_id = card1_id, card2_id
        elif score2 > score1:
            winner_id, loser_id = card2_id, card1_id
        else:
            winner_id, loser_id = "no one", "no one"

        if winner_id != "no one" and loser_id != "no one":

            winner = self._cards[winner_id]
            loser = self._cards[loser_id]

            winner.update_wins(1)
            loser.update_losses(1)

        result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

        self._matches.append(result)

        return result

    def get_leaderboard(self) -> List[dict]:
        """Return all registered cards sorted by rating descending."""

        entries = [
            {"id": cid, **card.get_rank_info()}
            for cid, card in self._cards.items()
        ]

        return sorted(entries, key=lambda e: e["rating"], reverse=True)

    def generate_tournament_report(self) -> dict:
        """Return a summary of all tournament activity."""

        ratings = [c.calculate_rating() for c in self._cards.values()]
        avg_rating = int(sum(ratings) / len(ratings)) if ratings else 0

        return {
            "total_cards": len(self._cards),
            "matches_played": len(self._matches),
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
