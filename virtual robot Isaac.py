import time
from tkinter import *
window = Tk()
canvas = Canvas(window, width = 1200, height=700, bg='white')
canvas.pack()
obj = canvas.create_rectangle(50,20,430,50, fill="black")
wall = canvas.create_rectangle(50,122,430,128, fill='black')
#robot
rbt = canvas.create_rectangle(440,210,450,200,fill="yellow")
# distanced covered per loop
v1=1 

#scale that increases/decreases
speed = Scale(canvas, from_=0.05, to=0.0001, orient=HORIZONTAL, resolution=0.0001,
              length=385)
speed.set(0.02)
speed.place(x=38,y=220)

#gets a random colour
def randomcol():
    import random
    random.choice(color)
    return random.choice(color)

#displays random colour
def fillobj():
    startbutton.configure(state = NORMAL)
    objcol = randomcol()
    canvas.itemconfig(obj,fill = objcol)
    
##############Robot moves to goal############################### 
def startjob():
    #distance from goal
    count = 0
    #displays the count
    counter=Label(canvas,text=str(count), width = 10)
    counter.place(x=200,y=25) 
    #prevents the start/random buttons from being pressed again
    startbutton.configure(state = DISABLED)
    randbutton.configure(state = DISABLED)
    #gets the colour of the goal
    colorgoal = canvas.itemcget(obj, 'fill')

    #finds if objective is on the top or bottom row
    
    if colorgoal  in ('blue','lightblue','violet','orange','pink','red','green'
                   ,'darkgreen'):
        top = False
        #adds a specific distance depending on top or bottom row
        count += 40
    else:
        top = True
        count +=130
    #determines how much to increase count depending on the column
        
    if colorgoal in ('blue','darkblue'):
                count += 370
            
    elif colorgoal in ('lightblue','grey'):
                count += 320
              
    elif colorgoal in ('violet','darkorange'):
                count += 270
             
    elif colorgoal in ('orange','salmon'):
                count += 220
             
    elif colorgoal in ('pink','purple'):
                count += 170
              
    elif colorgoal in ('red','silver'):
                count += 120
               
    elif colorgoal in ('green','lightgreen'):
                count += 70
                
    else:
                count += 20
                    

    #moves robot if a colour is selected      
    if colorgoal != "black":

        #moves robot to correct y coordinate
        if top == True:
                
                for x in range(125):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1,y1-1,x2,y2-1)
                     count -= 1
                     counter.config(text = count)
                     canvas.update()
                     time.sleep(speed.get())
                     
        else:
            
                for x in range(30):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1,y1-1,x2,y2-1)
                     count -= 1  
                     counter.config(text = count)         
                     canvas.update()
                     time.sleep(speed.get())

        #moves robot to the correct x coordinate
        if colorgoal in ('blue','darkblue'):
               
                for x in range(370):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1-1,y1,x2-1,y2)
                     count -= 1
                     counter.config(text = count)
                     canvas.update()
                     time.sleep(speed.get())
        elif colorgoal in ('lightblue','grey'):
              
                for x in range(320):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1-1,y1,x2-1,y2)
                     count -= 1
                     counter.config(text = count)
                     canvas.update()
                     time.sleep(speed.get())
        elif colorgoal in ('violet','darkorange'):
               
                for x in range(270):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1-1,y1,x2-1,y2)
                     count -= 1
                     counter.config(text = count)
                     canvas.update()
                     time.sleep(speed.get())
        elif colorgoal in ('orange','salmon'):
               
                for x in range(220):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1-1,y1,x2-1,y2)
                     count -= 1
                     counter.config(text = count)
                     canvas.update()
                     time.sleep(speed.get())
        elif colorgoal in ('pink','purple'):
             
                for x in range(170):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1-1,y1,x2-1,y2)
                     count -= 1
                     counter.config(text = count)
                     canvas.update()
                     time.sleep(speed.get())
        elif colorgoal in ('red','silver'):

                for x in range(120):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1-1,y1,x2-1,y2)
                     count -= 1
                     counter.config(text = count)
                     canvas.update()
                     time.sleep(speed.get())
        elif colorgoal in ('green','lightgreen'):
                for x in range(70):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1-1,y1,x2-1,y2)
                     count -= 1
                     counter.config(text = count)
                     canvas.update()
                     time.sleep(speed.get())
        else:
                for x in range(20):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1-1,y1,x2-1,y2)
                     count -= 1
                     counter.config(text = count)
                     canvas.update()
                     time.sleep(speed.get())

        #robot moves correct to the y coordinate to reach the goal
        if top == True:
                for x in range(5):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1,y1+1,x2,y2+1)
                     count -= 1
                     counter.config(text = count)
                     canvas.update()
                     time.sleep(speed.get())
                     
        else:
                for x in range(10):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1,y1-1,x2,y2-1)
                     count -= 1    
                     counter.config(text = count)       
                     canvas.update()
                     time.sleep(speed.get())
    else:      
            None
    
    returnbutton.configure(state = NORMAL)

