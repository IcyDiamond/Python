import tkinter as tk
from PIL import ImageTk, Image
import os

class Chess(tk.Tk):
    def __init__(self):
        super().__init__()

        row_Names = ["a","b","c","d","e","f","g","h"]
        self.color = "black"
        board = []
        self.temp_coloredboard = []
        self.role = "queen"
        self.role_pawn = [[-1],[-1,0,1]]
        self.role_rook = [[7,6,5,4,3,2,1],[7,6,5,4,3,2,1]]
        self.role_knight = [[-1,-2,-1,-2,1,2,1,2],[-2,-1,2,1,-2,-1,2,1]]
        self.role_bishop = [1,2,3,4,5,6,7]
        pawn = ImageTk.PhotoImage(Image.open("white_pawn.png"))


        for row in range(8):
            for col in range(8):
                square = tk.Canvas(self, name=(str(col)+row_Names[row]), background=self.color, width=80, height=80, highlightthickness=4, highlightbackground=self.color)
                #square.bind("<Button-1>", lambda event, button=square: self.clickBoard(event, button))
                #board.append(square)
                square.create_image(0,0,anchor=tk.NW, image = pawn)
                square.image = pawn
                square.grid(row=row,column=col)
                #self.change_color()
            #self.change_color()
        
        #print(board)

    def clickBoard(self, event, button):
        self.restoreColor()
        base_color = button["background"]
        button.configure(highlightbackground="red")
        self.temp_coloredboard.append([button,button["background"]])

        info = button.grid_info()

        
        if self.role == "pawn":
            for col in self.role_pawn[1]:
                try:
                    temp_sqaure = self.grid_slaves(info["row"],info["column"]+col)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
        if self.role == "rook":
            for col in self.role_rook[1]:
                try:
                    temp_sqaure = self.grid_slaves(info["row"],info["column"]+col)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
            for row in self.role_rook[0]:
                print(row)
                try:
                    temp_sqaure = self.grid_slaves(info["row"]+row,info["column"])
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
            for col in self.role_rook[1]:
                try:
                    temp_sqaure = self.grid_slaves(info["row"],info["column"]-col)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
            for row in self.role_rook[0]:
                print(row)
                try:
                    temp_sqaure = self.grid_slaves(info["row"]-row,info["column"])
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
        if self.role == "knight":
            for num in range(8):
                try:
                    temp_sqaure = self.grid_slaves(info["row"]+self.role_knight[0][num],info["column"]+self.role_knight[1][num])
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
        if self.role == "bishop":
            for num in self.role_bishop:
                try:
                    temp_sqaure = self.grid_slaves(info["row"]+num,info["column"]+num)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
            for num in self.role_bishop:
                try:
                    temp_sqaure = self.grid_slaves(info["row"]-num,info["column"]+num)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
            for num in self.role_bishop:
                try:
                    temp_sqaure = self.grid_slaves(info["row"]+num,info["column"]-num)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
            for num in self.role_bishop:
                try:
                    temp_sqaure = self.grid_slaves(info["row"]-num,info["column"]-num)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
        if self.role == "queen":
            for num in range(1,7):
                try:
                    temp_sqaure = self.grid_slaves(info["row"]+num,info["column"]+num)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
                try:
                    temp_sqaure = self.grid_slaves(info["row"]-num,info["column"]+num)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
                try:
                    temp_sqaure = self.grid_slaves(info["row"]+num,info["column"]-num)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
                try:
                    temp_sqaure = self.grid_slaves(info["row"]-num,info["column"]-num)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
                try:
                    temp_sqaure = self.grid_slaves(info["row"]+num,info["column"])
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
                try:
                    temp_sqaure = self.grid_slaves(info["row"],info["column"]+num)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
                try:
                    temp_sqaure = self.grid_slaves(info["row"]-num,info["column"])
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
                try:
                    temp_sqaure = self.grid_slaves(info["row"],info["column"]-num)
                    self.temp_coloredboard.append([temp_sqaure[0],temp_sqaure[0]["background"]])
                    temp_sqaure[0].configure(highlightbackground="cyan")
                except (tk.TclError, IndexError):
                    pass
        
        
    
    def restoreColor(self):
        for button, base_color in self.temp_coloredboard:
            button.configure(highlightbackground=base_color)

    def change_color(self):
        if self.color == "black":
            self.color = "light grey"
        else:
            self.color = "black" 


if __name__ == "__main__":
    app = Chess()
    app.mainloop()