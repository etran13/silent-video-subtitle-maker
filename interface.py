import tkinter as tk

def handle_generate_button_click(event):
    """Print the character associated to the key pressed"""
    print(text_box.get("1.0", tk.END))

window = tk.Tk()

greeting = tk.Label(text="Paste script")
greeting.pack()

text_box = tk.Text(bg="WHITE SMOKE")
text_box.pack()

generate_button = tk.Button(
    text="Generate",
    width=7,
    height=2,
    bg="WHITE SMOKE",
)
generate_button.bind("<Button-1>", handle_generate_button_click)
generate_button.pack()

text_box.get("1.0", tk.END)

window.mainloop()