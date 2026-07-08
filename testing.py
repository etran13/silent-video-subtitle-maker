def split(script: str) -> str:
    "Break up the script into chunks"
    return script.split(". ")

def calculate_times(script: list[str]) -> list[chunks]:
    pass

#TODO: Add an option for "preserve period"

if (__name__ == "__main__"):
    r = split("The text: str syntax says that the text argument should be of type str. Similarly, the optional align argument should have type bool with the default value True. Finally, the -> str notation specifies that headline() will return a string.")
    print(r)