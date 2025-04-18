# Step 1-3: Try to open and read the file, handle errors if file not found
try:
    with open("sample.txt", "r") as file:
        print("File contents:\n")
        # Step 2: Print content line by line
        for line in file:
            print(line.strip())  # .strip() removes extra newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
