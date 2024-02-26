import tkinter as tk
import random

class MazeGen(tk.Tk):
    def __init__(self):
        super().__init__()
        board_size = [16,16]
        cell_size = 30
        cell_color = 'red'
        self.walls = []

        for row in range(board_size[0]):
            for col in range(board_size[1]):
                cell = tk.Canvas(self, bg=cell_color, width=cell_size, height=cell_size, highlightthickness=0)
                cell.bind("<Button-1>", lambda event, cell=cell: self.open_cell(event, cell))
                cell.grid(row=row, column=col)

    def open_cell(self, event, starting_cell):
        starting_cell.configure(bg='grey')
        surrouding_cells = self.surronding_cells(starting_cell)

        for cell in surrouding_cells:
            if cell['background'] == 'green':
                cell.configure(bg='black')
            elif cell['background'] == 'red':
                cell.configure(bg='green')

        randcell = self.foo(surrouding_cells)
        if randcell['background'] != 'green':
            self.open_cell(event, starting_cell)
        else:
            print(surrouding_cells)
            print(randcell['background'])
            randcell.configure(bg='yellow')
            self.after(500, lambda event=None, cell=randcell :self.open_cell(event, cell))

    def foo(self, surrouding_cells):
        randcell = random.choice(surrouding_cells)
        return randcell

    def surronding_cells(self, cell):
        info = cell.grid_info()
        surrounding_cells = []
        try:
            cell = self.grid_slaves(info["row"]-1,info["column"])
            cell = cell[0]
            surrounding_cells.append(cell)
        except (tk.TclError, IndexError):
            pass
        try:
            cell = self.grid_slaves(info["row"],info["column"]-1)
            cell = cell[0]
            surrounding_cells.append(cell)
        except (tk.TclError, IndexError):
            pass
        try:
            cell = self.grid_slaves(info["row"],info["column"]+1)
            cell = cell[0]
            surrounding_cells.append(cell)
        except (tk.TclError, IndexError):
            pass
        try:
            cell = self.grid_slaves(info["row"]+1,info["column"])
            cell = cell[0]
            surrounding_cells.append(cell)
        except (tk.TclError, IndexError):
            pass

        return surrounding_cells

if __name__ == "__main__":
    app = MazeGen()
    app.mainloop()