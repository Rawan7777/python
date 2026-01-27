import sys


print("Program name:", sys.argv[0])

if len(sys.argv) == 1:
    print("No arguments provided")
else:
    i = 1
    while i < len(sys.argv):
        print(f"Arguments {i}: {sys.argv[i]}")
        i += 1
