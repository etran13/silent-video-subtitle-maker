import tkinter as tk

class Timestamp:
    def __init__(self, hrs=0, mins=0, secs=00.000):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs

    def __str__(self):
        return f"{self.hrs:02}:{self.mins:02}:{self.secs:06.3f}"
    
    def add(self, number):
        "Takes in a number in seconds and adds it to the timestamp."
        seconds = self.secs + number
        print(f"Seconds: {seconds}")
        if seconds < 60:
            print("Less than")
            self.secs = seconds
            return
        else:
            carryover = seconds // 60
            remainder = seconds - (carryover * 60)
            print(f"Carryover: {carryover}, Remainder: {remainder}")
            self.secs += remainder
            self.mins += int(carryover)

def handle_generate_button_click(event):
    """Get all fields and generate the vtt file"""
    text = text_box.get("1.0", tk.END)
    should_preserve = preserve_period_checkbox_var.get()
    should_split = split_long_sentences_checkbox_var.get()
    pathname = f"{pathname_text_box.get()}"
    filename = f"/{filename_text_box.get()}.vtt"

    handle(text, should_preserve, should_split, pathname, filename)

def handle(text, should_preserve, should_split, pathname, filename):
    #Split text into a list of lines
    list_of_lines = text.splitlines()

    #For each line in the list, figure out how long it will take
    current_time = 0.000
    list_of_durations = []
    for line in list_of_lines:
        duration_seconds = len(line) / 17
        start_time = current_time
        end_time = start_time + duration_seconds
        list_of_durations.append((f"{start_time:.3f}", f"{end_time:.3f}"))
        current_time = end_time + 0.001

    #Open file, write everything to file, close file
    print(list_of_lines)
    print(list_of_durations)

if __name__ == "__main__":
    window = tk.Tk()

    options_frame = tk.Frame()

    enter_script = tk.Label(text="Enter script")
    enter_script.grid(row=0, column=0)

    text_box = tk.Text(bg="WHITE SMOKE")
    text_box.grid(row=1, column=0)

    options = tk.Label(master=options_frame, text="Options:\n")
    options.grid(row=0, column=0)

    preserve_period_checkbox_var = tk.BooleanVar()
    preserve_period_checkbox = tk.Checkbutton(master=options_frame,
                                            text="Preserve period",
                                            variable = preserve_period_checkbox_var)
    preserve_period_checkbox.grid(row=1, column=1)

    split_long_sentences_checkbox_var = tk.BooleanVar()
    split_long_sentences_checkbox = tk.Checkbutton(master=options_frame,
                                                text="Split long sentences",
                                                variable = split_long_sentences_checkbox_var)
    split_long_sentences_checkbox.grid(row=2, column=1)

    pathname_label = tk.Label(master=options_frame,
        text="Pathname")
    pathname_label.grid(row=3, column=1)

    pathname_text_box = tk.Entry(master=options_frame, 
                                width=30,)
    pathname_text_box.grid(row=4, column=1)

    filename_label = tk.Label(master=options_frame,
        text="Filename")
    filename_label.grid(row=5, column=1)

    filename_text_box = tk.Entry(master=options_frame, 
                                width=30,)
    filename_text_box.grid(row=6, column=1)

    options_frame.grid(row=0, column=1)

    generate_button = tk.Button(
        text="Generate",
        width=7,
        height=2,
        bg="WHITE SMOKE",
    )
    generate_button.bind("<Button-1>", handle_generate_button_click)
    generate_button.grid(row=1, column=1)

    text_box.get("1.0", tk.END)

    window.mainloop()