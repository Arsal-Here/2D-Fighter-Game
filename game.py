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
        self.sprites.append(pygame.image.load("attack_1.png"))
        self.sprites.append(pygame.image.load("attack_2.png"))
        self.sprites.append(pygame.image.load("attack_3.png"))
        self.sprites.append(pygame.image.load("attack_4.png"))
        self.sprites.append(pygame.image.load("attack_5.png"))
        self.sprites.append(pygame.image.load("attack_6.png"))
        self.sprites.append(pygame.image.load("attack_7.png"))
        self.sprites.append(pygame.image.load("attack_8.png"))
        self.sprites.append(pygame.image.load("attack_9.png"))
        self.sprites.append(pygame.image.load("attack_10.png"))

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
            elif key[pygame.K_UP]:
                player.y-=100
            elif key[pygame.K_RIGHT]:
                player.x+=100
            elif key[pygame.K_LEFT]:
                player.x-=100
        
        player.update()
        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()
