import tkinter as tk

root = tk.Tk()

root.title("Newline character remover")
icon = tk.PhotoImage(file="/media/data/projects/remove_newline/icon.png")
root.iconphoto(False, icon)

def replace_character(chr, replacement):
    clipboard = root.clipboard_get()
    root.clipboard_clear()
    root.clipboard_append(clipboard.replace(chr, replacement))

def remove_newline_characters():
    replace_character('\n', ' ')

def remove_bullet_points():
    replace_character('•', '')

remove_newline_button = tk.Button(root, text="Remove newline characters", command=remove_newline_characters)
remove_bullets_button = tk.Button(root, text="Remove bullet points", command=remove_bullet_points)
exit_button = tk.Button(root, text="Exit", command=root.destroy)

remove_newline_button.grid(row=0, column=0)
remove_bullets_button.grid(row=0, column=1)
exit_button.grid(row=1, column=0)

root.mainloop()