#!/usr/bin/env python3

def garden_operations(error_type):
    """
    Raise a specific error based on the given error type.
    param error_type: Type of error to trigger
    """
    my_dict = {"plant": "tomato"}

    if error_type == "value":
        print("Testing ValueError...")
        int("abc")

    elif error_type == "zero":
        print("Testing ZeroDivisionError...")
        10 / 0

    elif error_type == "file":
        print("Testing FileNotFoundError...")
        open("missing.txt")

    elif error_type == "key":
        print("Testing KeyError...")
        print(my_dict["missing_plant"])


def test_error_types():

    """Run tests for different exception types."""

    print("=== Garden Error Types Demo ===")

    for error in ["value", "zero", "file", "key"]:
        try:
            garden_operations(error)

        except ValueError as caught_error:
            print(f"Caught ValueError: {caught_error}")

        except ZeroDivisionError as caught_error:
            print(f"Caught ZeroDivisionError: {caught_error}")

        except FileNotFoundError as caught_error:
            print(f"Caught FileNotFoundError: {caught_error}")

        except KeyError as caught_error:
            print(f"Caught KeyError: {caught_error}")

    try:
        print("Testing multiple errors together...")
        int("abc")

    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
