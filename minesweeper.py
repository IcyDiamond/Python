import tkinter as tk
import random

class Minesweeper(tk.Tk):
    def __init__(self):
        super().__init__()
        i = tk.PhotoImage(width=1, height=1)
        self.board_cells = []
        self.board_cells_reset = []
        self.game_start = False
        self.mine_count = 0
        self.mines = []
        self.opened_cells = []
        self.unused_cells = 'light grey'
        self.flag = 'red3'
        self.opened_cell = 'ghost white'
        self.board_size = [9,9]
        self.cell_size = 30
        self.used_flags = 0
        self.time = 0
        self.game_end = False
        self.timer_enabled = True

        self.cover = tk.Frame(self,bg='grey70', relief=tk.RAISED, borderwidth=2)
        self.cover.pack(expand=True, fill=tk.BOTH)

        empty = tk.Frame(self.cover, height=10, bg='grey70')
        empty.pack_propagate(False)

        self.font = ("system", 20, 'bold')
        self.title("MineSweeper")
        self.geometry("350x300")
        self.resizable(False,False)
        
        title = tk.Label(self.cover, font=("system", 25, 'bold'), text="MineSweeper", bg=self.unused_cells, fg= 'grey17', relief=tk.RAISED, borderwidth=2, width=250)
        beginner = tk.Button(self.cover, image=i, compound=tk.LEFT, font=self.font, bg=self.unused_cells, fg= 'royal blue', text='Beginner',width=250, height=55)
        beginner.bind("<ButtonRelease-1>", lambda event, mines=10, board=[9,9]: self.start_game(event, mines, board))
        intermediate = tk.Button(self.cover,image=i, compound=tk.LEFT, font=self.font, bg=self.unused_cells, fg= 'green', text='Intermediate',width=250, height=55)
        intermediate.bind("<ButtonRelease-1>", lambda event, mines=40, board=[16,16]: self.start_game(event, mines, board))
        expert = tk.Button(self.cover,image=i, compound=tk.LEFT, font=self.font, bg=self.unused_cells, fg= 'red4',  text='Expert',width=250, height=55)
        expert.bind("<ButtonRelease-1>", lambda event, mines=99, board=[30,16]: self.start_game(event, mines, board))
        custom = tk.Button(self.cover,image=i, compound=tk.LEFT, font=self.font, bg=self.unused_cells, fg= 'gray1',  text='Custom',width=250, height=55)
        
        title.pack()
        empty.pack()
        beginner.pack()
        intermediate.pack()
        expert.pack()
        #custom.pack()
        #Beginner - 8x8 or 9x9 - 10 mines
        #Intermediate - 16x16 -  40 mines 
        #expert - 30x16 - 99 mines
        

    def start_game(self, event, mine_count, board_size):
        self.cover.pack_forget()
        self.mine_count = mine_count
        self.board_size = board_size
        self.geometry(f"{self.board_size[0]*(self.cell_size+6)}x{self.board_size[1]*(self.cell_size+6)+50}")
        i = tk.PhotoImage(width=1, height=1)

        bar = tk.Frame(self, height=50, bg=self.unused_cells, width=self.board_size[0]*(self.cell_size+6), relief=tk.GROOVE, borderwidth=2)
        bar.grid()
        bar.pack_propagate(False)

        self.flag_counter = tk.Label(bar, image=i, compound= tk.LEFT, bg=self.unused_cells, text=f'0{self.mine_count}', font=self.font, fg='red', height=50, relief=tk.RIDGE)
        self.flag_counter.pack(side=tk.LEFT)

        self.timer_counter = tk.Label(bar, image=i, compound= tk.LEFT, bg=self.unused_cells, text='000', font=self.font, fg='red', height=50, relief=tk.RIDGE)
        self.timer_counter.pack(side=tk.RIGHT)

        self.face = tk.Button(bar, image=i, compound=tk.LEFT, bg="gold", height=50, width=45, relief=tk.RAISED,text='🙂', font=("system", 25, 'bold'))
        self.face.bind("<ButtonRelease-1>", lambda event : self.reset_board())
        self.face.pack()


        self.board = tk.Frame(self)
        self.board.grid()

        for row in range(self.board_size[1]):
            for col in range(self.board_size[0]):
                cell = tk.Button(self.board, image=i, compound= tk.LEFT, width=self.cell_size, height=self.cell_size, bg=self.unused_cells, font=self.font)
                cell.bind("<ButtonRelease-1>", lambda event, button=cell: self.button_do(event, button))
                cell.bind("<Button-3>", lambda event, button=cell: self.check_flag(button))
                cell.image = i
                cell.grid(row=row+1, column=col)
                self.board_cells.append(cell)
                self.board_cells_reset.append(cell)

    def button_do(self, event, button):
        if self.game_end == True:
            return
        button.configure(relief=tk.GROOVE, borderwidth=1)
        if button['background'] == "red":
            return
        if self.game_start == True:
            self.open_cell(button)
        else:
            self.timer_enabled = True
            self.timer_counter.after(1000, self.add_time)
            self.game_start = True
            self.spawn_mines(button)
            self.open_cell(button)

    def open_cell(self, button):
        if button['background'] == self.flag:
            return
        if button not in self.mines:
            self.cell_search(button)
            self.check_win()
        else:
            self.show_mines()

    def around_cells(self, button):
        info = button.grid_info()
        mine_count = 0
        checked_cells = []
        for row in range(3):
            for col in range(3):
                try:
                    side_button = self.board.grid_slaves(info["row"]+row-1,info["column"]+col-1)
                    side_button = side_button[0]
                    checked_cells.append(side_button)
                    if side_button in self.mines:
                        mine_count += 1
                except (tk.TclError, IndexError):
                    pass
        return checked_cells, mine_count

    def show_number(self, button, mine_count):
        color = self.opened_cell
        if mine_count == 1:
            color = 'blue'
        if mine_count == 2:
            color = 'green'
        if mine_count == 3:
            color = 'red'
        if mine_count == 4:
            color = 'purple'
        if mine_count == 5:
            color = 'crimson'
        if mine_count == 6:
            color = 'cyan'
        if mine_count == 7:
            color = 'black'
        if mine_count == 8:
            color = 'grey'
            
        if button['text'] == '🚩':
            self.used_flags -= 1
            self.flag_count_update()
        button.configure(text=mine_count, bg=self.opened_cell)
        if mine_count == 0:
            button.configure(text='', bg=self.opened_cell)
        button.configure(relief=tk.GROOVE, borderwidth=1, fg=color)

    def cell_search(self, button):
        checked_cells, mine_count = self.around_cells(button)
        self.opened_cells.append(button)
        self.show_number(button, mine_count)

        if mine_count == 0:
            self.open_all(button)

        for cell in checked_cells:
            if cell not in self.opened_cells:
                _, count = self.around_cells(cell)
                
                if count == 0:
                    self.cell_search(cell)
                #else:
                    #self.show_number(cell, count)
                    #cell.configure(bg="green")

    def open_all(self, button):
        checked_cells, mine_count = self.around_cells(button)
        self.opened_cells.append(button)
        for cell in checked_cells:
            checked_cells, mine_count = self.around_cells(cell)
            self.show_number(cell, mine_count)

    def check_flag(self, button):
        if self.game_end == True:
            return
        
        text = button['text']
        if text == self.opened_cell:
            return
        if text == '':
            button.configure(fg=self.flag, text='🚩', borderwidth=1)
            self.used_flags += 1
        if text == '🚩':
            button.configure(fg=self.unused_cells, text='', borderwidth=2)
            self.used_flags -= 1
        self.flag_count_update()       
        self.check_win()
        
    def flag_count_update(self):
        add = ''
        if self.mine_count-self.used_flags > 9:
            add = '0'
        else:
            if self.mine_count-self.used_flags > -10:
                add = '0'
            if self.mine_count-self.used_flags > -1:
                add = '00'
        self.flag_counter.configure(text=add+str(self.mine_count-self.used_flags))

    def spawn_mines(self, button):
        self.board_cells.remove(button)
        for _ in range(self.mine_count):
            self.place_mines(button)

    def place_mines(self, button):
        randint = random.randint(0,len(self.board_cells)-1)
        mine = self.board_cells[randint]
        self.board_cells.remove(mine)
        self.mines.append(mine)

    def show_mines(self):
        self.game_end = True
        self.face.configure(text='🙁')
        for mine in self.mines:
            if mine['text'] == '🚩':
                mine.configure(text = '💣', borderwidth = 1, fg=self.flag)
            else:
                mine.configure(text = '💣', borderwidth = 1, fg="black")

    def check_win(self):
        count = 0
        for cell in self.board_cells:
            if cell['background'] == self.opened_cell:
                count += 1
        if count == len(self.board_cells):
            self.face.configure(text='😎')
            self.game_end = True
            #self.start_game()

    def add_time(self):
        if self.game_end == False:
            self.time += 1
        if self.time < 10:
            add = '00'
        elif self.time > 9:
            add = '0'
        else:
            add = ''

        self.timer_counter.configure(text=add+str(self.time))
        if self.timer_enabled == True:
            self.timer_counter.after(1000, self.add_time)
        else:
            self.timer_counter.configure(text='000') 

    def reset_board(self):
        self.game_start = False
        self.game_end = False
        self.timer_enabled = False        
        self.time = 0
        self.used_flags = 0
        self.board_cells = []
        self.opened_cells = []
        self.mines = []
        self.flag_counter.configure(text=f'0{self.mine_count}')
        self.face.configure(text='🙂')

        for cell in self.board_cells_reset:
            self.board_cells.append(cell)
            cell.configure(text='', bg=self.unused_cells, relief=tk.RAISED, width=self.cell_size, height=self.cell_size, borderwidth=2)

if __name__ == "__main__":
    game = Minesweeper()
    game.mainloop()