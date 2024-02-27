import os

class WriteToFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None or 'bug' in open(self.filename).read().lower():
            os.remove(self.filename)

filename = input("Enter the filename (without extension): ") + ".txt"

try:
    with WriteToFile(filename) as file:
        text = input("Enter the text to be written to the file: ")
        file.write(text)

except Exception as e:
    print("An error occurred:", e)

finally:
    if os.path.exists(filename):
        print("\nFile written successfully.")
        print(f"No issue with the file '{filename}' and it is not deleted.")
    else:
        print(f"\nThere is some issue with the file '{filename}' and it is deleted.")