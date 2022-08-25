"""
This is going to be a visualizer for the Fantasy Football Project.

This visualizer doesn't need to be anything crazy.

Core functionality:
1. Take inputs
2. Run the code 
3. Display the outputs
"""

import tkinter as tk
window= tk.Tk()

greeting = tk.Label(text="Hello World")
greeting.pack()

label = tk.Label(text="Name")
entry = tk.Entry()

label.pack()
entry.pack()
window.mainloop()
