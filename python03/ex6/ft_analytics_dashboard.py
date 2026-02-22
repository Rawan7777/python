#!/usr/bin/env python3

data = {
    'players': {
        'alice': {
            'level': 41,
            'total_score': 2824,
            'sessions_played': 13,
            'favorite_mode': 'ranked',
            'achievements_count': 5,
        },
        'bob': {
            'level': 16,
            'total_score': 4657,
            'sessions_played': 27,
            'favorite_mode': 'ranked',
            'achievements_count': 2,
        },
        'charlie': {
            'level': 44,
            'total_score': 9935,
            'sessions_played': 21,
            'favorite_mode': 'ranked',
            'achievements_count': 7,
        },
        'diana': {
            'level': 3,
            'total_score': 1488,
            'sessions_played': 21,
            'favorite_mode': 'casual',
            'achievements_count': 4,
        },
        'eve': {
            'level': 33,
            'total_score': 1434,
            'sessions_played': 81,
            'favorite_mode': 'casual',
            'achievements_count': 7,
        },
        'frank': {
            'level': 15,
            'total_score': 8359,
            'sessions_played': 85,
            'favorite_mode': 'competitive',
            'achievements_count': 1,
        },
    },
    'sessions': [
        {
            'player': 'bob',
            'duration_minutes': 94,
            'score': 1831,
            'mode': 'competitive',
            'completed': False,
        },
        {
            'player': 'bob',
            'duration_minutes': 32,
            'score': 1478,
            'mode': 'casual',
            'completed': True,
        },
        {
            'player': 'diana',
            'duration_minutes': 17,
            'score': 1570,
            'mode': 'competitive',
            'completed': False,
        },
        {
            'player': 'alice',
            'duration_minutes': 98,
            'score': 1981,
            'mode': 'ranked',
            'completed': True,
        },
        {
            'player': 'diana',
            'duration_minutes': 15,
            'score': 2361,
            'mode': 'competitive',
            'completed': False,
        },
        {
            'player': 'eve',
            'duration_minutes': 29,
            'score': 2985,
            'mode': 'casual',
            'completed': True,
        },
        {
            'player': 'frank',
            'duration_minutes': 34,
            'score': 1285,
            'mode': 'casual',
            'completed': True,
        },
        {
            'player': 'alice',
            'duration_minutes': 53,
            'score': 1238,
            'mode': 'competitive',
            'completed': False,
        },
        {
            'player': 'bob',
            'duration_minutes': 52,
            'score': 1555,
            'mode': 'casual',
            'completed': False,
        },
        {
            'player': 'frank',
            'duration_minutes': 92,
            'score': 2754,
            'mode': 'casual',
            'completed': True,
        },
        {
            'player': 'eve',
            'duration_minutes': 98,
            'score': 1102,
            'mode': 'casual',
            'completed': False,
        },
        {
            'player': 'diana',
            'duration_minutes': 39,
            'score': 2721,
            'mode': 'ranked',
            'completed': True,
        },
        {
            'player': 'frank',
            'duration_minutes': 46,
            'score': 329,
            'mode': 'casual',
            'completed': True,
        },
        {
            'player': 'charlie',
            'duration_minutes': 56,
            'score': 1196,
            'mode': 'casual',
            'completed': True,
        },
        {
            'player': 'eve',
            'duration_minutes': 117,
            'score': 1388,
            'mode': 'casual',
            'completed': False,
        },
        {
            'player': 'diana',
            'duration_minutes': 118,
            'score': 2733,
            'mode': 'competitive',
            'completed': True,
        },
        {
            'player': 'charlie',
            'duration_minutes': 22,
            'score': 1110,
            'mode': 'ranked',
            'completed': False,
        },
        {
            'player': 'frank',
            'duration_minutes': 79,
            'score': 1854,
            'mode': 'ranked',
            'completed': False,
        },
        {
            'player': 'charlie',
            'duration_minutes': 33,
            'score': 666,
            'mode': 'ranked',
            'completed': False,
        },
        {
            'player': 'alice',
            'duration_minutes': 101,
            'score': 292,
            'mode': 'casual',
            'completed': True,
        },
        {
            'player': 'frank',
            'duration_minutes': 25,
            'score': 2887,
            'mode': 'competitive',
            'completed': True,
        },
        {
            'player': 'diana',
            'duration_minutes': 53,
            'score': 2540,
            'mode': 'competitive',
            'completed': False,
        },
        {
            'player': 'eve',
            'duration_minutes': 115,
            'score': 147,
            'mode': 'ranked',
            'completed': True,
        },
        {
            'player': 'frank',
            'duration_minutes': 118,
            'score': 2299,
            'mode': 'competitive',
            'completed': False,
        },
        {
            'player': 'alice',
            'duration_minutes': 42,
            'score': 1880,
            'mode': 'casual',
            'completed': False,
        },
        {
            'player': 'alice',
            'duration_minutes': 97,
            'score': 1178,
            'mode': 'ranked',
            'completed': True,
        },
        {
            'player': 'eve',
            'duration_minutes': 18,
            'score': 2661,
            'mode': 'competitive',
            'completed': True,
        },
        {
            'player': 'bob',
            'duration_minutes': 52,
            'score': 761,
            'mode': 'ranked',
            'completed': True,
        },
        {
            'player': 'eve',
            'duration_minutes': 46,
            'score': 2101,
            'mode': 'casual',
            'completed': True,
        },
        {
            'player': 'charlie',
            'duration_minutes': 117,
            'score': 1359,
            'mode': 'casual',
            'completed': True,
        },
    ],
    'game_modes': [
        'casual',
        'competitive',
        'ranked',
    ],
    'achievements': [
        'first_blood',
        'level_master',
        'speed_runner',
        'treasure_seeker',
        'boss_hunter',
        'pixel_perfect',
        'combo_king',
        'explorer',
    ],
}

