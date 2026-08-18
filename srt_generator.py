from pathlib import Path
from timestamp import Timestamp

def generate_srt(text, filename):
    #Split text into a list of lines
    list_of_lines = text.splitlines()

    #For each line in the list, figure out how long it will take
    time = Timestamp()
    list_of_durations = []
    for line in list_of_lines:
        duration_seconds = round(len(line) / 17, 3)
        start_time = str(time)
        time.add(duration_seconds)
        end_time = str(time)
        list_of_durations.append((f"{start_time} --> {end_time}"))
        time.add(0.001)
    
    pathname_string = f"{Path.home()}/Downloads/{filename}.srt"
    with open(pathname_string, "w", encoding="utf-8") as file:
        for i in range(len(list_of_lines)):
            file.write(f"{i + 1}\n")
            file.write(f"{list_of_durations[i]}\n")
            file.write(f"{list_of_lines[i]}\n\n")
    return pathname_string