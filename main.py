from tkinter import *
from PIL import Image, ImageTk

HEIGHT=3
WIDTH=3
CIRCLE_SYMBOL = "O"
CROSS_SYMBOL = "X"
TURN = True
BUTTON_LIST = []
GAME_MATRIX = [['']*WIDTH for _ in range(HEIGHT)]

window = Tk()
window.title("Tic Tac Toe")
window.minsize(width=500, height=500)

circle_img = Image.open("./assets/circle.jpeg")
resize_circle = circle_img.resize((160, 160))
CIRCLE= ImageTk.PhotoImage(resize_circle)

cross_img = Image.open("./assets/cancel.png")
resize_cross = cross_img.resize((160, 160))
CROSS = ImageTk.PhotoImage(resize_cross)

def button_function(loc):
    row = loc//WIDTH
    col = loc%WIDTH
    clicked_button = BUTTON_LIST[loc]
    global TURN;
    if TURN:
        clicked_button.configure(image=CIRCLE)
        clicked_button.img = CIRCLE
        GAME_MATRIX[row][col] = CIRCLE_SYMBOL
        print("ameno")
    else:
        clicked_button.configure(image=CROSS)
        clicked_button.img = CROSS
        GAME_MATRIX[row][col] = CROSS_SYMBOL
        print("bemeno")
    TURN = not TURN


Grid.rowconfigure(window,0,weight=1)
Grid.rowconfigure(window,1,weight=1)
Grid.rowconfigure(window,2,weight=1)
Grid.columnconfigure(window,0,weight=1)
Grid.columnconfigure(window,1,weight=1)
Grid.columnconfigure(window,2,weight=1)

loc = 0
for i in range(HEIGHT): #Rows
    for j in range(WIDTH): #Columns
        b = Button(window, text="", highlightthickness=0, command=lambda m=loc: button_function(m))
        b.config(height=15, width=15)
        b.grid(row=i, column=j, sticky='nesw')
        BUTTON_LIST.append(b)
        loc +=1

window.resizable(False,False)
window.mainloop()