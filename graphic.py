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

    def draw_line(self,line,fill_color):
        line.draw(self.canvas,fill_color)    

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def draw(self,canvas,fill_color):
        x1= self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y
        canvas.create_line(x1,y1,x2,y2,fill=fill_color,width=2)
    