from tkinter import Toplevel
from time import sleep
import tkinter as tk
import threading
import random

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        i = tk.PhotoImage(width=1, height=1)
        self.title("Tic Tac Toe")
        #self.geometry("300x200")
        self.resizable(False,False)
        
        self.color = "Red"
        self.turns = 0
        self.end_game = False
        self.unused_cells = 'light grey'
        self.flag = 'red3'
        self.opened_cell = 'ghost white'

        self.cover = tk.Frame(self,bg='grey70', relief=tk.RAISED, borderwidth=2)
        self.cover.pack(expand=True, fill=tk.BOTH)

        empty = tk.Frame(self.cover, height=10, bg='grey70')
        empty.pack_propagate(False)
        
        title = tk.Label(self.cover, font=("Arial", 25), text="Tic Tac Toe",  relief=tk.RAISED, borderwidth=2, width=17)
        beginner = tk.Button(self.cover, font=("Arial", 25), fg='royal blue',  image=i, compound=tk.LEFT, text='player vs player',width=250, height=55)
        beginner.bind("<ButtonRelease-1>", lambda event, botPlayer=False: self.start(botPlayer))
        intermediate = tk.Button(self.cover, font=("Arial", 25), fg='crimson', image=i, compound=tk.LEFT, text='Player vs Bot',width=250, height=55)
        intermediate.bind("<ButtonRelease-1>", lambda event, botPlayer=True: self.start(botPlayer))
        
        title.pack()
        empty.pack()
        beginner.pack()
        intermediate.pack()

    def start(self, botPlayer):
        self.cover.pack_forget()
        self.botPlayer = botPlayer
        base_color = "white"
        border_color = "light grey"
        self.whosTurn = tk.Label(self, text=f"{self.color}'s Turn", font=('Helvetica', 14))
        self.whosTurn.grid(column=1,row=0)

        self.top_left = tk.Canvas(self, width=100, height=100, borderwidth=1, bg=base_color, highlightbackground=border_color)
        self.top_mid = tk.Canvas(self, width=100, height=100, borderwidth=1, bg=base_color, highlightbackground=border_color)
        self.top_right = tk.Canvas(self, width=100, height=100, borderwidth=1, bg=base_color, highlightbackground=border_color)
        self.mid_left = tk.Canvas(self, width=100, height=100, borderwidth=1, bg=base_color, highlightbackground=border_color)
        self.mid_center = tk.Canvas(self, width=100, height=100, borderwidth=1, bg=base_color, highlightbackground=border_color)
        self.mid_right = tk.Canvas(self, width=100, height=100, borderwidth=1, bg=base_color, highlightbackground=border_color)
        self.bottom_left = tk.Canvas(self, width=100, height=100, borderwidth=1, bg=base_color, highlightbackground=border_color)
        self.bottom_mid = tk.Canvas(self, width=100, height=100, borderwidth=1, bg=base_color, highlightbackground=border_color)
        self.bottom_right = tk.Canvas(self, width=100, height=100, borderwidth=1, bg=base_color, highlightbackground=border_color)

        self.top_left.bind("<Button-1>", lambda event: self.turn(self.top_left))
        self.top_mid.bind("<Button-1>", lambda event: self.turn(self.top_mid))
        self.top_right.bind("<Button-1>", lambda event: self.turn(self.top_right))
        self.mid_left.bind("<Button-1>", lambda event: self.turn(self.mid_left))
        self.mid_center.bind("<Button-1>", lambda event: self.turn(self.mid_center))
        self.mid_right.bind("<Button-1>", lambda event: self.turn(self.mid_right))
        self.bottom_left.bind("<Button-1>", lambda event: self.turn(self.bottom_left))
        self.bottom_mid.bind("<Button-1>", lambda event: self.turn(self.bottom_mid))
        self.bottom_right.bind("<Button-1>", lambda event: self.turn(self.bottom_right))

        self.top_left.grid(column=0,row=1)
        self.top_mid.grid(column=1,row=1)
        self.top_right.grid(column=2,row=1)
        self.mid_left.grid(column=0,row=2)
        self.mid_center.grid(column=1,row=2)
        self.mid_right.grid(column=2,row=2)
        self.bottom_left.grid(column=0,row=3)
        self.bottom_mid.grid(column=1,row=3)
        self.bottom_right.grid(column=2,row=3)

        self.options = ["top_left", "top_mid", "top_right", "mid_left", "mid_center", "mid_right", "bottom_left", "bottom_mid", "bottom_right"]
        
    def turn(self, button):
        if self.end_game == True:
            return
        if button["background"] == "white":
            str_button = self.convert_object(button)
            self.options.remove(str_button)
            self.turns += 1
            button.configure(bg=self.color)
            self.check_win()
            if self.color == "Red":
                self.color = "Blue"
                self.botTurn()
            else:
                self.color = "Red"
        self.whosTurn.configure(text=f"{self.color}'s Turn")

    def check_win(self):
        if self.mid_center["background"] == self.color:
            if self.top_mid["background"] == self.color and self.bottom_mid["background"] == self.color:
                self.end_screen(f"{self.color} Won")
            if self.top_left["background"] == self.color and self.bottom_right["background"] == self.color:
                self.end_screen(f"{self.color} Won")
            if self.mid_left["background"] == self.color and self.mid_right["background"] == self.color:
                self.end_screen(f"{self.color} Won")
            if self.bottom_left["background"] == self.color and self.top_right["background"] == self.color:
                self.end_screen(f"{self.color} Won")
        else:
            if self.top_left["background"] == self.color and self.top_mid["background"] == self.color and self.top_right["background"] == self.color:
                self.end_screen(f"{self.color} Won")
            if self.bottom_left["background"] == self.color and self.bottom_mid["background"] == self.color and self.bottom_right["background"] == self.color:
                self.end_screen(f"{self.color} Won")
            if self.top_left["background"] == self.color and self.mid_left["background"] == self.color and self.bottom_left["background"] == self.color:
                self.end_screen(f"{self.color} Won")
            if self.top_right["background"] == self.color and self.mid_right["background"] == self.color and self.bottom_right["background"] == self.color:
                self.end_screen(f"{self.color} Won")
        if self.turns == 9:
            self.end_screen("Draw")

    def end_screen(self, option):
        self.end_game = True
        
        self.newWindow = Toplevel(self, width=self.winfo_width()-4, height=self.winfo_height()-4)
        self.newWindow.attributes('-alpha',0.5)
        self.newWindow.overrideredirect(1)
        self.newWindow.lift()
        
        self.x = threading.Thread(target=self.move_with_screen, daemon=True).start()
        screen = tk.Canvas(self.newWindow, bg="black",width=self.winfo_width()-4, height=self.winfo_height()-4)
        screen.create_text(self.winfo_width()//2, self.winfo_height()//2, text=option, font=("Arial", 55), fill='white')
        screen.pack(fill=tk.BOTH)

    def move_with_screen(self):
        for _ in range(999):
            self.newWindow.geometry(f"+{self.winfo_x()+8}+{self.winfo_y()+30}")
            sleep(.001)
            self.newWindow.lift()
        self.move_with_screen()

    def botTurn(self):
        if self.botPlayer == True:
            ranint = random.randint(0,len(self.options)-1)
            self.botOption = self.options[ranint]
            real_button = self.convert_object(str(self.botOption))
            self.turn(real_button)

    def convert_object(self, obj):
        if obj == "top_left":
            return self.top_left
        if obj == "top_mid":
            return self.top_mid
        if obj == "top_right":
            return self.top_right
        if obj == "mid_left":
            return self.mid_left
        if obj == "mid_center":
            return self.mid_center
        if obj == "mid_right":
            return self.mid_right
        if obj == "bottom_left":
            return self.bottom_left
        if obj == "bottom_mid":
            return self.bottom_mid
        if obj == "bottom_right":
            return self.bottom_right
        
        if obj == self.top_left:
            return "top_left"
        if obj == self.top_mid:
            return "top_mid"
        if obj == self.top_right:
            return "top_right"
        if obj == self.mid_left:
            return "mid_left"
        if obj == self.mid_center:
            return "mid_center"
        if obj == self.mid_right:
            return "mid_right"
        if obj == self.bottom_left:
            return "bottom_left"
        if obj == self.bottom_mid:
            return "bottom_mid"
        if obj == self.bottom_right:
            return "bottom_right"
        
if __name__ == "__main__":
    game = Game()
    game.mainloop()