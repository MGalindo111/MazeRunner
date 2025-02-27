from graphic import Cell
from time import sleep
import random as rand

class Maze():
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None,seed=None):
        if seed != None:
            rand.seed(seed)
        print (rand.random())
        self.x1 =x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells= []
        self.create_cells()
        self.break_ent_exit()
        self.break_walls_r(0,0)
        self._reset_cells_visited()
       

        
    def solve(self):
        x = self.solve_r(0,0)
        if x:
            return True
        return False
    def solve_r(self,i,j):
        self.animate()
        print(f"solving for col {i} row {j}")
        self.cells[i][j].visited = True
        if i== self.num_cols-1 and j == self.num_rows-1:
            return True
        
        if not self.cells[i][j].has_left:
            if not self.cells[i-1][j].visited:
                self.cells[i][j].draw_move(self.cells[i-1][j])
                z=self.solve_r(i-1,j)
                if z:
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i-1][j],True)
        if not self.cells[i][j].has_right:
            if not self.cells[i+1][j].visited:
                self.cells[i][j].draw_move(self.cells[i+1][j])
                z=self.solve_r(i+1,j)
                if z:
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i+1][j],True)
        if not self.cells[i][j].has_bot:
            if not self.cells[i][j+1].visited:
                self.cells[i][j].draw_move(self.cells[i][j+1])
                z=self.solve_r(i,j+1)
                if z:
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i][j+1],True)
        if not self.cells[i][j].has_top:
            if not self.cells[i][j-1].visited:
                self.cells[i][j].draw_move(self.cells[i][j-1])
                z=self.solve_r(i,j-1)
                if z:
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i][j-1],True)


    def break_walls_r(self,i,j):
       
        print(f"visiting col {i} and row {j}")
        
        self.cells[i][j].visited = True
        
        
        
        while True:
            to_visit = []
            if i>0:
                #print("check left")
                if self.cells[i-1][j].visited == False:
                    to_visit.append((i-1,j))
            if i<self.num_cols-1:
                #print("checkginr right")
                if self.cells[i+1][j].visited == False:
                    to_visit.append((i+1,j))
            if j>0:
                #print("check top")
                if self.cells[i][j-1].visited == False:
                    to_visit.append((i,j-1))
            if j<self.num_rows-1:
                #print("check bot ")
                if self.cells[i][j+1].visited == False:
                    to_visit.append((i,j+1))
                
            if to_visit == []:
                self.draw_cell(i,j)
                return
            direction_index = rand.randrange(len(to_visit))
            next_index = to_visit[direction_index]
            #right
            if next_index[0] == i+1:
                #print("going right")
                self.cells[i][j].has_right=False
                self.cells[i+1][j].has_left=False

            #left
            if next_index[0] == i - 1:
                #print("going left")
                self.cells[i][j].has_left = False
                self.cells[i - 1][j].has_right = False
            # down
            if next_index[1] == j + 1:
                #print("going down")
                self.cells[i][j].has_bot = False
                self.cells[i][j + 1].has_top = False
            # up
            if next_index[1] == j - 1:
                #print("going up")
                self.cells[i][j].has_top = False
                self.cells[i][j - 1].has_bot = False

            self.break_walls_r(next_index[0],next_index[1])
            
            
            
            
  

            
    def create_cells(self):
        
        for i in range(self.num_cols):
            z = []
            for j in range(self.num_rows):
                x= Cell(self.win)
                z.append(x)
            self.cells.append(z)


       
        for i in range(len(self.cells)):
            
            
            for j in range(len(self.cells[i])):
                
                
                self.draw_cell(i,j)
    def draw_cell(self,i,j):
        cell = self.cells[i][j]
        cellx1 = self.x1  + (i) * self.cell_size_x
        cellx2 = cellx1 + self.cell_size_x
        celly1 = self.y1  + (j) * self.cell_size_y
        celly2 = celly1+self.cell_size_y
      
       
        cell.draw(cellx1,celly1,cellx2,celly2)
        self.animate()
    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.1)
    def break_ent_exit(self):
        self.cells[0][0].has_top = False
        self.draw_cell(0,0)
        self.cells[self.num_cols - 1][self.num_rows - 1].has_bot = False
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)
    def _reset_cells_visited(self):
        for col in self.cells:
            for row in col:
                row.visited=False
