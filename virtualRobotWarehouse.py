from tkinter import *
import random
Movement_Speed = 15
Window_Height = 500
Window_Width = 500
windowDisplay = Tk()
windowDisplay.minsize(width = Window_Width,height = Window_Height)#Minimum window size
windowDisplay.maxsize(width = Window_Width,height = Window_Height)#Maximum window size
Obx1=random.randint(30,250)
Oby1=random.randint(30,250)
Obx2=Obx1+30
Oby2=Oby1-30
canvas = Canvas(windowDisplay, width = Window_Width,height = Window_Height) #Area we can draw on aka canvas
canvas.pack()#Display canvas
Shape1 = canvas.create_rectangle(3,7,3+30,7+30, fill='blue')#Draw Rectangle and keep it in the Shape1 Variable
Shape2=canvas.create_rectangle(Obx1,Oby1,Obx2,Oby2, fill='red')

def rightKey(event): #Right Arrow key is pressed
    global Obx1,Oby1,Oby2,Obx2
    x1,y1,x2,y2=canvas.coords(Shape1) #We get all the cordinates from our rectangle which is Shape1
    if x2 >= Window_Width-15: #x2 right side of rectangle. Here we are checking that x2 is grater or equal to our canvas Width
        canvas.coords(Shape1,x1,y1,x2,y2)#leave rectangle as it is
    else:
        if x2>(Obx1 - 10) and x2<(Obx1+10) and y1< Oby1 and y1>Oby2:
            if canvas.itemcget(Shape2, "fill") == 'red':
                canvas.itemconfig(Shape2, fill='green')
            elif canvas.itemcget(Shape2, "fill") == 'green':
                Obx1=random.randint(30,250)
                Oby1=random.randint(30,250)
                Obx2=Obx1+30
                Oby2=Oby1-30
                canvas.coords(Shape2,Obx1,Oby1,Obx2,Oby2)
        elif x2>(Obx1 - 10) and x2<(Obx1+10) and y2< Oby1 and y2>Oby2:       
            if canvas.itemcget(Shape2, "fill") == 'red':
                canvas.itemconfig(Shape2, fill='green')
            elif canvas.itemcget(Shape2, "fill") == 'green':
                Obx1=random.randint(30,250)
                Oby1=random.randint(30,250)
                Obx2=Obx1+30
                Oby2=Oby1-30
                canvas.coords(Shape2,Obx1,Oby1,Obx2,Oby2)
        canvas.coords(Shape1,x1+Movement_Speed,y1,x2+Movement_Speed,y2)#increase the Shape1 X1 and x2 cordinates to move right by adding the Movement_Speed
        
def leftKey(event):#Left Arrow Key pressed
    global Obx1,Oby1,Oby2,Obx2
    x1,y1,x2,y2=canvas.coords(Shape1)#We get all the cordinates from our rectangle which is Shape1
    if x1 <= 15:#x1 left side of rectangle. Here we are checking that x1 is less or equal to the left boundary of our window
        canvas.coords(Shape1,x1,y1,x2,y2)#leave rectangle as it is
    else:
        if x1<(Obx2 + 10) and x1>(Obx2 - 10) and y1< Oby1 and y1>Oby2:
            if canvas.itemcget(Shape2, "fill") == 'red':
                canvas.itemconfig(Shape2, fill='green')
            elif canvas.itemcget(Shape2, "fill") == 'green':
                Obx1=random.randint(30,250)
                Oby1=random.randint(30,250)
                Obx2=Obx1+30
                Oby2=Oby1-30
                canvas.coords(Shape2,Obx1,Oby1,Obx2,Oby2)
        elif x1<(Obx2 + 10) and x1>(Obx2 - 10) and y2< Oby1 and y2>Oby2:
            if canvas.itemcget(Shape2, "fill") == 'red':
                canvas.itemconfig(Shape2, fill='green')
            elif canvas.itemcget(Shape2, "fill") == 'green':
                Obx1=random.randint(30,250)
                Oby1=random.randint(30,250)
                Obx2=Obx1+30
                Oby2=Oby1-30
                canvas.coords(Shape2,Obx1,Oby1,Obx2,Oby2)
        canvas.coords(Shape1,x1-Movement_Speed,y1,x2-Movement_Speed,y2)#decrease the Shape1 X1 and x2 cordinates to move left by subtracting the Movement_Speed

