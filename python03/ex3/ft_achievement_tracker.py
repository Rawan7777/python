
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

print("=== Achievement Tracker System ===\n")

player_sets = {}

for player, achievements in data.items():
    player_sets[player] = set(achievements)
    print(f"Player {player} achievements: {player_sets[player]}")

print("\n=== Achievement Analytics ===")

all_unique = set.union(*player_sets.values())
print(f"All unique achievements: {all_unique}")
print(f"Total unique achievements: {len(all_unique)}\n")

common_all = set.intersection(*player_sets.values())
print(f"Common to all players: {common_all}")

achievement_count = {}

for achievements in player_sets.values():
    for ach in achievements:
        if ach in achievement_count:
            achievement_count[ach] += 1
        else:
            achievement_count[ach] = 1

rare = {ach for ach, count in achievement_count.items() if count == 1}
print(f"Rare achievements (1 player only): {rare}\n")

common = player_sets["alice"].intersection(player_sets["bob"])
unique_alice = player_sets["alice"].difference(player_sets["bob"])
unique_bob = player_sets["bob"].difference(player_sets["alice"])

print(f"Alice vs Bob common: {common}")
print(f"Alice unique: {unique_alice}")
print(f"Bob unique: {unique_bob}")
