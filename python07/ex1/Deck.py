from ex0.Card import Card
import math

class Deck:

    cards = {}

    def add_card(self, card: Card) -> None:
        Deck.cards[card.name] = card

    def remove_card(self, card_name: str) -> bool:
        ...

    def shuffle(self) -> None:
        ...

    def draw_card(self) -> Card:
        ...

    def get_deck_stats(self) -> dict:

        spell = 0
        artifact = 0
        creature = 0
        total_cost = 0

        for v in Deck.cards.values():
            if v.type == "Spell":
                spell += 1
            elif v.type == "Artifact":
                artifact += 1
            elif v.type == "Creature":
                creature += 1

            total_cost += v.cost
            

            avg_cost = total_cost / len(Deck.cards)

        return {
            "total_cards": len(Deck.cards),
            "creatures": creature,
            "spells": spell,
            "artifacts": artifact,
            "avg_cost": float(math.ceil(avg_cost))
        }
