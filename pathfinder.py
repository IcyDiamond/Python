import tkinter as tk
import random

class PathFiding(tk.Tk):
    def __init__(self):
        super().__init__()
        i = tk.PhotoImage(width=1, height=1)
        self.board_size = [30,16]
        self.cell_size = 30
        self.color = 'light grey'
        self.stop = False
        self.searching_cells = []
        self.cells = []
        self.path = []

        for row in range(self.board_size[1]):
            for col in range(self.board_size[0]):
                cell = tk.Button(self, image=i, compound= tk.LEFT, width=self.cell_size, height=self.cell_size, bg=self.color, relief=tk.RIDGE)
                self.cells.append(cell)
                cell.parent = ''
                cell.count = 0
                cell.bind("<Button-4>", lambda event, cell=cell: cell.configure(relief=tk.RAISED))
                cell.bind("<Button-1>", lambda event, cell=cell: self.start(cell))
                cell.bind("<Button-3>", lambda event, cell=cell: cell.configure(bg='red'))
                cell.bind("<Button-2>", lambda event, cell=cell: cell.configure(bg=self.color))
                cell.bind("<Button-5>", lambda event, cell=cell: cell.configure(relief=tk.RIDGE))
                cell.image = i
                cell.grid(row=row+1, column=col)

        self.place_walls()

    def start(self, cell):
        cell.parent = 'start'
        self.start_path(cell)

    def start_path(self, base_cell):
        base_cell.configure(bg='green')
        self.searching_cells.append(base_cell)
        surrouding_cells = self.surronding_cells(base_cell)
        for cell in surrouding_cells:
            if cell not in self.searching_cells:
                if cell['background'] == 'red':
                    self.stop = True
                    self.path.append(base_cell)
                    self.check(base_cell)
                    #cell.configure(bg='red')
                if cell['background'] != 'green':
                    if self.stop == False:
                        if cell['relief'] != tk.RAISED:
                            cell.configure(bg='yellow')
                            cell.parent = base_cell
                            self.searching_cells.append(cell)
                            cell.count = base_cell.count + 1
                            cell.configure(text=cell.count, borderwidth=1)
                            self.after(1, lambda cell=cell: self.start_path(cell))

    def check(self, cell):
        if cell.parent:
            if cell.parent == 'start':
                self.after(3, self.reset)
            else:
                self.path.append(cell)
                self.check(cell.parent)

    def reset(self):
        self.stop = False
        for cell in self.searching_cells:
            if cell['text'] != '':
                cell.parent = ''
            cell.count = 0
            cell.configure(bg='light grey', text='', borderwidth=2)
        self.searching_cells = []
        self.move()

    def move(self):
        if self.path != []:
            cell = self.path[len(self.path)-1]
            cell.configure(bg='blue')
            self.path.remove(cell)
            self.after(100, self.move)
            #self.after(100, lambda cell=cell: cell.configure(bg='light grey'))

    def place_walls(self):
        for _ in range(100):
            randcell = random.choice(self.cells)
            randcell.configure(relief=tk.RAISED)

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

if __name__ == '__main__':
    app = PathFiding()
    app.mainloop()