from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:

    try:

        print("=== DataDeck Game Engine ===\n")
        print("Configuring Fantasy Card Game...")

        factory = FantasyCardFactory()
        strategy = AggressiveStrategy()
        engine = GameEngine()

        engine.configure_engine(factory, strategy)

        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.__class__.__name__}")
        print(f"Available types: {factory.get_supported_types()}")

        print("\nSimulating aggressive turn...")
        turn_result = engine.simulate_turn()

        print(f"Hand: {turn_result['hand']}")
        print("\nTurn execution:")
        print(f"Strategy: {turn_result['turn_execution']['strategy']}")
        print(f"Actions: {turn_result['turn_execution']['actions']}")

        print(f"\nGame Report:\n{engine.get_engine_status()}")

        print(
            "\nAbstract Factory + Strategy Pattern:\
Maximum flexibility achieved!"
        )

    except Exception as exc:
        print(f"Fatal error: {exc}")


main()
