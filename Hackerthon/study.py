import tkinter as tk
from tkinter import messagebox
import time

class StudySessionGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Study Session Timer")
        self.geometry("1000x1000")  # Make the window two times bigger
        self.configure(bg="#FAFAD2")  # Light cream background color

        self.study_time = tk.StringVar()
        self.num_of_breaks = tk.StringVar()
        self.time_of_breaks = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self, bg="#FAFAD2")  # Light cream background color
        main_frame.pack(expand=True)

        # Custom font with 3 times bigger size
        custom_font = ("Arial", 20)

        self.label1 = tk.Label(main_frame, text="How long do you want to study today? Please enter the time in minutes:", font=custom_font, bg="#FAFAD2", fg="black")
        self.label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry1 = tk.Entry(main_frame, textvariable=self.study_time, font=custom_font, bg="white", fg="black")
        self.entry1.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = tk.Label(main_frame, text="How many breaks do you want to have?", font=custom_font, bg="#FAFAD2", fg="black")
        self.label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry2 = tk.Entry(main_frame, textvariable=self.num_of_breaks, font=custom_font, bg="white", fg="black")
        self.entry2.grid(row=1, column=1, padx=10, pady=10)

        self.label3 = tk.Label(main_frame, text="How long do you want your breaks to be for? (Enter in minutes)", font=custom_font, bg="#FAFAD2", fg="black")
        self.label3.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry3 = tk.Entry(main_frame, textvariable=self.time_of_breaks, font=custom_font, bg="white", fg="black")
        self.entry3.grid(row=2, column=1, padx=10, pady=10)

        self.start_button = tk.Button(main_frame, text="Start Study Session", font=custom_font, command=self.start_study_session)
        self.start_button.grid(row=3, columnspan=2, padx=10, pady=10)

        # Center the main frame
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

    def start_study_session(self):
        study_time = int(self.study_time.get())
        num_of_breaks = int(self.num_of_breaks.get())
        time_of_breaks = int(self.time_of_breaks.get())

        cycles = num_of_breaks + 1
        time_of_sessions = study_time / cycles

        messagebox.showinfo("Study Session", "Nice! Let's get started with your study session.")

        for cycle in range(cycles):
            messagebox.showinfo("Study Session", f"Session {cycle + 1}: Study for {time_of_sessions} minutes.")
            time.sleep(time_of_sessions * 60)

            messagebox.showinfo("Study Session", f"Now, let's take a break for {time_of_breaks} minutes.")
            time.sleep(time_of_breaks * 60)

        messagebox.showinfo("Congratulations!", "GREAT JOB! YOU COMPLETED YOUR STUDY TIME!")

if __name__ == "__main__":
    root = StudySessionGUI()
    root.mainloop()