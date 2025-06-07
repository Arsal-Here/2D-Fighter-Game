import pygame
import time
import random


WIDTH,HEIGHT = 1300,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fighter game")

BG = pygame.transform.scale(pygame.image.load("image.jpeg.jpg"),(WIDTH,HEIGHT))

def draw(player):
    WIN.blit(BG,(0,0))
    WIN.blit(player.image,(player.x,player.y))
    pygame.display.update()

class Player:
    def __init__(self,x,y):
        self.sprites = []
        self.curr = 0
        self.IsAnimate = False
        for i in range(1,11):
            self.sprites.append(pygame.image.load(f"attack_{i}.png"))

        self.image = self.sprites[self.curr]
        self.x = x
        self.y = y

    
    def animate(self):
        self.IsAnimate = True
    def update(self):
        if self.IsAnimate == True:
                self.curr +=0.2
                if int(self.curr) == len(self.sprites):
                    self.curr =0 
                    self.IsAnimate = False
                self.image = self.sprites[int(self.curr)]

clock = pygame.time.Clock()

def main():
    run = True
    clock.tick(60)
    player = Player(800,200)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            key = pygame.key.get_pressed() 
            if key[pygame.K_q]:
                player.animate()
            elif key[pygame.K_DOWN]:
                player.y+=100
                if player.y>=HEIGHT:
                    player.y-=100
            elif key[pygame.K_UP]:
                player.y-=100
                if player.y<0:
                    player.y+=100
            elif key[pygame.K_RIGHT]:
                player.x+=100
                if player.x>=WIDTH:
                    player.x-=100
            elif key[pygame.K_LEFT]:
                player.x-=100
                if player.x<0:
                    player.x+=100
        
        player.update()
        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()
