if robotcolor == 'yellow': #use to detect if it is the first robot then do the rest
            if callcolor=='blue': #if the callcolor variable is equal to blue then do the rest 
                for i in range(543):
                    for x in range(50): #move robot for 543 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot) #get robot current x, y positions and store them in the x1,y1,x2,y2 variables 
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)#make robot move upwards by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(1223):
                    for x in range(50): #move robot for 1223 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot) #get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        if x1 < 1000: #if x1 coordinate is less then 1000 pixels then do the following
                            canvas.coords(robot,x1,y1,x2,y2) #used to leave robot in current possition 
                        else: #when previous boolean statment is false do the following 
                            canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(40):
                    for x in range(50):#move robot for 40 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)  #make robot move down by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(950):
                    for x in range(50):#move robot for 950 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2)  #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(94):
                    for x in range(50):#move robot for 94 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy) #make robot move down by decreasing the y coordinates 
                        canvas.update()#update and display the robot position to give the impression of robot movement 
                for i in range(63):
                    for x in range(50):#move robot for 63 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1+vx,y1,x2+vx,y2)#make robot move right by decreasing the x coordinates#make robot move right by decreasing the x coordinates 
                        canvas.update()#update and display the robot position to give the impression of robot movement 
                count() # Call count() function
            
            elif callcolor == 'lightblue':  #if the callcolor variable is equal to lightblue then do the rest 
                for i in range(543):
                    for x in range(50):#move robot for 543 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)#make robot move upwards by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(903):
                    for x in range(50):#move robot for 903 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        if x1 < 1000: #if x1 coordinate is less then 1000 pixels then do the following
                            canvas.coords(robot,x1,y1,x2,y2) #used to leave robot in current possition 
                        else: #when previous boolean statment is false do the following
                            canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(40):
                    for x in range(50):#move robot for 40 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)  #make robot move down by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(640):
                    for x in range(50): #move robot for 640 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(94):
                    for x in range(50):#move robot for 94 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)  #make robot move down by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(45):
                    for x in range(50):#move robot for 45 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                count() # Call count() function
            
            elif callcolor == 'violet':  #if the callcolor variable is equal to violet then do the rest 
                for i in range(543):
                    for x in range(50):#move robot for 543 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy)#make robot move upwards by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(923):
                    for x in range(50):#move robot for 923 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        if x1 < 1000:#if x1 coordinate is less then 1000 pixels then do the following
                            canvas.coords(robot,x1,y1,x2,y2) #used to leave robot in current possition 
                        else: #when previous boolean statment is false do the following
                            canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(40):
                    for x in range(50):#move robot for 40 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)  #make robot move down by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(640):
                    for x in range(50):#move robot for 640 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(94):
                    for x in range(50):#move robot for 94 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)  #make robot move down by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(50):
                    for x in range(50):#move robot for 50 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1+vx,y1,x2+vx,y2)#make robot move right by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                count() # Call count() function
             
            elif callcolor == 'orange':  #if the callcolor variable is equal to orange then do the rest 
                for i in range(543):
                    for x in range(50): #move robot for 543 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy) #make robot move upwards by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(608):
                    for x in range(50):#move robot for 608 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        if x1 < 1000: #used to leave robot in current possition 
                            canvas.coords(robot,x1,y1,x2,y2)
                        else: #when previous boolean statment is false do the following
                            canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(40):
                    for x in range(50):#move robot for 40 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy) #make robot move down by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(330):
                    for x in range(50):#move robot for 330 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(94):
                    for x in range(50):#move robot for 94 x 50 times 
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy) #make robot move down by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(53):
                    for x in range(50):#move robot for 53 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                count() # Call count() function
                
            elif callcolor == 'pink':  #if the callcolor variable is equal to pink then do the rest 
                for i in range(543):
                    for x in range(50):#move robot for 543 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy) #make robot move upwards by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(623):
                    for x in range(50):#move robot for 623 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        if x1 < 1000: #if x1 coordinate is less then 1000 pixels then do the following
                            canvas.coords(robot,x1,y1,x2,y2) #used to leave robot in current possition 
                        else: #when previous boolean statment is false do the following
                            canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(40):
                    for x in range(50):#move robot for 40 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)#make robot move down by decreasing the y coordinates
                        canvas.update()#update and display the robot position to give the impression of robot movement 
                for i in range(330):
                    for x in range(50):#move robot for 330 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(100):
                    for x in range(50):#move robot for 100 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)#make robot move down by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(40):
                    for x in range(50):#move robot for 40 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1+vx,y1,x2+vx,y2)#make robot move right by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                count() # Call count() function
                
            elif callcolor == 'red':  #if the callcolor variable is equal to red then do the rest 
                for i in range(543):
                    for x in range(50):#move robot for 543 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1-vy,x2,y2-vy) #make robot move upwards by decreasing the y coordinates 
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(303):
                    for x in range(50):#move robot for 303 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        if x1 < 1000:#if x1 coordinate is less then 1000 pixels then do the following
                            canvas.coords(robot,x1,y1,x2,y2) #used to leave robot in current possition 
                        else: #when previous boolean statment is false do the following
                            canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(135):
                    for x in range(50):#move robot for 135 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1,y1+vy,x2,y2+vy)#make robot move down by decreasing the y coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                for i in range(80):
                    for x in range(50):#move robot for 80 x 50 times
                        x1,y1,x2,y2=canvas.coords(robot)#get robot current x, y positions and store them in the x1,y1,x2,y2 variables
                        canvas.coords(robot,x1-vx,y1,x2-vx,y2) #make robot move left by decreasing the x coordinates
                        canvas.update() #update and display the robot position to give the impression of robot movement 
                count() # Call count() function
            
                    
