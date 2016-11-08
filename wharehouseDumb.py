from tkinter import *
window = Tk()
def Left(event):
    print ("Left button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    if y2<100:
        if x1>100:
            canvas.coords(id1,x1-20,y1,x2-20,y2)
    elif y2>200:
        if x1>0:
            canvas.coords(id1,x1-20,y1,x2-20,y2)
    elif y2>500:
        if x1>100:
            canvas.coords(id1,x1-20,y1,x2-20,y2)
    else:
        if x1>100:
            canvas.coords(id1,x1-20,y1,x2-20,y2)
def Right(event):
    print ("Right button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    if x1<1280 and x2<1280:
        canvas.coords(id1,x1+20,y1,x2+20,y2)
    else:
        print("error")
def Up(event):
    print ("Up button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    if y1>0 and y2>0:
        canvas.coords(id1,x1,y1-20,x2,y2-20)
    else:
        print("error")
def Down(event):
    print ("Down button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    if y1<720 and y2<720:
        canvas.coords(id1,x1,y1+20,x2,y2+20)
    else:
        print("error")
canvas = Canvas(window, width=1280, height=720, bg='white')
canvas.pack()

canvas.bind("<Down>", Down)
canvas.bind("<Up>", Up)
canvas.bind('<Left>', Left)
canvas.bind('<Right>', Right)
canvas.focus_set()
canvas.pack(padx=10,pady=10)
id1=canvas.create_rectangle(120,120,100, 100, width=2)
id2=canvas.create_rectangle(0,0,100,100, fill='blue')
id3=canvas.create_rectangle(0,100,100,200, fill='red')
id4=canvas.create_rectangle(0,500,100,698, fill="black")
                            
window.mainloop()
