from tkinter import *
from tkinter import messagebox 
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

circle_img = Image.open("./assets/circle.png")
resize_circle = circle_img.resize((160, 160))
CIRCLE= ImageTk.PhotoImage(resize_circle)

cross_img = Image.open("./assets/cancel.png")
resize_cross = cross_img.resize((160, 160))
CROSS = ImageTk.PhotoImage(resize_cross)

white_img = Image.open("./assets/white.png")
resize_white = white_img.resize((160, 190))
WHITE = ImageTk.PhotoImage(resize_white)


def button_function(loc):
    row = loc//WIDTH
    col = loc%WIDTH
    clicked_button = BUTTON_LIST[loc]
    global TURN;
    if TURN:
        clicked_button.configure(image=CIRCLE)
        clicked_button.img = CIRCLE
        GAME_MATRIX[row][col] = CIRCLE_SYMBOL
    else:
        clicked_button.configure(image=CROSS)
        clicked_button.img = CROSS
        clicked_button.update()
        GAME_MATRIX[row][col] = CROSS_SYMBOL
    clicked_button["state"] = "disabled"
    window.update_idletasks()
    if is_win():
        win_condition()
    TURN = not TURN

def check_rows():
    for r in range(HEIGHT):
        result = True
        row = GAME_MATRIX[r]
        for c in range(1,WIDTH):
            if row[c-1] != row[c] or row[c]=='':
                result = False
        if result:
            return result
    return False 

def check_cols():
    for c in range(WIDTH):
        result = True
        for r in range(1,HEIGHT):
            if GAME_MATRIX[r-1][c] != GAME_MATRIX[r][c] or GAME_MATRIX[r][c]=='':
                result = False
        if result:
            return result
    return False


def check_diag():
    result = True
    for i in range(1, HEIGHT):
        if GAME_MATRIX[i-1][i-1] != GAME_MATRIX[i][i] or GAME_MATRIX[i][i] == '':
            result = False
    if result:
        return True
    else:
        result = True
        for i in range(1,HEIGHT):
            if GAME_MATRIX[i-1][HEIGHT-i-2] == GAME_MATRIX[i][HEIGHT-i-1] or GAME_MATRIX[i][HEIGHT-i-1] == '':
                result = False
        if result:
            return True
    return result


def is_win():
    return check_rows() or check_cols() or check_diag()


def win_condition():
    global TURN
    if TURN:
        messagebox.showinfo("showinfo", "Player 1 Won")
    else:
        messagebox.showinfo("showinfo", "Player 2 Won")


Grid.rowconfigure(window,0,weight=1)
Grid.rowconfigure(window,1,weight=1)
Grid.rowconfigure(window,2,weight=1)
Grid.columnconfigure(window,0,weight=1)
Grid.columnconfigure(window,1,weight=1)
Grid.columnconfigure(window,2,weight=1)

loc = 0
for i in range(HEIGHT): #Rows
    for j in range(WIDTH): #Columns
        b = Button(window, text="", highlightthickness=0, command=lambda m=loc: button_function(m), image=WHITE)
        b.config(height=15, width=15)
        b.grid(row=i, column=j, sticky='nesw')
        BUTTON_LIST.append(b)
        loc +=1

window.resizable(False,False)
window.mainloop()