import time
from functools import wraps
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func()
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_power = kwargs.get("power")
            if current_power is None:
                for arg in args:
                    if isinstance(arg, int):
                        current_power = arg
            if current_power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    try:

        print("Testing spell timer...")

        @spell_timer
        def fireball():
            time.sleep(0.1)
            return "Fireball cast!"

        result = fireball()
        print(f"Result: {result}")

        print("\nTesting retrying spell...")

        @retry_spell(max_attempts=3)
        def unstable_spell():
            raise RuntimeError("Spell unstable!")

        @retry_spell(max_attempts=3)
        def always_fails():
            raise RuntimeError("Spell unstable!")

        outcome = always_fails()
        print(outcome)
        print("Waaaaaaagh spelled !")

        print("\nTesting MageGuild...")
        guild = MageGuild()
        print(MageGuild.validate_mage_name("Merlin"))
        print(MageGuild.validate_mage_name("X2"))

        print(guild.cast_spell("Lightning", 15))
        print(guild.cast_spell("Lightning", 5))

    except Exception as error:
        print(f"Error catched: {error}")
