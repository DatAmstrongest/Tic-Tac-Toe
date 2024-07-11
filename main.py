from tkinter import *

window = Tk()
window.title("Tic Tac Toe")
window.minsize(width=500, height=500)

Grid.rowconfigure(window,0,weight=1)
Grid.rowconfigure(window,1,weight=1)
Grid.rowconfigure(window,2,weight=1)
Grid.columnconfigure(window,0,weight=1)
Grid.columnconfigure(window,1,weight=1)
Grid.columnconfigure(window,2,weight=1)

height=3
width=3
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Button(window, text="")
        b.config(height=15, width=15)
        b.grid(row=i, column=j, sticky='nesw')

window.mainloop()