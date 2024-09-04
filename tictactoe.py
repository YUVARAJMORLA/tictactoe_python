import tkinter

def set_title(row,column):
    global curr_player

    if (game_over):
        return

    if board[row][column]["text"] !="":
        return

    board[row][column]["text"] = curr_player

    if curr_player == player2:
        curr_player = player1
    else:
        curr_player = player2

    label["text"] = curr_player+" 's turn"

    #check winner
    check_winner()

def check_winner():
    global turns,game_over
    turns +=1

    # horizontal checking
    for row in range(3):
        if (board[row][0]["text"]==board[row][1]["text"] ==board[row][2]["text"] and board[row][0]["text"] !=""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground = color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow,background=color_white)
            game_over = True
            return

    #vertical checking
    for column in range(3):
        if(board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] !=""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground = color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow,background=color_white)
            game_over = True
            return

   # diagonal checking and anti diagonal checking
    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] !=""):
            label.config(text=board[0][0]["text"]+" is the winner!", foreground = color_yellow)
            for i in range(3):
                board[i][i].config(foreground=color_yellow,background=color_green)
            game_over = True
            return
    if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] !=""):
            label.config(text=board[0][2]["text"]+" is the winner!", foreground = color_yellow)
            # board[0][2].config(foreground=color_yellow,background=color_orange)
            # board[1][1].config(foreground=color_yellow,background=color_orange)
            # board[2][0].config(foreground=color_yellow,background=color_orange)
            j=2
            for i in range(3):
                board[i][j-i].config(foreground=color_yellow,background=color_orange)
            game_over = True
            return

    # game tie
    if(turns==9):
        game_over=True
        label.config(text="Tie",foreground=color_green)
        return


def new_game():
    global turns,game_over
    turns = 0
    game_over = False

    label.config(text=curr_player+"'s turn",foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="",foreground=color_blue,background=color_black)


# players and game setup

player1 = "X"
player2 = "O"
curr_player = player1
board = [[0,0,0],[0,0,0],[0,0,0]]


# colors

color_blue = "#1f96ee"
color_green = "#57ea24"
color_yellow = "#f2b916"
color_black =  "#000000"
color_white =  "#ededed"
color_orange = "#fc6616"
color_cherryred = "#e61155"

turns = 0
game_over = False

# window setup
window = tkinter.Tk ()
window.title("Tic Tac Toe")
window.resizable(False,False)


# keeping frame in window
frame = tkinter.Frame(window)
label = tkinter.Label(frame,text=curr_player+"'s turn",font=("Consolas",20),background=color_black,foreground="white")
label.grid(row=0,column=0,columnspan=3,sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame,text="",font=("Consolas",50,"bold"),background=color_black,foreground=color_blue,width=4,height=1,command=lambda row=row, column=column: set_title(row,column))

        board[row][column].grid(row=row+1,column=column)

button = tkinter.Button(frame,text="restart",font=("Consolas",20),background=color_black,foreground="white",command=new_game)

button.grid(row=4,column=0,columnspan=3,sticky="we")
frame.pack()

# keep the window in center
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))

# format (w) x (h) + (x) + (y)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()


# pip install pyinstaller
# pyinstaller --onefile tictactoe.py
