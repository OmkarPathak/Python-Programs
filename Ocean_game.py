Simple python game:Ocean treasures 
 
    Simple game  in which  you have  to find treasure  chests lost  in the 
    bottom of the ocean. The ocean is  represented by a grid of 60 columns 
    by 15 rows and the chests can be  in any one cell. To find a chest you 
    need to drop sonar devices at given locations. 
 
    To play, click buttons to drop sonar device. 
    The sonar reports the distance to the treasure. 
''' 
 
import math 
import random 
import tkinter 
 
def odd(n): 
    return n & 1 
 
def color(a): 
    return 'green' if odd(a) else 'blue' 
 
class Map: 
 
    def __init__(self, master, rows = 15, columns = 60): 
        self.master = master 
        self.row = random.randrange(rows) 
        self.col = random.randrange(columns) 
        self.cost = 0 
        self.found = False 
        Button = tkinter.Button 
        self.buttons = [] 
        options = dict(text = '??', font = 'Courier 14') 
        for r in range(rows): 
            br = []                 # row of buttons 
            self.buttons.append(br) 
            for c in range(columns): 
                b = Button( 
                    master, 
                    command = lambda r=r, c=c: self(r, c), 
                    fg = color(r+c), 
                    **options 
                    ) 
                b.grid(row = r, column = c) 
                br.append(b) 
        master.mainloop() 
 
    def __bool__(self): 
        return self.found 
 
    def __call__(self, row, col): 
        if self: 
            self.master.quit() 
        distance = int(round(math.hypot(row-self.row, col-self.col))) 
        self.buttons[row][col].configure(text = '{}'.format(distance), bg = 'yellow', fg = 'red') 
        self.cost += 1 
        if not distance: 
            print('You win!  At the cost of {} sonar devices.'.format(self.cost)) 
            self.found = True 
 
def main(): 
    root = tkinter.Tk() 
    map = Map(root) 
    root.destroy() 
 
if __name__ == '__main__': 
    main() 
