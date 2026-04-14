from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    powers = []
    for ele in mages:
        powers.append(ele['power'])
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


if __name__ == "__main__":

    try:

        print("Testing artifact sorter...")

        artifacts = [
            {"name": "Storm Crown", "power": 111, "type": "focus"},
            {"name": "Lightning Rod", "power": 108, "type": "armor"},
            {"name": "Lightning Rod", "power": 109, "type": "relic"},
            {"name": "Water Chalice", "power": 88, "type": "focus"},
        ]

        sorted_artifacts = artifact_sorter(artifacts)
        first, second = sorted_artifacts[0], sorted_artifacts[1]
        print(
            f"{first['name']} ({first['power']} power) "
            f"comes before {second['name']} ({second['power']} power)"
        )

        print("\nTesting power filter...")

        mages = [
            {"name": "Morgan", "power": 91, "element": "fire"},
            {"name": "Sage", "power": 65, "element": "light"},
            {"name": "Casey", "power": 60, "element": "light"},
            {"name": "Riley", "power": 51, "element": "fire"},
            {"name": "Alex", "power": 51, "element": "wind"},
        ]

        filtered = power_filter(mages, 70)
        print(f"Mages with power >= 70: {[m['name'] for m in filtered]}")

        print("\nTesting spell transformer...")
        spells = [
            "blizzard",
            "meteor",
            "lightning",
            "earthquake",
        ]
        print(" ".join(spell_transformer(spells)))

        print("\nTesting mage stats...")
        stats = mage_stats(mages)
        print(
            f"Max: {stats['max_power']}, Min: {stats['min_power']}, "
            f"Avg: {stats['avg_power']}"
        )

    except Exception as error:
        print(f"Error catched: {error}")