def upKey(event):#Up Arrow key pressed
    global Obx1,Oby1,Oby2,Obx2
    x1,y1,x2,y2=canvas.coords(Shape1)#We get all the cordinates from our rectangle which is Shape1
    if y1 <= 15:#y1 top side of rectangle. Here we are checking that y1 is less or equal to the top boundary of our window
        canvas.coords(Shape1,x1,y1,x2,y2)#leave rectangle as it is
    else:
        if y1>(Oby1 - 10) and y1<(Oby1+10) and x1>Obx1 and x1<Obx2:
            if canvas.itemcget(Shape2, "fill") == 'red':
                canvas.itemconfig(Shape2, fill='green')
            elif canvas.itemcget(Shape2, "fill") == 'green':
                Obx1=random.randint(30,250)
                Oby1=random.randint(30,250)
                Obx2=Obx1+30
                Oby2=Oby1-30
                canvas.coords(Shape2,Obx1,Oby1,Obx2,Oby2)
        elif y1>(Oby1 - 10) and y1<(Oby1+10) and x2>Obx1 and x2<Obx2:
            if canvas.itemcget(Shape2, "fill") == 'red':
                canvas.itemconfig(Shape2, fill='green')
            elif canvas.itemcget(Shape2, "fill") == 'green':
                Obx1=random.randint(30,250)
                Oby1=random.randint(30,250)
                Obx2=Obx1+30
                Oby2=Oby1-30
                canvas.coords(Shape2,Obx1,Oby1,Obx2,Oby2)
        canvas.coords(Shape1,x1,y1-Movement_Speed,x2,y2-Movement_Speed)#decrease the Shape1 y1 and y2 cordinates to move up by subtracting the Movement_Speed

def downKey(event):#Down Arrow key pressed
    global Obx1,Oby1,Oby2,Obx2
    x1,y1,x2,y2=canvas.coords(Shape1)#We get all the cordinates from our rectangle which is Shape1
    if y2 >= Window_Height-15:#y2 is the bottom side of the rectangle. Here we are checking that the rectangle is greater or equal to the bottom of our window
        canvas.coords(Shape1,x1,y1,x2,y2)#leave rectangle as it is
    else:
        if y2>(Oby2 - 10) and y2<(Oby2+10) and x1>Obx1 and x1<Obx2:
            if canvas.itemcget(Shape2, "fill") == 'red':
                canvas.itemconfig(Shape2, fill='green')
            elif canvas.itemcget(Shape2, "fill") == 'green':
                Obx1=random.randint(30,250)
                Oby1=random.randint(30,250)
                Obx2=Obx1+30
                Oby2=Oby1-30
                canvas.coords(Shape2,Obx1,Oby1,Obx2,Oby2)
        elif y2>(Oby2 - 10) and y2<(Oby2+10) and x2>Obx1 and x2<Obx2:
            if canvas.itemcget(Shape2, "fill") == 'red':
                canvas.itemconfig(Shape2, fill='green')
            elif canvas.itemcget(Shape2, "fill") == 'green':
                Obx1=random.randint(30,250)
                Oby1=random.randint(30,250)
                Obx2=Obx1+30
                Oby2=Oby1-30
                canvas.coords(Shape2,Obx1,Oby1,Obx2,Oby2)
        canvas.coords(Shape1,x1,y1+Movement_Speed,x2,y2+Movement_Speed)#increase the Shape1 y1 and y2 cordinates to move down by adding the Movement_Speed

canvas.update()#update our canvas to show changes
canvas.bind('<Right>', rightKey)#gets Right Arrow key and maps it to the rightKey definition
canvas.bind('<Left>', leftKey)#gets Left Arrow key and maps it to the leftKey definition
canvas.bind('<Up>', upKey)#gets Up Arrow key and maps it to the upKey definition
canvas.bind('<Down>', downKey)#gets Down Arrow key and maps it to the downKey definition
canvas.focus_set()#awaits for input from keyboard
windowDisplay.mainloop()#makes our window to stay open forever
