
import sys
import os
import site

def in_virtualenv() -> bool:
    return sys.prefix != sys.base_prefix

def main() -> None:

    python_path = sys.executable

    print("MATRIX STATUS:", "Welcome to the construct\n" if in_virtualenv() else "You're still plugged in\n")
    print(f"Current Python: {python_path}")

    if in_virtualenv():

        venv_name = os.path.basename(sys.prefix)

        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.\n")
        print("Package installation path:")
        print(site.getsitepackages()[0])

    else:

        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows\n")
        print("Then run this program again.")

if __name__ == "__main__":
    main()
