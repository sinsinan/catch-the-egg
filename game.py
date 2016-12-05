import pygame
import time
import random

pygame.init()


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


display_width=800
display_height=600

screen=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Catch The Egg")
clock=pygame.time.Clock()


wegg=pygame.image.load('wegg.png')
begg=pygame.image.load('begg.png')
basket=pygame.image.load('basket.jpeg')

n=1
p=0
q=0
r=0
s=0
list_x=[]
list_y=[]
list_n=[]
list_type=[]


def create():
        global n,p,q,r,s,list_x,list_y,list_n,list_type
        n=random.randint(1,3)
        list_x.append(n*((display_width-27)/4))
        list_y.append(30)
        list_n.append(n)
        c=random.randint(1,3)
        if c==1:
                list_type.append(begg)
        else:
                list_type.append(wegg)
        s=r
        r=q
        q=p
        p+=1

def gameobjects(basket_x):
        global n,p,q,s,r,list_x,list_y,list_n,list_type
        for i in [q,r,s]:
                screen.blit(list_type[i],(list_x[i],list_y[i]))
        screen.blit(basket,(basket_x,500))
                        
       
def gameloop():
        global n,p,q,r,s,list_x,list_y,list_n,list_type
        speed=2
        point=0
        mouse_x=400
        max =10
        create()
	while 1:
		for event in pygame.event.get():
            		if event.type == pygame.QUIT:
                		pygame.quit()	
                		quit()
                        elif event.type == pygame.MOUSEMOTION:
                                mouse_x,y=event.pos
                for i in [q,r,s]:
                        list_y[i]+=speed
                        if list_y[i]>500 and ((list_x[i]>mouse_x and list_x[i]<mouse_x+140))and list_type[i]==begg:
                                print point
                                list_y[i]=-100
                                pygame.quit()	
                                quit()
                        elif list_y[i]>500 and ((list_x[i]>mouse_x and list_x[i]<mouse_x+140)):
                                point+=1
                                list_y[i]=-100
                                
                        elif list_y[i]>520 and list_type[i]==wegg:
                                print point
                                list_y[i]=-100
                                pygame.quit()	
                                quit()
                                
                if list_y[q] > display_height/3:
                        create()
                screen.fill(white)
                gameobjects(mouse_x)
                if point >= max:
                        speed+=1
                        max+=max
                text="point:"+str(point)
                font = pygame.font.Font('freesansbold.ttf',20)
                TextSurf = font.render(text, True, red)
                TextRect=TextSurf.get_rect()
               
                TextRect.center = ((display_width-50),(15))
                screen.blit(TextSurf, TextRect)
                pygame.display.update()
                clock.tick(60)




gameloop()
pygame.quit()	
quit()
