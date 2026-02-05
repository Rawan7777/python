def create_data():

    try:
        with open(file_name, 'w') as my_file:
            my_file.write("[ENTRY 001] New quantum algorithm discovered\n[ENTRY 002] Efficiency increased by 347%\n[ENTRY 003] Archived by Data Archivist trainee")
            print("Storage unit created successfully...\n")
        
        with open(file_name, 'r') as my_file:
            print("Inscribing preservation data...")
            print(my_file.read())

    except FileNotFoundError as e:
        print(e)
    finally:
        print("\nData inscription complete. Storage unit sealed.")


if __name__ == "__main__":

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    file_name = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_name}")
    create_data()
    print(f"Archive '{file_name}' ready for long-term preservation.")
