with open("test.txt", "rb") as f: # with whence=1 or negative offsets, you need to open the file in binary mode ("rb")
    # 1️⃣ Move to 6th byte from start
    f.seek(6, 0)  # from start
    print("From start:", f.read(5))  # b'World'

    # 2️⃣ Move 6 bytes forward from current position
    f.seek(6, 1)  # from current
    print("From current:", f.read(3))  # b'File '

    # 3️⃣ Move 7 bytes back from end
    f.seek(-7, 2)  # from end
    print("From end:", f.read())  # b'Handling'

# output:
    # From start: b'world'
    # From current: b'and'
    # From end: b'\nWorld\n'