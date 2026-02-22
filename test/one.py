import sys

# --------------------------
# 1. sys.stdin → reading input
# --------------------------
print("Enter your name:", end=' ')
name = sys.stdin.readline().strip()  # reads one line from standard input
print(f"Hello, {name}!\n")

# --------------------------
# 2. sys.stdout → writing output
# --------------------------
sys.stdout.write("This is written directly to standard output.\n")

# --------------------------
# 3. sys.stderr → writing error messages
# --------------------------
sys.stderr.write("Warning: This is an error message!\n")