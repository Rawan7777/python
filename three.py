try:
    print("Trying to water plants...")
    plant = None
    if not plant:
        print("Error: No plant to water!")
except ValueError:
    print("Caught a ValueError!")
else:
    print("Watering successful!")
finally:
    print("Closing watering system (cleanup)")
