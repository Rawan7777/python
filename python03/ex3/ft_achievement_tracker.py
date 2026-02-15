
data = {
    'alice': [
        'first_blood',
        'pixel_perfect',
        'speed_runner',
        'first_blood',
        'first_blood'
    ],
    'bob': [
        'level_master',
        'boss_hunter',
        'treasure_seeker',
        'level_master',
        'level_master'
    ],
    'charlie': [
        'treasure_seeker',
        'boss_hunter',
        'combo_king',
        'first_blood',
        'boss_hunter',
        'first_blood',
        'boss_hunter',
        'first_blood'
    ],
    'diana': [
        'first_blood',
        'combo_king',
        'level_master',
        'treasure_seeker',
        'speed_runner',
        'combo_king',
        'combo_king',
        'level_master'
    ],
    'eve': [
        'level_master',
        'treasure_seeker',
        'first_blood',
        'treasure_seeker',
        'first_blood',
        'treasure_seeker'
    ],
    'frank': [
        'explorer',
        'boss_hunter',
        'first_blood',
        'explorer',
        'first_blood',
        'boss_hunter'
    ]
}

alice_achiev = set(data["alice"])
bob_achiev = set(data["bob"])
charlie_achiev = set(data["charlie"])

print("=== Achievement Tracker System ===\n")

print(f"Player alice achievements: {alice_achiev}")
print(f"Player bob achievements: {bob_achiev}")
print(f"Player charlie achievements: {charlie_achiev}")

print("\n=== Achievement Analytics ===")

union_set = alice_achiev.union(bob_achiev).union(charlie_achiev)
print(f"All unique achievements: {union_set}")
print(f"Total unique achievements: {len(union_set)}\n")

intersiction_set = alice_achiev.intersection(bob_achiev).intersection(charlie_achiev)
print(f"Common to all players: {intersiction_set}")

bob_difference_set = bob_achiev.difference(charlie_achiev)
charlie_difference_set = charlie_achiev.difference(bob_achiev)

difference_set = bob_difference_set
difference_set.update(charlie_difference_set)

difference_sett = difference_set.difference(alice_achiev)
print(f"Rare achievements (1 player): {difference_sett}\n")

alice_vs_bob = alice_achiev.intersection(bob_achiev)
print(f"Alice vs Bob common: {alice_vs_bob}")

alice_unique = alice_achiev.difference(bob_achiev)
print(f"Alice unique:: {alice_unique}")

bob_unique = bob_achiev.difference(alice_achiev)
print(f"Bob unique: {bob_unique}")