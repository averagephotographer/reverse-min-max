import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Reversi - mini-max")
root.iconbitmap("images/icon.ico")


# greeting = tk.Label(text = "Hello there")
label2 = tk.Label(
    fg = "white",
    bg = "green",
    width = 11*10,
    height = 5*10
)

# greeting.pack()
label2.pack()

root.mainloop()
