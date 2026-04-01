from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from enum import Enum


class RARITY(Enum):

    LEGENDARY = "Legendary"
    COMMON = "Common"
    EPIC = "Epic"
    RARE = "Rare"
    UNCOMMON = "Uncommon"


def main() -> None:

    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...")

    dragon = TournamentCard("Fire Dragon", 5, RARITY.LEGENDARY.value,
                            7, 5, 1200)
    wizard = TournamentCard("Ice Wizard", 4, RARITY.RARE.value, 4, 3, 1150)

    platform = TournamentPlatform()

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    for card_id, card in [(dragon_id, dragon), (wizard_id, wizard)]:

        info = card.get_rank_info()

        print(f"\n{card.name} (ID: {card_id}):")
        print(f"- Interfaces: [\
{Card.__name__}, {Combatable.__name__}, {Rankable.__name__}]")
        print(f"- Rating: {info['rating']}")
        print(f"- Record: {info['record']}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    for rank, entry in enumerate(platform.get_leaderboard(), start=1):
        print(
            f"{rank}. {entry['name']} - "
            f"Rating: {entry['rating']} ({entry['record']})"
        )

    print(f"\nPlatform Report:\n{platform.generate_tournament_report()}")

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
