import tkinter as tk
from window_1 import *
from window_2 import *


def main():
    root = tk.Tk()
    window1 = WelcomeGUI(root)
    window1.add_widgets()
    #window2_instance = window2()

    root.mainloop()


if __name__ == "__main__":
    main()
