import tkinter as tk

root = tk.Tk()

root.title("Newline character remover")
icon = tk.PhotoImage(file="/media/data/projects/remove_newline/icon.png")
root.iconphoto(False, icon)

def remove_newline_characters():
    clipboard = root.clipboard_get()
    root.clipboard_clear()
    root.clipboard_append(clipboard.replace('\n', ' '))

submit_button = tk.Button(root, text="Remove newline characters", command=remove_newline_characters)
exit_button = tk.Button(root, text="Exit", command=root.destroy)

submit_button.grid(row=0, column=0)
exit_button.grid(row=1, column=0)

root.mainloop()