#
# World McCrea
# 7/12/2024
# Program using Tkinter to build GUIs
#
import tkinter


# import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Grade Calculator')
        self.main_window.geometry('260x125')

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)

        self.button1 = tkinter.Button(self.frame5, text='Calculate',
                                      command=self.calculate)

        self.button2 = tkinter.Button(self.frame5, text='Quit',
                                      command=self.main_window.destroy)

        self.label1 = tkinter.Label(self.frame1, text='Tests Grade:')
        self.tests_entry = tkinter.Entry(self.frame1, width=10)
        self.label1.pack(side='left')
        self.tests_entry.pack(side='left')

        self.label2 = tkinter.Label(self.frame2, text='Labs Grade:')
        self.labs_entry = tkinter.Entry(self.frame2, width=10)
        self.label2.pack(side='left')
        self.labs_entry.pack(side='left')

        self.label3 = tkinter.Label(self.frame3, text='Exams Grade:')
        self.exams_entry = tkinter.Entry(self.frame3, width=10)
        self.label3.pack(side='left')
        self.exams_entry.pack(side='left')

        self.label4 = tkinter.Label(self.frame4, text='Grade Average:')
        self.label4.pack(side='left')

        self.avg_value = tkinter.StringVar()
        self.label5 = tkinter.Label(self.frame4, textvariable=self.avg_value)
        self.label5.pack(side='left')
        self.avg_value.set('(avg )')

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.button1.pack(side='left')
        self.button2.pack(side='left')

        self.main_window.mainloop()

    def calculate(self):
        # figure out weighted grades
        test_w = float(self.tests_entry.get())
        test_w2 = test_w * .20

        labs_w = float(self.labs_entry.get())
        lab_w2 = labs_w * .30

        exams_w = float(self.exams_entry.get())
        exams_w2 = exams_w * .50

        grade_avg = test_w2 + lab_w2 + exams_w2
        self.avg_value.set(f'{grade_avg:.1f}')
        # print(grade_avg)


my_gui = MyGUI()
