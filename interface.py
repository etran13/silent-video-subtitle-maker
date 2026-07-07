import tkinter as tk

def handle_generate_button_click(event):
    """Print the character associated to the key pressed"""
    print(text_box.get("1.0", tk.END))
    if preserve_period_checkbox_var.get():
        print("Preserve period")
    if split_long_sentences_checkbox_var.get():
        print("Split long sentences")

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