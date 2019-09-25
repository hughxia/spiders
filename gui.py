import tkinter as tk


window = tk.Tk()
window.title("my window")
window.geometry('200x100')

lbl = tk.Label(window, text='H-H', bg='blue', font=('Arial', 12),
            width=12, height=2)
lbl.pack()

window.mainloop()