from tkinter import *

import Lecturer_Window
import Student_Window
import window_1


# def background(self, color):
#     self.master.color = "#333333"
#
#
# background()
class window2:
    def choice_GUI(self, master):
        master.message = Label(text="Do you want to access student or lecturer data?", font=["Ariel", 15, "bold"], fg="white", bg="black")
        master.message.place(x=180, y=220)

        master.student_button = Button(text="Student", width=12, command=lambda: self.clear(master, "student"), fg="white", bg="black")
        master.student_button.place(x=440, y=275)

        master.lecturer_button = Button(text="Lecturer", width=12, command=lambda: self.clear(master, "lecturer"), fg="white", bg="black")
        master.lecturer_button.place(x=240, y=275)

    def clear(self, master, window_type):
        master.message.destroy()
        master.lecturer_button.destroy()
        master.student_button.destroy()
        if window_type == "student":
            student_window = Student_Window.Student_window(master)
            student_window.crud_widgets(master)
        elif window_type == "lecturer":
            lecture_window = Lecturer_Window.Lecturer_window(master)
            lecture_window.crud_widgets(master)


#
# from tkinter import *
#
# import Lecturer_Window
# import Student_Window
# import window_1
#
#
# class window2:
#     def choice_GUI(self, master):
#         master.message = Label(text="Do you want to access student or lecturer data?", font=["Ariel", 15, "bold"])
#         master.message.place(x=180, y=220)
#
#         master.student_button = Button(text="Student", width=12, command=lambda: self.clear(master, "student"))
#         master.student_button.place(x=440, y=275)
#
#         master.lecturer_button = Button(text="Lecturer", width=12,command=lambda: self.clear(master, "lecturer"))
#         master.lecturer_button.place(x=240, y=275)
#
#     def clear(self, master, window_type):
#         master.message.destroy()
#         master.lecturer_button.destroy()
#         master.student_button.destroy()
#         if window_type == "student":
#             student_window = Student_Window.Student_window(master)
#             student_window.crud_widgets(master)
#         elif window_type == "lecturer":
#             lecture_window = Lecturer_Window.Lecturer_window(master)
#             lecture_window.crud_widgets(master)

