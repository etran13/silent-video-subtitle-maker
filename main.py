import tkinter as tk
from pathlib import Path

class Timestamp:
    def __init__(self, hrs=0, mins=0, secs=00.000):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs

    def __str__(self):
        return f"{self.hrs:02}:{self.mins:02}:{self.secs:06.3f}".replace(".", ",")
    
    def add(self, number):
        "Takes in a number in seconds and adds it to the timestamp."
        seconds = self.secs + number
        #print(f"Seconds: {seconds}")
        if seconds < 60:
            #print("Less than")
            self.secs = seconds
            return
        else:
            carryover = seconds // 60
            remainder = seconds - (carryover * 60)
            #print(f"Carryover: {carryover}, Remainder: {remainder}")
            self.secs = remainder
            self.mins += int(carryover)

    def convert_to_secs(self):
        "Converts the timestamp to seconds (purely for testing)"
        return self.secs + (self.mins * 60) + (self.hrs * 60 * 60)

def handle_generate_button_click(event):
    """Get all fields and generate the vtt file"""
    text = text_box.get("1.0", tk.END)
    filename = f"{filename_text_box.get()}"

    handle(text, filename)

def handle(text, filename):
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
    done(pathname_string)

def done(pathname):
    "Shows a popup when file is done generating"
    status_label.config(text=f"✓ File saved to {pathname}")
    window.after(3000, lambda: status_label.config(text=""))  # clear after 3 sec

if __name__ == "__main__":
    window = tk.Tk()

    options_frame = tk.Frame()

    enter_script = tk.Label(text="Enter script")
    enter_script.grid(row=0, column=0)

    text_box = tk.Text(bg="WHITE SMOKE")
    text_box.grid(row=1, column=0)

    filename_label = tk.Label(master=options_frame,
        text="Filename")
    filename_label.grid(row=5, column=1)

    filename_text_box = tk.Entry(master=options_frame, 
                                width=30,)
    filename_text_box.insert(0, "script")
    filename_text_box.grid(row=6, column=1)

    options_frame.grid(row=0, column=1)

    generate_button = tk.Button(
        text="Save",
        width=7,
        height=2,
        bg="WHITE SMOKE",
    )
    generate_button.bind("<Button-1>", handle_generate_button_click)
    generate_button.grid(row=1, column=1)

    status_label = tk.Label(master=window, text="", fg="green")
    status_label.grid()

    text_box.get("1.0", tk.END)

    window.mainloop()