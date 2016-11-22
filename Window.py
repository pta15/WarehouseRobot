from tkinter import *
window=Tk()
frame = Canvas(window,width = 1280 , height = 720)
frame.grid()

font0 = font.Font(size=25, weight='bold') # Creates font0
label0 = Label(frame, fg="green") # Creates label0
# label0 configuration
label0.config(text='Instructions:\n In this game you have two rob ',font=font0)
label0.place(x=10,y=50) # label0 placement on window

buttonOk=Button(frame,text='Start',command=window.destroy,bg='lightblue',
               height=9, width=17)
buttonOk.place(x=640,y=360)

window.mainloop()

