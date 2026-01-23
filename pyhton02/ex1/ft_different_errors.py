#!/usr/bin/env python3

def garden_operations():

    my_dict = {"name": "brouane"}
    
    try:
        print("Testing ValueError...")
        x = int("a")
    except ValueError as value_error:
        print(f"Caught ValueError: {value_error}\n")
    
    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError as zero_division_error:
        print(f"Caught ZeroDivisionError: {zero_division_error}\n")
    
    try:
        print("Testing FileNotFoundError...")
        my_file = open("missing.txt")
    except FileNotFoundError as file_not_found_error:
        print(f"Caught FileNotFoundError: {file_not_found_error}\n")
    
    try:
        print("Testing KeyError...")
        print(my_dict["age"])
    except KeyError as key_error:
        print(f"Caught KeyError: {key_error}\n")
    
    try:
        print("Testing multiple errors together...")
        x = int("a")
        10 / 0
        print(my_dict["age"])
        my_file = open("missing.txt")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as key_error:
        print(f"Caught KeyError: {key_error}\n")
    

def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")

if __name__ == "__main__":

    test_error_types()