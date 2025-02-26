from tkinter import Tk, BOTH, Canvas
from graphic import Window,Point,Line
def main():
    print("hello")
    my_window = Window(800,600)
    p1 = Point(50,50)
    p2 = Point(400,400)
    line_1 = Line(p1,p2)
    my_window.draw_line(line_1,"black")
    my_window.wait_for_close()
    
main()