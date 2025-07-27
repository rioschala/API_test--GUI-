from tkinter import *
from tkinter import ttk
from functions import *
from ttkthemes import ThemedTk
root = Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)
root.title("API on call button")
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

result_label = ttk.Label(root, text="Waiting...")
result_label.pack(pady=10)
#use lambda to avoid inmediate execution of functions on command when name == main
button = ttk.Button(root, text="Click me to get a no reason", command=lambda: on_button_click(result_label))
button.pack()

root.mainloop()