#####Return back to start####################
def returnjob():
    returnbutton.configure(state = DISABLED)
    colorgoal = canvas.itemcget(obj, 'fill')

    if colorgoal  in ('blue','lightblue','violet','orange','pink','red','green'
                   ,'darkgreen'):
        top = False        
    else:
        top = True

    if top == True:
                for x in range(5):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1,y1-1,x2,y2-1)
                     canvas.update()
                     time.sleep(speed.get())
                     
    else:
                for x in range(10):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1,y1+1,x2,y2+1)      
                     canvas.update()
                     time.sleep(speed.get())


    if colorgoal in ('blue','darkblue'):
               
                for x in range(370):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1+1,y1,x2+1,y2)
                     canvas.update()
                     time.sleep(speed.get())
    elif colorgoal in ('lightblue','grey'):
              
                for x in range(320):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1+1,y1,x2+1,y2)
                     canvas.update()
                     time.sleep(speed.get())
    elif colorgoal in ('violet','darkorange'):
               
                for x in range(270):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1+1,y1,x2+1,y2)
                     canvas.update()
                     time.sleep(speed.get())
    elif colorgoal in ('orange','salmon'):
               
                for x in range(220):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1+1,y1,x2+1,y2)
                     canvas.update()
                     time.sleep(speed.get())
    elif colorgoal in ('pink','purple'):
             
                for x in range(170):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1+1,y1,x2+1,y2)
                     canvas.update()
                     time.sleep(speed.get())
    elif colorgoal in ('red','silver'):

                for x in range(120):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1+1,y1,x2+1,y2)
                     canvas.update()
                     time.sleep(speed.get())
    elif colorgoal in ('green','lightgreen'):
                for x in range(70):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1+1,y1,x2+1,y2)
                     canvas.update()
                     time.sleep(speed.get())
    else:
                for x in range(20):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1+1,y1,x2+1,y2)
                     canvas.update()
                     time.sleep(speed.get())
    if top == True:
                
                for x in range(125):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1,y1+1,x2,y2+1)
                     canvas.update()
                     time.sleep(speed.get())
                     
    else:            
                for x in range(30):
                     x1,y1,x2,y2 = canvas.coords(rbt) 
                     canvas.coords(rbt,x1,y1+1,x2,y2+1)        
                     canvas.update()
                     time.sleep(speed.get())

    #returns function of the random and start buttons
    randbutton.configure(state = NORMAL)
    startbutton.configure(state = NORMAL)


#buttons

randbutton = Button(canvas, text='random',command=fillobj,bg='white',
                height=1, width=17)
randbutton.place(x=38, y=190) 

startbutton = Button(canvas, text='start', command=startjob, bg='white',
                height=1, width=17, state = DISABLED)
startbutton.place(x=170, y=190)

returnbutton = Button(canvas, text='return',command=returnjob,bg='white',
                height=1, width=17, state = DISABLED)
returnbutton.place(x=300, y=190)


#parameters for the boxes
b1=130
b2=160
t1=90
t2=120
r1=50
r2=r1+50
r3=r2+50
r4=r3+50
r5=r4+50
r6=r5+50
r7=r6+50
r8=r7+50

# List of possible box colors
color = ('blue','darkblue','lightblue','grey','violet','darkorange','orange',
         'salmon','pink','purple','red','silver','green','lightgreen','darkgreen',
         'brown')
# Objective Boxes
canvas.create_rectangle(r1, b1, r1+30, b2, fill=color[0]) # Blue Box
canvas.create_rectangle(r1, t1, r1+30, t2, fill=color[1]) # Dark Blue Box
canvas.create_rectangle(r2, b1, r2+30, b2, fill=color[2]) # Light Blue Box
canvas.create_rectangle(r2, t1, r2+30, t2, fill=color[3]) # Grey Box
canvas.create_rectangle(r3, b1, r3+30, b2, fill=color[4]) # Violet Box
canvas.create_rectangle(r3, t1, r3+30, t2, fill=color[5]) # Dark Orange Box
canvas.create_rectangle(r4, b1, r4+30, b2, fill=color[6]) # Orange Box
canvas.create_rectangle(r4, t1, r4+30, t2, fill=color[7]) # Salmon Box
canvas.create_rectangle(r5, b1, r5+30, b2, fill=color[8]) # Pink Box
canvas.create_rectangle(r5, t1, r5+30, t2, fill=color[9]) # Purple Box
canvas.create_rectangle(r6, b1, r6+30, b2, fill=color[10])# Red Box
canvas.create_rectangle(r6, t1, r6+30, t2, fill=color[11])# Silver Box
canvas.create_rectangle(r7, b1, r7+30, b2, fill=color[12])# Green Box
canvas.create_rectangle(r7, t1, r7+30, t2, fill=color[13])# Light Green Box
canvas.create_rectangle(r8, b1, r8+30, b2, fill=color[14])# Dark Green Box
canvas.create_rectangle(r8, t1, r8+30, t2, fill=color[15])# Brown Box

window.mainloop()
