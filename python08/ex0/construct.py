import os
import site
import sys


# Check if Python is running inside a virtual environment
def in_virtualenv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    # Absolute path of the Python interpreter executing this script
    python_path = sys.executable

    # Print a status message depending on environment detection
    print(
        "MATRIX STATUS:",
        "Welcome to the construct\n"
        if in_virtualenv()
        else "You're still plugged in\n",
    )

    # Show which Python binary is currently running
    print(f"Current Python: {python_path}")

    # If running inside a virtual environment
    if in_virtualenv():

        # Extract the virtual environment folder name from its path
        venv_name = os.path.basename(sys.prefix)

        # Display virtual environment information
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}\n")

        # Explain why using a venv is good practice
        print("SUCCESS: You're in an isolated environment!")
        print(
            "Safe to install packages without affecting the global system.\n"
        )

        # Try to show where packages will be installed
        print("Package installation path:")
        try:
            # getsitepackages() may not exist in some environments
            print(site.getsitepackages()[0])
        except Exception:
            # Fallback message if the path cannot be determined
            print("Could not determine site-packages path.")

    else:
        # User is running Python globally (not recommended for projects)
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        # Provide instructions to create a virtual environment
        print("To enter the construct, run:")
        print("python -m venv matrix_env")

        # Activation command differs depending on the OS
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows\n")

        print("Then run this program again.")


# Ensure main() runs only when the script is executed directly
if __name__ == "__main__":
    main()
