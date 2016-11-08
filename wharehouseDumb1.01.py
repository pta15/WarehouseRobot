from tkinter import *
window = Tk()
def Left(event):
    print ("Left button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    if (((x1>0 and x1<=120) or (x1>=325 and x1<=425) or (x1>=625 and x1<=725) or (x1>=925 and x1<=1025) or (x1>=1225 and x1<=1300)) or y1<125 or y2>375)and (x1>0 and x1<1350 and y2>0 and y1<500):
        canvas.coords(id1,x1-10,y1,x2-10,y2)
   
        
def Right(event):
    print ("Right button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    if ((x2>=0 and x2<=120) or (x2>=325 and x2<=425) or (x2>=625 and x2<=725) or (x2>=925 and x2<=1025) or (x2>=1225 and x2<=1350)  or y1<125 or y2>375)and(x2>0 and x2<1350 and y2>0 and y1<500):
        canvas.coords(id1,x1+10,y1,x2+10,y2)

        
def Up(event):
    print ("Up button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    if ((x2>=0 and x2<=125) or (x2>=325 and x2<=425) or (x2>=625 and x2<=725) or (x2>=925 and x2<=1025) or (x2>=1225 and x2<=1350)  or y1<125 or y2>385)and(x2>0 and x1<1350 and y2>0 and y1<500):
        canvas.coords(id1,x1,y1-10,x2,y2-10)
    
def Down(event):
    print ("Down button pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    if ((x2>=0 and x2<=125) or (x2>=325 and x2<=425) or (x2>=625 and x2<=725) or (x2>=925 and x2<=1025) or (x2>=1225 and x2<=1350)  or y1<125 or y2>385)and(x2>0 and x1<1350 and y2>0 and y1<500):
        canvas.coords(id1,x1,y1+10,x2,y2+10)
    
canvas = Canvas(window, width=1350, height=720, bg='white')
canvas.pack()

canvas.bind("<Down>", Down)
canvas.bind("<Up>", Up)
canvas.bind('<Left>', Left)
canvas.bind('<Right>', Right)
canvas.focus_set()
canvas.pack(padx=10,pady=10)

id1=canvas.create_rectangle(120,120,100, 100, width=2)
id2=canvas.create_rectangle(125,125,225,250, fill='blue')
id3=canvas.create_rectangle(125,250,225,375, fill='red')

id2=canvas.create_rectangle(225,125,325,250, fill='purple')
id2=canvas.create_rectangle(225,250,325,375, fill='grey')

id2=canvas.create_rectangle(425,125,525,250, fill='blue')
id3=canvas.create_rectangle(425,250,525,375, fill='red')
id2=canvas.create_rectangle(525,125,625,250, fill='purple')
id2=canvas.create_rectangle(525,250,625,375, fill='grey')

id2=canvas.create_rectangle(725,125,825,250, fill='blue')
id3=canvas.create_rectangle(725,250,825,375, fill='red')
id2=canvas.create_rectangle(825,125,925,250, fill='purple')
id2=canvas.create_rectangle(825,250,925,375, fill='grey')

id2=canvas.create_rectangle(1025,125,1125,250, fill='blue')
id3=canvas.create_rectangle(1025,250,1125,375, fill='red')
id2=canvas.create_rectangle(1125,125,1225,250, fill='purple')
id2=canvas.create_rectangle(1125,250,1225,375, fill='grey')

id4=canvas.create_rectangle(0,500,1350,510, fill="black")
                            
window.mainloop()
