import tkinter as tk
import tkinter.font as tkFont
import AppOpener as app
import subprocess, os, platform
def textEditor():
    root = tk.Tk()

    root.title('Personal Journal Entry')
    root.geometry("600x600")

    journal = []
    # Create the menu: THis will contain 'File' 'Format' 'search'
    menu = tk.Menu(root)
    root.configure(menu=menu)
    root.configure(background="#2C5F2D")
    file_menu = tk.Menu(menu, tearoff=0, foreground="pink", background="#5c9aef")
    label = tk.Label(root, text="Personal Journal 🤠", font=("Georgia",32), background="#97BC62", foreground="#2C5F2D")
    label.pack(padx=5, pady=10)
    menu.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="New", command=lambda: textEditor())
    file_menu.add_command(label="Open", command=lambda: textEditor())
    file_menu.add_separator()

    format_menu = tk.Menu(menu, tearoff=0, foreground="pink", background="#5c9aef")
    bold_sub_menu = tk.Menu(format_menu, tearoff=0, foreground="#5c9aef")
    format_menu.add_cascade(label="Bold", menu=bold_sub_menu)
    bold_sub_menu.add_radiobutton(label="Bold On", value="on", command=lambda: print("hello"))
    bold_sub_menu.add_radiobutton(label="Bold Off", value="off", command=lambda: print("Bye"))

    italic_sub_menu = tk.Menu(format_menu, tearoff=0, foreground="#5c9aef")
    format_menu.add_cascade(label="Italics", menu=italic_sub_menu)
    italic_sub_menu.add_radiobutton(label="Italics On", value="on1", command=lambda: print("hello"))
    italic_sub_menu.add_radiobutton(label="Italics Off", value="off1", command=lambda: print("Bye"))

    underline_sub_menu = tk.Menu(format_menu, tearoff=0, foreground="#5c9aef")
    format_menu.add_cascade(label="Underline", menu=underline_sub_menu)
    underline_sub_menu.add_radiobutton(label="Underline On", value="on2", command=lambda: print("hello"))
    underline_sub_menu.add_radiobutton(label="Underline Off", value="off2", command=lambda: print("Bye"))

    def font_menu():
        fonts = list(tkFont.families())
        fonts.sort()
        #print(fonts)
        listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        for font in fonts:
            listbox.insert('end', font)

        listbox.place(x=100, y=20)

        def font_chooser(event):
            our_font.configure(
                family=listbox.get(listbox.curselection())
            )
            listbox.destroy()

        listbox.bind('<ButtonRelease>', font_chooser)

    def font_size_menu():
        font_size = [2, 8, 12, 14, 16, 18, 24, 32, 48, 64, 96, 128]
        listbox = tk.Listbox(root, selectmode=tk.SINGLE)  # 'select mode' controls how many objects can be selected [
        # SINGLE, EXTENDED, e.t.c]

        i = 0
        while i < len(font_size):
            listbox.insert('end', str(font_size[i]))  # Always make sure to add the 'end' index in the
            # front
            i += 1
        listbox.place(x=100, y=20)

        def font_chooser(event):
            our_font.configure(
                size=int(listbox.get(listbox.curselection()))
            )
            listbox.destroy()

        listbox.bind('<ButtonRelease>', font_chooser)  # This carries out the function called after the given command

    def font_color_menu():
        font_color = ['Red', 'Green', 'Blue', 'Brown', 'Yellow', 'Black', 'White', 'Orange', 'Gray', 'Pink', 'Purple',
                      'Olive', 'Gold', 'Cyan']
        listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        i = 0
        while i < len(font_color):
            listbox.insert('end', str(font_color[i]))
            i += 1
        listbox.place(x=100, y=20)

        def color_chooser(event):
            text.configure(
                foreground=(listbox.get(listbox.curselection()))
            )
            listbox.destroy()

        listbox.bind('<ButtonRelease>', color_chooser)



    # font_sub_menu = tk.Menu(format_menu)
    format_menu.add_command(label="Font", command=font_menu)

    format_menu.add_command(label="Font-Size", command=font_size_menu)

    format_menu.add_command(label="Font-Color", command=font_color_menu)

    format_menu.add_separator()

    search_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Format", menu=format_menu)
    menu.add_cascade(label="Search", menu=search_menu)

    # Frame for the text box
    frame = tk.Frame(root, width=510, height=900)
    frame.pack(pady=10)

    # Set the font attributes to 'our_font' so it can be configured/ manipulated in the functions above
    our_font = tkFont.Font(family="Helvetica", size=12, )

    #  Freeze frame in place
    frame.propagate(False)
    frame.columnconfigure(0, weight=10)

    text = tk.Text(frame, font=our_font, background="#e6fbf2",)
    text.pack()

    def get_words():
        journal.append(text.get("1.0", tk.END))
        #print(text.get("1.0", tk.END))

        for word in journal:
            print(word)
            with open('Journal.txt','w') as f:
                f.write(word+'\n')

    def open_words():
        app.open("Notepad")
        subprocess.check_call(('open', 'Journal.txt'))

    get_text = tk.Button(root, text="Save", command=lambda: get_words())
    get_text.place(x=740, y=680)

    open_text = tk.Button(root, text="Open Journal", command=lambda: open_words())
    open_text.place(x=840, y=680)

    root.mainloop()


