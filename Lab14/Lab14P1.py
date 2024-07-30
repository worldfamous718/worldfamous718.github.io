#
# World McCrea
# 7/12/2024
# Program using Tkinter to build GUI
#

import tkinter
from tkinter import messagebox


class MyGUI:
    # format the main window
    def __init__(self):
        # self.grade_avg = None
        self.main_window = tkinter.Tk()
        self.main_window.title('Grade Calculator')
        self.main_window.geometry('260x125')

        # Frame 1 contents Tests
        self.frame1 = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.frame1, text='Tests Grade:')
        self.tests_entry = tkinter.Entry(self.frame1, width=10)
        self.label1.pack(side='left')
        self.tests_entry.pack(side='left')

        # Frame 2 contents Labs
        self.frame2 = tkinter.Frame(self.main_window)
        self.label2 = tkinter.Label(self.frame2, text='Labs Grade:')
        self.labs_entry = tkinter.Entry(self.frame2, width=10)
        self.label2.pack(side='left')
        self.labs_entry.pack(side='left')

        # Frame 3 contents Exams
        self.frame3 = tkinter.Frame(self.main_window)
        self.label3 = tkinter.Label(self.frame3, text='Exams Grade:')
        self.exams_entry = tkinter.Entry(self.frame3, width=10)
        self.label3.pack(side='left')
        self.exams_entry.pack(side='left')

        # Frame 4 contents and StringVar setting
        self.frame4 = tkinter.Frame(self.main_window)
        self.label4 = tkinter.Label(self.frame4, text='Grade Average:')
        self.label4.pack(side='left')
        self.avg_value = tkinter.StringVar()
        self.label5 = tkinter.Label(self.frame4, textvariable=self.avg_value)
        self.label5.pack(side='left')
        self.avg_value.set('(avg )')

        # Frame 5 contents. Calc and Quit buttons
        self.frame5 = tkinter.Frame(self.main_window)
        self.button1 = tkinter.Button(self.frame5, text='Calculate',
                                      command=self.calculate)
        self.button2 = tkinter.Button(self.frame5, text='Quit',
                                      command=self.main_window.destroy)

        # Unpack my frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.button1.pack(side='left')
        self.button2.pack(side='left')

        # call the main loop
        self.main_window.mainloop()

    # callback functions, logic, and exception handling
    def calculate(self):
        try:
            # convert user entry to floats
            test_input = float(self.tests_entry.get())
            labs_input = float(self.labs_entry.get())
            exams_input = float(self.exams_entry.get())

            # convert grade_avg to an object. so I can use it in my class
            self.grade_avg = (test_input * 0.20) + (labs_input * 0.30) + (exams_input * 0.50)
            self.format_grades()  # add the letter grades
        except ValueError:
            messagebox.showerror('Numbers Only!')  # I cant figure out how to make the error box bigger

    # format snd logic for the letter grades
    def format_grades(self):
        grade_avg = self.grade_avg
        letter_grade = 'A'
        if grade_avg > 90:
            letter_grade = 'A'
        elif grade_avg >= 80:
            letter_grade = 'B'
        elif grade_avg >= 70:
            letter_grade = 'C'
        elif grade_avg >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'

        # get the letter grade next to the number grade
        self.avg_value.set(f'{grade_avg:.1f} ({letter_grade})')


my_gui = MyGUI()
