try:
    x = 10 / 0  # This raises ZeroDivisionError
except ValueError:
    print("Caught a ValueError!")
finally:
    print("This always runs!")
