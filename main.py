import tkinter as tk
from srt_generator import generate_srt

def handle_generate_button_click(event):
    """Get all fields and generate the srt file"""
    text = text_box.get("1.0", tk.END)
    filename = f"{filename_text_box.get()}"
    pathname = generate_srt(text, filename)
    done(pathname)

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

    window.mainloop()