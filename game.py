import pygame
import time
import random
import sys
pygame.font.init()
pygame.mixer.init()

FONT = pygame.font.SysFont("comicsans",30)

WIDTH,HEIGHT = 1300,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fighter game")

title = pygame.transform.scale(pygame.image.load("Start_pic.png"),(WIDTH,HEIGHT))
bg = pygame.transform.scale(pygame.image.load("Background.png"),(WIDTH,HEIGHT))
p1win = pygame.transform.scale(pygame.image.load("p1win.png"),(WIDTH,HEIGHT))
p2win = pygame.transform.scale(pygame.image.load("p2won.png"),(WIDTH,HEIGHT))

punch = pygame.mixer.Sound("punch.mp3")
c_height = 400
c_width = 400

def draw(player,player2,screen,p1_life,p2_life):
    current_screen = screen
        
    p1msg = FONT.render(f"Player 1",1,"white")
    p2msg = FONT.render(f"Player 2",1,"white")
    WIN.blit(current_screen,(0,0))
    if current_screen == bg:
        WIN.blit(player.image,(player.x,player.y))
        WIN.blit(player2.image,(player2.x,player2.y))
        WIN.blit(p1msg,(50,10))
        WIN.blit(p2msg,(WIDTH-160,10))
        

        p1_coord=50
        rec = pygame.Rect(p1_coord,50,50,30) 
        pygame.draw.line(WIN, "black", rec.topleft, rec.bottomleft,3)   # Left
        pygame.draw.line(WIN, "black", rec.topright, rec.bottomright, 3) # Right

        for i in range(0,p1_life):
            rec = pygame.Rect(p1_coord,50,50,30) 
            pygame.draw.rect(WIN,"red",rec)
            pygame.draw.line(WIN, "black", rec.topleft, rec.topright, 3)     # Top
            pygame.draw.line(WIN, "black", rec.bottomleft, rec.bottomright, 3)  # Bottom
            p1_coord+=50
        
        p2_coord = WIDTH-100
        rec2 = pygame.Rect(p2_coord,50,50,30) 
        pygame.draw.line(WIN, "black", rec2.topleft, rec2.bottomleft, 3)   # Left
        pygame.draw.line(WIN, "black", rec2.topright, rec2.bottomright, 3) # Right

        for i in range(0,p2_life):
            rec2 = pygame.Rect(p2_coord,50,50,30) 
            pygame.draw.rect(WIN,"red",rec2)
            pygame.draw.line(WIN, "black", rec2.topleft, rec2.topright, 3)     # Top
            pygame.draw.line(WIN, "black", rec2.bottomleft, rec2.bottomright, 3)  # Bottom
            p2_coord-=50

    key = pygame.key.get_pressed()
    if p1_life<=0:
        WIN.blit(p2win,(0,0))
        
    elif p2_life<=0:
        WIN.blit(p1win,(0,0))        

    pygame.display.update()

class PlayerLeft:
    def __init__(self,x,y,sound):
        self.sprites = []
        self.punch = sound
        self.curr = 0
        self.IsAnimate = False
        for i in range(1,7):
            self.sprites.append(pygame.transform.scale((pygame.image.load(f"RightChar{i}.png")),(c_width,c_height)))

        self.image = self.sprites[self.curr]
        self.x = x
        self.y = y

    
    def animate(self):
        self.IsAnimate = True
        self.punch.play()
    def update(self):
        if self.IsAnimate == True:
                self.curr +=1
                if int(self.curr) == len(self.sprites):
                    self.curr =0 
                    self.IsAnimate = False
                self.image = self.sprites[int(self.curr)]


class PlayerRight:
    def __init__(self,x,y,sound):
        self.IsAnimate = False
        self.punch = sound
        self.x = x
        self.y = y
        self.sprites=[]
        self.curr=0
        self.image = pygame.transform.scale(pygame.image.load("leftChar1.png"),(c_width,c_height+30))
        for i in range(1,4):
            self.sprites.append(pygame.transform.scale(pygame.image.load(f"leftChar{i}.png"),(c_width,c_height+30)))
        
    def animate(self):
        self.IsAnimate= True
        self.punch.play()
    def update(self):
        if self.IsAnimate:
            self.curr +=0.7
            if int(self.curr) == len(self.sprites):
                self.curr =0 
                self.IsAnimate = False
            self.image = self.sprites[int(self.curr)]

clock = pygame.time.Clock()

def main():
    p1_life = 10
    p2_life = 10
    run = True
    current_screen = title
    clock.tick(60)
    player = PlayerLeft(10,300,punch)
    player2 = PlayerRight(900,300,punch)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    player.animate()
                    if player.x  >= player2.x - c_width/2:
                        player2.x +=50
                        if (p2_life>0):
                            p2_life-=1

                        
                elif event.key == pygame.K_DOWN:        #for player2
                    player2.x+=100              #p2 movement               
                    if player2.x +300>=WIDTH:              
                        player2.x-=100             
                elif event.key == pygame.K_UP:             
                    player2.x-=100             
                    if player2.x<0:            
                        player2.x+=100                          
                elif event.key == pygame.K_k:           #k for attack
                    player2.animate()
                    if player.x  >= player2.x - c_width/2:
                        player.x -=50         
                        if(p1_life>0):
                            p1_life-=1    #till here


                elif event.key == pygame.K_RIGHT:   #p1 movement
                    player.x+=100
                    if player.x + c_width >=WIDTH:
                        player.x-=100
                elif event.key == pygame.K_LEFT:
                    player.x-=100
                    if player.x<0:
                        player.x+=100

                elif event.key == pygame.K_RETURN:  #background
                    current_screen = bg
                
        player.update()
        player2.update()
        draw(player,player2,current_screen,p1_life,p2_life)

    pygame.quit()

if __name__ == "__main__":
    main()
