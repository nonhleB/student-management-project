import window_2
from window_2 import *


class WelcomeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("BC data center")
        self.master.geometry("800x600")
        self.master.configure(bg="gray")
        #self.master.resizeable(False, False)
    def add_widgets(self):

            # Labels:
            self.welcome_message = Label(self.master, text="Welcome to the Belgium Campus data management center", font=["Ariel", 20, "bold"], fg="white", bg="black")
            self.welcome_message.grid(row=0, column=0, padx=10, pady=10)

            self.group_message = Label(self.master, text="Created by XTRA Sauce", font=["Ariel", 10, "bold"], fg="white", bg="black")
            self.group_message.place(x=320, y=340)
            # self.group_message.grid(row=0, column=1, padx=10, pady=10)
            # Button
            self.continue_message = Button(self.master, text="Continue", width=12, command=self.clear, fg="white", bg="black")
            self.continue_message.place(x=320, y=550)



    def clear(self):
        self.welcome_message.destroy()
        self.group_message.destroy()
        self.continue_message.destroy()
        window2_instance = window_2.window2()
        window2_instance.choice_GUI(self.master)

#
# import window_2
# from window_2 import *
#
#
# class WelcomeGUI:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("BC data center")
#         self.master.geometry("800x600")
#
#     def add_widgets(self):
#
#             # Labels:
#             self.welcome_message = Label(self.master, text="Welcome to the Belgium Campus data management center",
#                                          font=["Ariel", 20, "bold"])
#             self.welcome_message.place(x=5, y=290)
#
#             self.group_message = Label(self.master, text="Created by XTRA Sauce", font=["Ariel", 10, "bold"])
#             self.group_message.place(x=320, y=340)
#
#             # Button
#             self.continue_message = Button(self.master, text="Continue", width=12, command=self.clear)
#             self.continue_message.place(x=320, y=550)
#
#     def clear(self):
#         self.welcome_message.destroy()
#         self.group_message.destroy()
#         self.continue_message.destroy()
#         window2_instance = window_2.window2()
#         window2_instance.choice_GUI(self.master)






