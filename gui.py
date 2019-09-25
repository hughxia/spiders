import tkinter as tk


window = tk.Tk()
window.title("my window")
window.geometry('200x100')

var = tk.StringVar()
lbl = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12),
            width=12, height=2)
lbl.pack()

on_hit = False

def hit_me():
    global on_hit
    if not on_hit:
        var.set('you hit me')
    else:
        var.set('')
    on_hit = not on_hit

btn = tk.Button(window, text='hit me', width=8, height=2, command=hit_me)
btn.pack()

window.mainloop()