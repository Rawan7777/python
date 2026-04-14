from collections.abc import Callable
from typing import List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def caster(target: str, power: int) -> str:

        if condition(target, power):
            return spell(target, power)

        return "Spell fizzled"

    return caster


def spell_sequence(spells: List[Callable]) -> Callable:

    def sequence(target: str, power: int) -> List[str]:
        return [spell(target, power) for spell in spells]

    return sequence


if __name__ == "__main__":

    try:

        def fireball(target: str, power: int) -> str:
            return f"Fireball hits {target} for {power} damage"

        def heal(target: str, power: int) -> str:
            return f"Heals {target} for {power} health"

        print("Testing spell combiner...")
        combined = spell_combiner(fireball, heal)
        result = combined("Dragon", 10)
        print(f"Combined spell result: {result[0]}, {result[1]}")

        print("\nTesting power amplifier...")
        mega_fireball = power_amplifier(fireball, 3)
        original = fireball("Dragon", 10)
        amplified = mega_fireball("Dragon", 10)
        print("Original: 10, Amplified: 30")
        print(f"{original}")
        print(f"{amplified}")

        print("\nTesting conditional caster...")

        def strong_enough(target: str, power: int) -> bool:
            return power >= 20

        conditional = conditional_caster(strong_enough, fireball)
        print(conditional("Dragon", 25))
        print(conditional("Dragon", 5))

        print("\nTesting spell sequence...")
        sequence = spell_sequence([fireball, heal])
        results = sequence("Dragon", 15)
        for r in results:
            print(f"{r}")

    except Exception as error:
        print(f"Error catched: {error}")
