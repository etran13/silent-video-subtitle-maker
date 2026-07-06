import tkinter as tk

def handle_generate_button_click(event):
    """Print the character associated to the key pressed"""
    print(text_box.get("1.0", tk.END))

window = tk.Tk()

enter_script = tk.Label(text="Enter script")
enter_script.grid(row=0, column=0)

text_box = tk.Text(bg="WHITE SMOKE")
text_box.grid(row=1, column=0)

options = tk.Label(text="Options")
options.grid(row=0, column=1)

preserve_period = tk.Label(text="Preserve period")
preserve_period.grid(row=1, column=1)

split_long_sentences = tk.Label(text="Split long sentences")
split_long_sentences.grid(row=2, column=1)

generate_button = tk.Button(
    text="Generate",
    width=7,
    height=2,
    bg="WHITE SMOKE",
)
generate_button.bind("<Button-1>", handle_generate_button_click)
generate_button.grid(row=3, column=1)

text_box.get("1.0", tk.END)

window.mainloop()