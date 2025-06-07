import pygame
import time
import random
import sys

WIDTH,HEIGHT = 1300,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fighter game")

BG = pygame.transform.scale(pygame.image.load("Background.png"),(WIDTH,HEIGHT))


c_height = 400
c_width = 400

def draw(player,player2):
    WIN.blit(BG,(0,0))
    WIN.blit(player.image,(player.x,player.y))
    WIN.blit(player2.image,(player2.x,player2.y))
    pygame.display.update()

class PlayerLeft:
    def __init__(self,x,y):
        self.sprites = []
        self.curr = 0
        self.IsAnimate = False
        for i in range(1,11):
            self.sprites.append(pygame.transform.scale((pygame.image.load(f"attack_{i}.png")),(c_width,c_height)))

        self.image = self.sprites[self.curr]
        self.x = x
        self.y = y

    
    def animate(self):
        self.IsAnimate = True
    def update(self):
        if self.IsAnimate == True:
                self.curr +=1
                if int(self.curr) == len(self.sprites):
                    self.curr =0 
                    self.IsAnimate = False
                self.image = self.sprites[int(self.curr)]


class PlayerRight:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.sprites=[]
        self.image = pygame.transform.scale(pygame.image.load("RightCharacter.png"),(c_width,c_height+100))



clock = pygame.time.Clock()

def main():
    run = True
    clock.tick(60)
    player = PlayerLeft(800,300)
    player2 = PlayerRight(900,300)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            key = pygame.key.get_pressed() 
            if key[pygame.K_q]:
                player.animate()
                if player.x + 150 >= player2.x:
                    player2.x +=50
                    
            elif key[pygame.K_DOWN]:        #for player2
                player2.x+=100
                if player2.x +300>=WIDTH:
                    player2.x-=100
            elif key[pygame.K_UP]:
                player2.x-=100
                if player2.x<0:
                    player2.x+=100           #till here
            elif key[pygame.K_RIGHT]:
                player.x+=100
                if player.x + 100 >=WIDTH:
                    player.x-=100
            elif key[pygame.K_LEFT]:
                player.x-=100
                if player.x<0:
                    player.x+=100
        
        player.update()
        draw(player,player2)

    pygame.quit()

if __name__ == "__main__":
    main()
