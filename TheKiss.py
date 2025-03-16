import tkinter as tk
import random
from tkinter import messagebox


def move_no_button(event):
    nx = window.winfo_width() - no_button.winfo_width()
    new_x = random.randint(0, nx)
    ny = window.winfo_height() - no_button.winfo_height()
    new_y = random.randint(50 , ny)
    no_button.place(x=new_x, y = new_y)

def show_thank_you():
    messagebox.showinfo("B612" , "COME HEAR ... ")

window = tk.Tk()
window.title("B612")
window.geometry("400x300")


label =tk.Label(window,
                text="CAN I KISS YOU <3 ?",
                font=("vazir bold" , 18),
                )
label.pack(pady = 20)

yes_button = tk.Button(window,
                      text="YES",
                      font=("vazir", 14),
                      command=show_thank_you
                      )
yes_button.pack(side=tk.LEFT, padx=60)

no_button =tk.Button(window,
                      text="NO",
                      font=("vazir", 14))
no_button.place(x=200, y=150)
no_button.bind("<Enter>", move_no_button)

window.mainloop()

