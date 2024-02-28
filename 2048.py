import tkinter as tk

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        i = tk.PhotoImage(width=1, height=1)
        self.tempcolumnspan=0
        self.board_cells = []

        self.background = tk.Frame(self)
        self.background.pack()

        for row in range(4):
            for col in range(4):
                cell = tk.Label(self.background, image=i, width=100, height=100, bg='grey60', highlightthickness=5, highlightbackground='grey50')
                cell.grid(row=row, column=col)

        button1 = tk.Label(self.background, image=i, width=100, height=100, bg='red')
        button2 = tk.Label(self.background, image=i, width=100, height=100, bg='blue')
        button3 = tk.Label(self.background, image=i, width=100, height=100, bg='green')
        self.board_cells.append(button1)
        self.board_cells.append(button2)
        self.board_cells.append(button3)
        self.bind('<w>', lambda event, direction = 'up': self.move(direction))
        self.bind('<d>', lambda event, direction = 'right': self.move(direction))
        self.bind('<s>', lambda event, direction = 'down': self.move(direction))
        self.bind('<a>', lambda event, direction = 'left': self.move(direction))
        button1.grid(row=0, column=3)
        button2.grid(row=1, column=1)
        button3.grid(row=3, column=2)
        #surrounding_cells = self.surronding_cells(button)

    def move(self, direction):
        for cell in self.board_cells:
            surrounding_cells = self.surronding_cells(cell)
            if direction == 'up':
                if surrounding_cells['row'] > 0:
                    if surrounding_cells['up'] not in self.board_cells:
                        cell.grid(row=surrounding_cells['row']-1)

            if direction == 'right':
                if surrounding_cells['column'] < 3:
                    if surrounding_cells['right'] not in self.board_cells:
                        cell.grid(column=surrounding_cells['column']+1)

            if direction == 'down':
                if surrounding_cells['row'] < 3:
                    if surrounding_cells['down'] not in self.board_cells:
                        cell.grid(row=surrounding_cells['row']+1)
                        
            if direction == 'left':
                if surrounding_cells['column'] > 0:
                    if surrounding_cells['left'] not in self.board_cells:
                        cell.grid(column=surrounding_cells['column']-1)



    def surronding_cells(self, cell):
        info = cell.grid_info()
        surrounding_cells = {
            'up':  None,
            'right' : None,
            "down" : None,
            'left' : None,
            'column' : info["column"],
            'row' : info["row"]
        }
        
        try:
            cell = self.background.grid_slaves(info["row"]-1,info["column"])
            cell = cell[0]
            surrounding_cells['up'] = cell
        except (tk.TclError, IndexError):
            pass
        try:
            cell = self.background.grid_slaves(info["row"],info["column"]-1)
            cell = cell[0]
            surrounding_cells['left'] = cell
        except (tk.TclError, IndexError):
            pass
        try:
            cell = self.background.grid_slaves(info["row"],info["column"]+1)
            cell = cell[0]
            surrounding_cells['right'] = cell
        except (tk.TclError, IndexError):
            pass
        try:
            cell = self.background.grid_slaves(info["row"]+1,info["column"])
            cell = cell[0]
            surrounding_cells['down'] = cell
        except (tk.TclError, IndexError):
            pass

        
        return surrounding_cells


if __name__ == '__main__':
    game = Game()
    game.mainloop()