from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self,width,height):
        self.width=width
        self.height = height
        self.root = Tk()
        self.root.title("My Title")
        self.canvas =Canvas(self.root,bg="white",height=height,width=width)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM Delete Window",self.close)
        

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()


    def wait_for_close(self):
        self.running = True
        while self.running == True:     
            self.redraw()
        print("window closed....")
    def close(self):
        self.running = False

    def draw_line(self,line,fill_color="black"):
        line.draw(self.canvas,fill_color)    

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def draw(self,canvas,fill_color="black"):
        x1= self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y
        canvas.create_line(x1,y1,x2,y2,fill=fill_color,width=2)

class Cell():
    def __init__(self,window=None,visited=False):
        self.has_left= True
        self.has_right = True
        self.has_top = True
        self.has_bot = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = window
        self.visited = visited
        
    def draw(self,x1,y1,x2,y2):
        if self.win is None:
            return
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        topleft = Point(x1,y1)
        topright = Point(x2,y1)
        botleft = Point(x1,y2)
        botright = Point(x2,y2)
        if self.has_left:
            left_wall = Line(topleft,botleft)
            self.win.draw_line(left_wall)
        else:
            left_wall = Line(topleft,botleft)
            self.win.draw_line(left_wall,"white")
        if self.has_right:
            right_wall = Line(topright,botright)
            self.win.draw_line(right_wall)
        else:
            right_wall = Line(topright,botright)
            self.win.draw_line(right_wall,"white")
        if self.has_top:
            top_wall = Line(topleft,topright)
            self.win.draw_line(top_wall)
        else:
            top_wall = Line(topleft,topright)
            self.win.draw_line(top_wall,"white")
        if self.has_bot:
            bot_wall = Line(botleft,botright)
            self.win.draw_line(bot_wall)
        else:
            bot_wall = Line(botleft,botright)
            self.win.draw_line(bot_wall,"white")
    def draw_move(self,to_cell,undo=False):
        if undo:
            color = "gray"
        else:
            color="red"
        self_centerx = abs(self.x2-self.x1)//2 + self.x1
        self_centery = abs(self.y2-self.y1)//2 + self.y1
        to_centerx = abs(to_cell.x2-to_cell.x1)//2 + to_cell.x1
        to_centery = abs(to_cell.y2-to_cell.y1)//2 + to_cell.y1
        line = Line(Point(self_centerx,self_centery),Point(to_centerx,to_centery))
        line.draw(self.win.canvas,color)
