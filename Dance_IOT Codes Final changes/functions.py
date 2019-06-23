import pygame
class functions(object):
    def __init__(self):
        self.window_x = 600
        self.window_y = 400
        self.screen = pygame.display.set_mode((self.window_x,self.window_y))
        pygame.display.set_caption("Rainbow!")
        self.clock = pygame.time.Clock()
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
    def printColours(self,y):
        a_sum=y[0]+y[1]+y[2]
        g_sum=y[3]+y[4]+y[5]
        m_sum=y[6]+y[7]+y[8]
        if(g_sum<4):
            self.screen.fill(self.red)
            print('red',g_sum)
            # elif(sum3>1):
            #     screen.fill(green)
            #     print('green')
        elif(g_sum>6.00):
            self.screen.fill(self.blue)
            print('blue',g_sum)
        
            # screen.fill(green)
            # screen.fill(red)
            # screen.fill(blue)
        pygame.display.flip()
        self.clock.tick(30)     