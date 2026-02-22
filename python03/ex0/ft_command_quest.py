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

        for i in range(1, total_args):
            print(f"Argument {i}: {sys.argv[i]}")

        print(f"Total arguments: {total_args}")
