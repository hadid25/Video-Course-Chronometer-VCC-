import tkinter
import customtkinter

class Table:
    def __init__(self, master):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = tkinter.Entry(master, width=20, fg='blue',font=('Arial',16,'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


# take the data
lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Aaryan', 'Pune', 18),
       (3, 'Vaishnavi', 'Mumbai', 20),
       (4, 'Rachna', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
