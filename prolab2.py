from pyamaze import maze,agent,COLOR,textLabel
import turtle                    
import time
import sys
from collections import deque
import datetime

        
an1=datetime.datetime.now()
grid=[]
satir=0
with open ('url2.txt','r') as file:
    for line in file.read().splitlines():
     
     grid.append(line)
     satir=satir+1
 


for i in range(satir):
    grid[i]=grid[i].replace("0"," ")
    grid[i]=grid[i].replace("1","+")
    grid[i]=grid[i].replace("2","+")
    grid[i]=grid[i].replace("3","+")
    

            

print(grid)        



        




wn = turtle.Screen()               
wn.bgcolor("black")                
wn.title("Prolab II proje I")
wn.setup(1300,700)                  


    

class Maze(turtle.Turtle):               
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")           
        self.color("white")             
        self.penup()                    
        self.speed(0)


class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(4)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)



class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(1)

            



def setup_maze(grid):                         
    global start_x, start_y, end_x, end_y      
    for y in range(len(grid)):                 
        for x in range(len(grid[y])):          
            character = grid[y][x]             
            screen_x = -588 + (x * 24)         
            screen_y = 288 - (y * 24)          

            if character == "+":
                maze1.goto(screen_x, screen_y)         
                maze1.stamp()                          
                walls.append((screen_x, screen_y))    
            if character == " " or character == "e":
                path.append((screen_x, screen_y))     
            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)       
                end_x, end_y = screen_x,screen_y     
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y  
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()


def search(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:          
        time.sleep(0)
        x, y = frontier.popleft()     

        if(x - 24, y) in path and (x - 24, y) not in visited:  
            cell = (x - 24, y)
            solution[cell] = x, y    
            blue.goto(cell)        
            blue.stamp()
            frontier.append(cell)   
            visited.add((x-24, y))  
        if (x, y - 24) in path and (x, y - 24) not in visited:  
            cell = (x, y - 24)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution)

        if(x + 24, y) in path and (x + 24, y) not in visited:   
            cell = (x + 24, y)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  
            cell = (x, y + 24)
            solution[cell] = x, y
            
            
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x,y)
        green.stamp()
        


def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):    
        yellow.goto(solution[x, y])        
        yellow.stamp()
        x, y = solution[x, y]               


maze1 = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()


walls = []
path = []
visited = set()
frontier = deque()
solution = {}                           



setup_maze(grid)
search(start_x,start_y)
backRoute(end_x, end_y)
wn.exitonclick()


an2=datetime.datetime.now()
print(an2-an1)


an3=datetime.datetime.now()
def BFS(m):
    start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bfsPath={}
    print(start)
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
                
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
        print(fwdPath, "a")
    return fwdPath


if __name__=='__main__':
    a=int(input("enter a value"))
    b=int(input("enter a value"))
    m=maze(a,b)
    m.CreateMaze(loopPercent=40)
    path=BFS(m)

    a=agent(m,footprints=True,filled=True)
    m.tracePath({a:path})
    an4=datetime.datetime.now()
    
    
    l=textLabel(m,'en kısa yolun uzunlugu',len(path)+1)
    c=textLabel(m,'gecen sure:',an4-an3)

    m.run()
