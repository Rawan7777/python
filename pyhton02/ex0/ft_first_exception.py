#!/usr/bin/env python3

def check_temperature(temp_str: str):

    print("Testing temperature:", temp_str)
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
    else:
        if temp >= 0 and temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!\n")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")

if __name__ == "__main__":

    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")

    print("All tests completed - program didn't crash!")