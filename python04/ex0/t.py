def extract_data():
    print("Connection established...\n")

    try:
        with open(file_name, 'r') as my_file:
            print("RECOVERED DATA:")
            print(my_file.read())
    except FileNotFoundError as e:
        print(e)
    finally:
        my_file.close()
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    file_name = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file_name}")
    extract_data()