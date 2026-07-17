import tkinter as tk
import string_processing as sp

def handle_generate_button_click(event):
    """Generate the vtt file"""
    text = text_box.get("1.0", tk.END)
    should_preserve = preserve_period_checkbox_var.get()
    should_split = split_long_sentences_checkbox_var.get()
    filename = f""

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