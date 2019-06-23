import pygame
import ast
class function(object):
    def __init__(self):
        self.window_x = 600
        self.window_y = 400
        self.screen = pygame.display.set_mode((self.window_x,self.window_y))
        pygame.display.set_caption("Rainbow!")
        self.clock = pygame.time.Clock()
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        self.white = (255,255,255)
        self.screen.fill(self.red)

    def printColours2(self,temp):
        ax = abs(temp['DATA'][0]['VALUE'])
        ay = abs(temp['DATA'][1]['VALUE'])
        az = abs(temp['DATA'][2]['VALUE'])
        #print("-",temp,"----------",ax)
        if(ax>2):
            
            #self.screen.fill(self.red)
            print("--------MOVE----------------AXIS X------------MOVE------------",ax)
        #     # elif(sum3>1):
            #     screen.fill(green)
            #     print('green')
        elif(ay>2):
            #self.screen.fill(self.blue)
            print("--------MOVE----------------AXIS Y------------MOVE------------",ay) 
        elif(az>12):
            #self.screen.fill(self.blue)
            print("--------MOVE----------------AXIS Z------------MOVE------------",az) 
        else:
            #self.screen.fill(self.white)
            print("-------------------------- NO MOVE -------------------------",ax,ay,az) 
            #print('white',ax)

    def printColours(self,temp,filename):
        file2 = open(filename,"a")
        str1=""
        str2=""
        print("-",temp)


        for b in temp:
            x = ast.literal_eval(b)
            print(x)
            a = x["DATA"]
            #print(type(a))
            #c = a["DATA"]
            params=[0.0]*9
            j=0
            for i in a:
                d = i["VALUE"]
                params[j]=d
                str1=str1+str(d)+" "
                str2=str2+str(d)+" "
                j+=1
            y=str2.split(" ")
            ax=params[0]
            ay=params[1]
            az=params[2]
            gx=params[3]
            gy=params[4]
            gz=params[5]
            mx=params[6]
            my=params[7]
            mz=params[8]
            if(ax>2):
                self.screen.fill(self.red)
                print('red',ax,ay)
            #     # elif(sum3>1):
                #     screen.fill(green)
                #     print('green')
            elif(ay>2):
                self.screen.fill(self.blue)
                print('blue',ax,ay)
            
                # screen.fill(green)
                # screen.fill(red)
                # screen.fill(blue)
            else:
                self.screen.fill(self.white)
                print('white',ax,ay)

            pygame.display.flip()
            self.clock.tick(30) 
            str1=str1+"\n"
            str2="" 
        file2.write(str1)
        file2.close()