if __name__ == "__main__":

    print("=== Game Analytics Dashboard ===")

    players = data['players']
    sessions = data['sessions']
    achievements = data['achievements']

    print("\n=== List Comprehension Examples ===")

    high_scorers = [
        p for p, v in players.items()
        if v['total_score'] > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [
        v['total_score'] * 2 for v in players.values()
    ]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [
        p for p, v in players.items()
        if v['sessions_played'] > 20
    ]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {
        p: d['total_score']
        for p, d in players.items()
    }
    print(f"Player scores: {player_scores}")

    score_categories = {
        'high': sum(
            1 for v in players.values()
            if v['total_score'] > 5000
        ),
        'medium': sum(
            1 for d in players.values()
            if 2000 <= d['total_score'] <= 5000
        ),
        'low': sum(
            1 for d in players.values()
            if d['total_score'] < 2000
        ),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {
        p: d['achievements_count']
        for p, d in players.items()
    }
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {n['player'] for n in sessions if n['completed'] is True
                      and n['mode'] == "ranked"}
    print(f"Unique players: {unique_players}")

    unique_achievements = {a for a in achievements if '_' in a}
    print(f"Unique achievements: {unique_achievements}")

    active_modes = {s['mode'] for s in sessions}
    print(f"Active modes: {active_modes}")

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    total_unique_achievements = len(unique_achievements)

    average_score = (
        sum(v['total_score'] for v in players.values())
        / total_players
    )

    def get_total_score(key):
        return players[key]['total_score']

    top_player_name = max(players, key=get_total_score)

    top_player_score = players[top_player_name]['total_score']
    top_player_achievements = (
        players[top_player_name]['achievements_count']
    )

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score:.1f}")
    print(
        "Top performer: "
        f"{top_player_name} "
        f"({top_player_score} points, "
        f"{top_player_achievements} achievements)"
    )
