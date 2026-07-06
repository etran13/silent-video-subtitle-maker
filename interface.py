import tkinter as tk

def handle_generate_button_click(event):
    """Print the character associated to the key pressed"""
    print(text_box.get("1.0", tk.END))
    if preserve_period_checkbox["text"] != " ":
        print("preserve_period_checkbox checked")
    if split_long_sentences_checkbox["text"] != " ":
        print("split_long_sentences_checkbox checked")

def handle_preserve_period_checkbox(event):
    if preserve_period_checkbox["text"] == " ":
        preserve_period_checkbox.config(text="\u2713")
    else:
        preserve_period_checkbox.config(text=" ")

def handle_split_long_sentences_checkbox(event):
    if split_long_sentences_checkbox["text"] == " ":
        split_long_sentences_checkbox.config(text="\u2713")
    else:
        split_long_sentences_checkbox.config(text=" ")

window = tk.Tk()

options_frame = tk.Frame()

enter_script = tk.Label(text="Enter script")
enter_script.grid(row=0, column=0)

text_box = tk.Text(bg="WHITE SMOKE")
text_box.grid(row=1, column=0)

options = tk.Label(master=options_frame, text="Options:\n")
options.grid(row=0, column=0)

preserve_period = tk.Label(master=options_frame, text="Preserve period")
preserve_period.grid(row=1, column=0)

split_long_sentences = tk.Label(master=options_frame, text="Split long sentences")
split_long_sentences.grid(row=2, column=0)

preserve_period_checkbox = tk.Button(
    master=options_frame,
    text=" ",
    width=1,
    height=1,
    bg="WHITE SMOKE",
)
preserve_period_checkbox.bind("<Button-1>", handle_preserve_period_checkbox)
preserve_period_checkbox.grid(row=1, column=1)

split_long_sentences_checkbox = tk.Button(
    master=options_frame,
    text=" ",
    width=1,
    height=1,
    bg="WHITE SMOKE",
)
split_long_sentences_checkbox.bind("<Button-1>", handle_split_long_sentences_checkbox)
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