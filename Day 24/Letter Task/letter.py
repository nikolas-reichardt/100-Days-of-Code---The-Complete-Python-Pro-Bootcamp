import os


class Letter():
    DIR = os.path.dirname(__file__)  # Directory of the current script
    PATH = os.path.join(DIR, "starting_letter.txt")
    print(PATH)

    def __init__(self) -> None:
        try:
            # Attempt to open and read the file
            with open(self.PATH, "r") as file:
                self.content = file.read()
                # Check if the file content is empty
                if not self.content:
                    raise ValueError("File is empty.")
        except FileNotFoundError:
            # This will catch the case where the file doesn't exist
            print(f"Error: The file at '{self.PATH}' was not found.")

        except ValueError as e:
            # This will catch the case where the file is empty or has invalid data
            print(f"Error: {e}")