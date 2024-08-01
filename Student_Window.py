from tkinter import *
import sqlite3


class Student_window:

    def __init__(self, master):
        self.master = master


    def create_data(self, master, button):
        if button == "create":
            CreateFunction(self.master, )
        elif button == "update":
            UpdateFunction(self.master)
        elif button == "read":
            ReadFunction(self.master)
        elif button == "delete":
            DeleteFunction(self.master)
        self.clear(master)

    def crud_widgets(self, master):
        # Button
        master.create = Button(text="Create", width=12,
                               command=lambda: self.create_data(master=master, button="create"))
        master.create.place(x=200, y=250)

        master.update = Button(text="Update", width=12,
                               command=lambda: self.create_data(master=master, button="update"))
        master.update.place(x=300, y=250)

        master.read = Button(text="Read", width=12,
                             command=lambda: self.create_data(master=master, button="read"))
        master.read.place(x=400, y=250)

        master.delete = Button(text="Delete", width=12,
                               command=lambda: self.create_data(master=master, button="delete"))
        master.delete.place(x=500, y=250)


    def clear(self, master):
        master.create.destroy()
        master.update.destroy()
        master.read.destroy()
        master.delete.destroy()


class CreateFunction:
    def __init__(self, master, read_function_instance=None):
        self.master = master
        self.read_function_instance = read_function_instance

        # Labels:
        self.name_label = Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=20, pady=10, sticky="e")

        self.student_number_label = Label(master, text="Student number:")
        self.student_number_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")

        self.department_label = Label(master, text="Course:")
        self.department_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")

        # Inputs:
        self.name_entry = Entry(master)
        self.name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        self.student_number_entry = Entry(master)
        self.student_number_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        self.department_entry = Entry(master)
        self.department_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Buttons:
        self.create_button = Button(master, text="Create", command=self.insert_and_update)
        self.create_button.grid(row=3, column=0, columnspan=1, padx=20, pady=20)

        self.cancel_button = Button(master, text="Cancel")
        self.cancel_button.grid(row=3, column=1, columnspan=1, padx=20, pady=20)

        if self.read_function_instance:
            # Bind the create_button to the insert_and_update method if ReadFunction instance is provided
            self.create_button.config(command=self.insert_and_update)

    # def clear_create(self):
    #     print("")
    #
    # def cancel_operation(self):
    #     lecturer_window_instance = Lecturer_window(self.master)
    #     lecturer_window_instance.crud_widgets(self.master)


    def insert_and_update(self):
        # Retrieve data from Entry widgets
        name = self.name_entry.get()
        student_number = self.student_number_entry.get()
        department = self.department_entry.get()

        # Insert data into the database
        self.insert_data(name, student_number, department)

        if self.read_function_instance:
            self.read_function_instance.read_data()

    def insert_data(self, n, id, d):
        connection = sqlite3.connect('management_system.db')
        cursor = connection.cursor()

        cursor.execute("INSERT INTO students VALUES (Null, ?, ?, ?)", (n, id, d))
        connection.commit()


class UpdateFunction:
    def __init__(self,master):
        self.master = master


        # Labels:
        self.name_label = Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=20, pady=10, sticky="e")

        self.student_number_label = Label(master, text="Student Number:")
        self.student_number_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")

        self.department_label = Label(master, text="Course:")
        self.department_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")

        self.id_label = Label(master, text="student ID:")
        self.id_label.grid(row=3, column=0, padx=20, pady=10, sticky="e")

        # Inputs:

        self.name_entry = Entry(master)
        self.name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        self.student_number_entry = Entry(master)
        self.student_number_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        self.department_entry = Entry(master)
        self.department_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        self.id_entry = Entry(master)
        self.id_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        # Buttons:
        self.create_button = Button(master, text="Update")
        self.create_button.grid(row=4, column=0, columnspan=1, padx=20, pady=20)

        self.cancel_button = Button(master, text="Cancel")
        self.cancel_button.grid(row=4, column=1, columnspan=1, padx=20, pady=20)



        # Bind the update_button to the update_table method
        self.create_button.config(command=self.update_table)

    def update_table(self):
        name = self.name_entry.get()
        student_number = self.student_number_entry.get()
        department = self.department_entry.get()
        lecturer_id = self.id_entry.get()
        self.update_database(name, student_number, department, lecturer_id)

    def update_database(self, n, sn, c, id):
        connection = sqlite3.connect("management_system.db")
        cursor = connection.execute("UPDATE students SET name=?, student_number=?,"
                                    " course=? WHERE id=?", (n, sn, c, id))
        connection.commit()


class ReadFunction:
    def __init__(self, master):
        self.master = master
        self.plist = Listbox(self.master, height=20, width=50)
        self.plist.grid(row=1, column=2, pady=20, padx=20)
        self.read_data()

    def read_data(self):
        connection = sqlite3.connect('management_system.db')
        cursor = connection.execute("SELECT * from students")
        rows = cursor.fetchall()
        self.plist.delete(0, END)

        for row in rows:
            self.plist.insert(END, row)
        connection.close()


class DeleteFunction:
    def __init__(self, master):
        self.master = master

        # Labels:
        self.name_label = Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=20, pady=10, sticky="e")

        self.student_number_label = Label(master, text="Student Number:")
        self.student_number_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")

        self.department_label = Label(master, text="Course:")
        self.department_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")

        self.id_label = Label(master, text="student_ID:")
        self.id_label.grid(row=3, column=0, padx=20, pady=10, sticky="e")

        # Inputs:
        self.name_entry = Entry(master)
        self.name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        self.student_number_entry = Entry(master)
        self.student_number_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        self.department_entry = Entry(master)
        self.department_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        self.id_entry = Entry(master)
        self.id_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        # Buttons:
        self.create_button = Button(master, text="Delete")
        self.create_button.grid(row=4, column=0, columnspan=1, padx=20, pady=20)

        self.cancel_button = Button(master, text="Cancel")
        self.cancel_button.grid(row=4, column=1, columnspan=1, padx=20, pady=20)

        self.create_button.config(command=self.delete_data)

    def delete_data(self):
        id_to_delete = self.id_entry.get()
        id_to_delete = int(id_to_delete)
        self.delete_data_database(id_to_delete)


    def delete_data_database(self, id_to_delete):
        connection = sqlite3.connect("management_system.db")
        cursor = connection.execute("DELETE FROM students WHERE id=?", (id_to_delete,))
        connection.commit()
