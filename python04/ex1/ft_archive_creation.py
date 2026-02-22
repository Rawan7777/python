#!/usr/bin/env python3

def create_data() -> None:

    """Write sample entries to a file and display its contents."""

    try:
        
        read_file = None
        read_file = open(file_name, 'w')

        read_file.write(
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee"
            )

        read_file.close()
        print("Storage unit created successfully...\n")

        write_file = None
        write_file = open(file_name, 'r')

        print("Inscribing preservation data...")
        print(write_file.read())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if read_file:
            read_file.close()
        if write_file:
            write_file.close()
        
        print("\nData inscription complete. Storage unit sealed.")


if __name__ == "__main__":

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    file_name = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_name}")
    create_data()
    print(f"Archive '{file_name}' ready for long-term preservation.")
