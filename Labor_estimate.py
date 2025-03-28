import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askfloat
# import skin
#import sv_ttk

# could try streamlit for simplicity



top = tkinter.Tk()
# # determine size of window
# top.geometry('400x400')

# add widgets below

# quantity of signs
# qty = askfloat("Input", "Enter quantity of signs:")

# dimension of a square piece of vinyl that gets gets installed on a wall.

square_dimension = askfloat("Input", "Enter dimension of indoor vinyl to be installed (in inches)")

# amount payed per hour for worker
num = askfloat("Input", "Enter amount paid to employee:")

# if num == 20:
#     print('you entered 20!')

# labor cost to customer, devide by 60 minutes so you get per minute cost
actual_employee_cost = (num * 2) / 60

# calculate square vinyl dimension:
# for every 10 inches of vinyl, it will take one minute to apply.

time_needed = square_dimension / 10

time_required = time_needed,'minutes for install'

result = (time_needed) * actual_employee_cost

rounded = round(result),'dollars for labor'

print(result,2),'dollars for labor'


# var = StringVar()
# label = Message(top, textvariable=var, relief=RAISED)
# var.set("Hey!? How are you doing?")
# var.set(time_needed)
# label.pack()



tkinter.messagebox.showinfo(title='test', message=time_required)

tkinter.messagebox.showinfo(title='test', message=rounded)


#print('labor cost: ',actual_employee_cost)


#print(num)




# display list of items
# https://www.tutorialspoint.com/python/tk_listbox.htm

# Lb1 = Listbox(top)
# Lb1.insert(1, 'item in listbox')
# Lb1.pack()

# A menubutton is the part of a drop-down menu that stays on the screen all the time.
# Every menubutton is associated with a Menu widget that can display the choices for that menubutton when the user clicks on it.
# https://www.tutorialspoint.com/python/tk_menubutton.htm
# mb= Menubutton ( top, text="condiments", relief=RAISED )
# mb.grid()
# mb.menu = Menu ( mb, tearoff = 0 )
# mb["menu"] = mb.menu

# mayoVar = IntVar()
# ketchVar = IntVar()
# mb.menu.add_checkbutton (label="mayo", variable=mayoVar)
# mb.menu.add_checkbutton (label="ketchup", variable=ketchVar)
# mb.pack()


# button = ttk.Button(top, text="Click me!")
# button.pack()



# Change theme to light or dark
#sv_ttk.set_theme("dark")


# exit tk inter window
top.destroy()
top.mainloop()