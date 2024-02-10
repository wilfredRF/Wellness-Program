import tkinter as tk
import tkinter.font as tkFont
import random

from PIL import ImageTk
from study import *
import webview
from journal import *


# This is the home screen of the wellness app

root = tk.Tk()

root.geometry("400x500")
root.title("Wellness Program")

def resources():
    webview.create_window('Geeks for Geeks', 'https://www.mcneese.edu/campus-life/rec/wellness-program')
    webview.start()

def resources1():
    webview.create_window('Geeks for Geeks', 'https://www.lcmh.com/')
    webview.start()
def home_page(username):
    for widgets in root.winfo_children():
        widgets.destroy()
    print("Hey " + username.get())
    greetings = username.get()
    bg_home = tk.PhotoImage(file="Wellness/meditate8 (1).png")  # Suitable size: W x H: 1540 x 1040 px

    journal = tk.PhotoImage(file="Wellness/study.png")

    quote = tk.PhotoImage(file="Wellness/quote.png")

    studying = tk.PhotoImage(file="Wellness/journal.png")

    background_home = tk.Label(root, image=bg_home)

    background_home.place(relheight=1, relwidth=1)

    # Text: 'Hello, what's your name?'

    text = tk.Label(root, text=" Hello "+greetings+" ", font=("Pristina", 40), background="#2C5F2D",
                    foreground="#97BC62", borderwidth=1, relief="raised")
    text.pack(padx=5, pady=15)

    text1 = tk.Label(root, text=" What would you like to do today 😄 ", font=("Pristina", 40), background="#2C5F2D",
                    foreground="#97BC62", borderwidth=1, relief="raised")
    text1.pack(padx=5, pady=15)

    memoir_button = tk.Button(root, text=" Personal Journal  😸 ", command= lambda: textEditor())
    memoir_button.place(x=240, y=680)

    quote_button = tk.Button(root, text=" Mental-health Resources (On-Campus) 😇 ", command= lambda: resources())
    quote_button.place(x=680, y=680)

    quote_button1 = tk.Button(root, text=" Mental-health Resources (Off-Campus) 😇 ", command=lambda: resources1())
    quote_button1.place(x=680, y=740)

    study_button = tk.Button(root, text=" Study 🤩 ")
    study_button.place(x=1280, y=680)

    memoir_img = tk.Label(root, image=journal,width=400, height=350)

    quote_img = tk.Label(root, image=quote, width=400, height=350)

    study_img = tk.Label(root, image=studying, width=400, height=350)

    memoir_img.place(x=110, y=320)
    quote_img.place(x=610, y=320)
    study_img.place(x=1110, y=320)

    root.mainloop()


def switch(page):
    page()

# Background image

bg = tk.PhotoImage(file="Wellness/meditate9 (1).png")  # Suitable size: W x H: 1540 x 1040 px

background = tk.Label(root, image=bg)

background.place(relheight=1, relwidth=1)

# Text: 'Hello, what's your name?'

text = tk.Label(root, text=" Hello, what's your name? ", font=("Pristina", 40), background="#2C5F2D",
                foreground="#97BC62", borderwidth=1, relief="raised")
text.pack(padx=5, pady=15)

# Frame for the name input and next button
name_box = tk.Frame(root, bg="#2C5F2D", borderwidth=1, relief="raised")

# Collect name
user_name = tk.StringVar()
name = tk.Entry(name_box, font=("Pristina"), textvariable=user_name)
name.grid(padx=5, pady=5, row=0, column=0)

# Next button

next_button = tk.Button(name_box, text="Next", command=lambda: switch(home_page(user_name)))
next_button.grid(padx=5, pady=5, row=0, column=1)

name_box.pack()
root.mainloop()
