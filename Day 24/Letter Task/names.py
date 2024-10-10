import os


class Names():
    DIR = os.path.dirname(__file__)  # Directory of the current script
    PATH = os.path.join(DIR, "invited_names.txt")
    print(PATH)

    def __init__(self) -> None:
        try:
            # Attempt to open and read the file
            with open(self.PATH, "r") as file:
                self.names = file.readlines()
                print(self.names)
                # Check if the file content is empty
                if not self.names:
                    raise ValueError("File is empty.")
                 # Strip the newline characters and update the list
                self.names = [line.strip("\n") for line in self.names]
                print(self.names)
        except FileNotFoundError:
            # This will catch the case where the file doesn't exist
            print(f"Error: The file at '{self.PATH}' was not found.")

        except ValueError as e:
            # This will catch the case where the file is empty or has invalid data
            print(f"Error: {e}")