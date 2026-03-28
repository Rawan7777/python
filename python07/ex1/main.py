from .Deck import Deck
from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard

print("=== DataDeck Deck Builder ===\n")

print("Building deck with different card types...")

lightning_bolt = SpellCard("Lightning Bolt", 3, "Legendary", "damage")
mana_crystal = ArtifactCard("Mana Crystal", 2, "Legendary", 1, "Permanent: +1 mana per turn")
fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

deck = Deck()

deck.add_card(lightning_bolt)
deck.add_card(mana_crystal)
deck.add_card(fire_dragon)

print(f"Deck stats: {deck.get_deck_stats()}\n")

print("Drawing and playing cards:\n")

game_state = {'mana': 6}

print(f"Drew: {lightning_bolt.name} ({lightning_bolt.type})")
print(f"Play result: {lightning_bolt.play(game_state)}\n")

print(f"Drew: {mana_crystal.name} ({mana_crystal.type})")
print(f"Play result: {mana_crystal.play(game_state)}\n")

print(f"Drew: {fire_dragon.name} ({fire_dragon.type})")
print(f"Play result: {fire_dragon.play(game_state)}\n")

print("Polymorphism in action: Same interface, different card behaviors!")