#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    print("=== Command Quest ===")

    program_name = sys.argv[0]
    total_args = len(sys.argv)

    if total_args == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {total_args}")
    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {total_args - 1}")

        i = 1
        while i < total_args:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

        print(f"Total arguments: {total_args}")
