from tkinter import *
from tkinter import ttk
from functions import *
root = Tk()
root.title("API on call button")

result_label = ttk.Label(root, text="Waiting...")
result_label.pack(pady=10)
button = ttk.Button(root, text="Click me to get a no reason", command=lambda: on_button_click(result_label))
button.pack()

root.mainloop()


