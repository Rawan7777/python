#!/usr/bin/env python3

def extract_data() -> None:

    """Establishes a connection to a storage file, reads its contents,
    and prints the recovered data."""

    print("Connection established...\n")

    my_file = None

    try:

        my_file = open(file_name, 'r')

        print("RECOVERED DATA:")
        print(my_file.read())

    except Exception as error:
        print("ERROR: Storage vault not found")
    finally:
        if my_file:
            my_file.close()
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    file_name = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file_name}")
    extract_data()
