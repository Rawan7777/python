
data = {
    'alice': [
        'first_blood',
        'pixel_perfect',
        'speed_runner',
        'first_blood',
        'first_blood'
    ],
    'bob': [
        'first_blood',
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



# player_sets = {}

# for player, achievements in data.items():
#     player_sets[player] = set(achievements)

# all_unique = set().union(*player_sets.values())
# print(f"All unique achievements: {all_unique}")
# all_unique = set.union(*player_sets.values())
# print(f"All unique achievements: {all_unique}")





# dd = set.intersection(*player_sets.values())
# print(f"All unique achievements: {dd}")
# dd = set().intersection(*player_sets.values())
# print(f"All unique achievements: {dd}")


s1 = {2, 5, 8}
s2 = {3, 2, 7}

# s3 = s1.intersection(s2, s3, s4, s5)
# print(s3)
s4 = set.intersection(5, s2)
print(s4)
s5 = set([2]).intersection(s1, s2)
print(s5)