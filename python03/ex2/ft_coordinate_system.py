#!/usr/bin/env python3

import sys
import math


def create_position(x: int, y: int, z: int) -> tuple[int, int, int]:
    """Create a 3D position tuple from x, y, z coordinates."""
    return (x, y, z)


def distance_3d(p1: tuple[int, int, int],
                p2: tuple[int, int, int]) -> float:

    """Calculate the Euclidean distance between two 3D points."""

    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt(
        pow((x2 - x1), 2) +
        pow((y2 - y1), 2) +
        pow((z2 - z1), 2)
    )


def parse_coordinates(coord_string: str) -> tuple[int, int, int]:

    """Parse a coordinate string formatted as 'x,y,z' or '(x,y,z)'
    into a tuple of integers."""

    x, y, z = coord_string.split(",")

    return int(x), int(y), int(z)


if __name__ == "__main__":

    print("=== Game Coordinate System ===\n")

    zero_position = (0, 0, 0)

    if len(sys.argv) > 1:

        try:

            if len(sys.argv) == 4 or len(sys.argv) == 2:

                if len(sys.argv) == 4:

                    print(f"Parsing coordinates: {sys.argv[1:]}")

                    parsing_coordinates = ",".join(sys.argv[1:])
                    parsed_position = parse_coordinates(parsing_coordinates)

                elif len(sys.argv) == 2:

                    print(f"Parsing coordinates: \"{sys.argv[1]}\"")
                    parsed_position = parse_coordinates(sys.argv[1])

                print(f"Parsed position: {parsed_position}")

                dist = distance_3d(zero_position, parsed_position)

                print(
                    f"Distance between {zero_position} "
                    f"and {parsed_position}: {dist:.2f}\n"
                )

                print("Unpacking demonstration:")
                x, y, z = parsed_position
                print(f"Player at x={x}, y={y}, z={z}")
                print(f"Coordinates: X={x}, Y={y}, Z={z}")

            else:

                print("Invalid coordinates format,", end=" ")
                print("try one string like ' \"3,4,0\" ',", end=" ")
                print("or 3 values like ' 10 20 5 '")

        except Exception as e:

            print(f"Error parsing coordinates: {e}")
            print(
                f"Error details - Type: "
                f"{type(e).__name__}, Args: {e.args}\n"
            )

    else:

        try:

            player_position = create_position(10, 20, 5)
            print(f"Position created: {player_position}")

            dist = distance_3d(zero_position, player_position)

            print(
                f"Distance between {zero_position} "
                f"and {player_position}: {dist:.2f}\n"
            )

            coord_text = "3,4,0"
            print(f"Parsing coordinates: \"{coord_text}\"")
            player_position = parse_coordinates(coord_text)
            print(f"Parsed position: {player_position}")

            dist2 = distance_3d(zero_position, player_position)

            print(
                f"Distance between {zero_position} "
                f"and {player_position}: {dist2:.1f}\n"
            )

            invalid_text = "abc,def,ghi"
            print(f"Parsing invalid coordinates: \"{invalid_text}\"")

            parse_coordinates(invalid_text)

        except Exception as e:
            print(f"Error parsing coordinates: {e}")
            print(
                f"Error details - Type: "
                f"{type(e).__name__}, Args: {e.args}\n"
            )

        print("Unpacking demonstration:")
        x, y, z = player_position
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
