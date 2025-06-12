import pygame
import time
import random
import sys

# Initialize pygame modules
pygame.init()
pygame.font.init()
pygame.mixer.init()

FONT = pygame.font.SysFont("comicsans", 30)

WIDTH, HEIGHT = 1300, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fighter game")

title = pygame.transform.scale(pygame.image.load("Start_pic.png"), (WIDTH, HEIGHT))
bg = pygame.transform.scale(pygame.image.load("Background.png"), (WIDTH, HEIGHT))
p1win = pygame.transform.scale(pygame.image.load("p1win.png"), (WIDTH, HEIGHT))
p2win = pygame.transform.scale(pygame.image.load("p2won.png"), (WIDTH, HEIGHT))

punch = pygame.mixer.Sound("punch.mp3")
c_height = 400
c_width = 400

def draw(player, player2, screen, p1_life, p2_life):
    current_screen = screen
    p1msg = FONT.render(f"Player 1", 1,"Black")
    p2msg = FONT.render(f"Player 2", 1,"Black")
    p1_ins = FONT.render("A-left  D-Right  W-Punch",1,"white")
    p2_ins = FONT.render("J-left  L-Right  I-Punch",1,"white")
    WIN.blit(current_screen, (0, 0))

    if current_screen == bg:
        WIN.blit(player.image, (player.x, player.y))
        WIN.blit(player2.image, (player2.x, player2.y))

        WIN.blit(p1_ins, (10, 750))
        WIN.blit(p2_ins, (950, 750))

        WIN.blit(p1msg, (50, 10))
        WIN.blit(p2msg, (WIDTH - 160, 10))

        # Player 1 health bar
        p1_coord = 50
        for i in range(p1_life):
            rec = pygame.Rect(p1_coord, 55, 50, 30)
            pygame.draw.rect(WIN, "red", rec)
            pygame.draw.line(WIN, "black", rec.topleft, rec.topright, 3)
            pygame.draw.line(WIN, "black", rec.bottomleft, rec.bottomright, 3)
            if i == 0:
                pygame.draw.line(WIN, "black", rec.topleft, rec.bottomleft, 3)
            if i == p1_life - 1:
                pygame.draw.line(WIN, "black", rec.topright, rec.bottomright, 3)
            p1_coord += 50

        # Player 2 health bar
        p2_coord = WIDTH - 100
        for i in range(p2_life):
            rec2 = pygame.Rect(p2_coord, 55, 50, 30)
            pygame.draw.rect(WIN, "red", rec2)
            pygame.draw.line(WIN, "black", rec2.topleft, rec2.topright, 3)
            pygame.draw.line(WIN, "black", rec2.bottomleft, rec2.bottomright, 3)
            if i == 0:
                pygame.draw.line(WIN, "black", rec2.topright, rec2.bottomright, 3)
            if i == p2_life - 1:
                pygame.draw.line(WIN, "black", rec2.topleft, rec2.bottomleft, 3)
            p2_coord -= 50

    if p1_life <= 0:
        WIN.blit(p2win, (0, 0))
        restart_msg = FONT.render("Press R to Restart or any key to Exit", True, "white")
        WIN.blit(restart_msg, (WIDTH // 2 - restart_msg.get_width() // 2, HEIGHT - 60))
    elif p2_life <= 0:
        WIN.blit(p1win, (0, 0))
        restart_msg = FONT.render("Press R to Restart or any key to Exit", True, "white")
        WIN.blit(restart_msg, (WIDTH // 2 - restart_msg.get_width() // 2, HEIGHT - 60))

    pygame.display.update()

class PlayerLeft:
    def __init__(self, x, y, sound):
        self.sprites = []
        self.punch = sound
        self.curr = 0
        self.IsAnimate = False
        for i in range(1, 7):
            self.sprites.append(pygame.transform.scale(pygame.image.load(f"RightChar{i}.png"), (c_width, c_height)))
        self.image = self.sprites[self.curr]
        self.x = x
        self.y = y

    def animate(self):
        self.IsAnimate = True
        self.punch.play()

    def update(self):
        if self.IsAnimate:
            self.curr += 1
            if self.curr == len(self.sprites):
                self.curr = 0
                self.IsAnimate = False
            self.image = self.sprites[int(self.curr)]

class PlayerRight:
    def __init__(self, x, y, sound):
        self.IsAnimate = False
        self.punch = sound
        self.x = x
        self.y = y
        self.sprites = []
        self.curr = 0
        self.image = pygame.transform.scale(pygame.image.load("leftChar1.png"), (c_width, c_height + 30))
        for i in range(1, 4):
            self.sprites.append(pygame.transform.scale(pygame.image.load(f"leftChar{i}.png"), (c_width, c_height + 30)))

    def animate(self):
        self.IsAnimate = True
        self.punch.play()

    def update(self):
        if self.IsAnimate:
            self.curr += 0.7
            if int(self.curr) == len(self.sprites):
                self.curr = 0
                self.IsAnimate = False
            self.image = self.sprites[int(self.curr)]

clock = pygame.time.Clock()

def main():
    def reset_game():
        return 10, 10, PlayerLeft(10, 343, punch), PlayerRight(900, 340, punch), False

    p1_life, p2_life, player, player2, game_over = reset_game()
    run = True
    current_screen = title

    while run:
        clock.tick(60)  #  Keep this inside the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        p1_life, p2_life, player, player2, game_over = reset_game()
                        current_screen = bg
                    else:
                        run = False  # Exit on any key
            else:
                if current_screen == title and event.type == pygame.KEYDOWN and event.key==pygame.K_RETURN:
                    current_screen = bg  # Enter key starts the game

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player.animate()
                        if abs(player.x - player2.x) < c_width / 2:  #  Better hit detection
                            player2.x += 50
                            if p2_life > 0:
                                p2_life -= 1

                    elif event.key == pygame.K_i:
                        player2.animate()
                        if abs(player.x - player2.x) < c_width / 2:
                            player.x -= 50
                            if p1_life > 0:
                                p1_life -= 1

                    elif event.key == pygame.K_d:
                        player.x += 100
                        if player.x + c_width >= WIDTH:
                            player.x -= 100
                    elif event.key == pygame.K_a:
                        player.x -= 100
                        if player.x < 0:
                            player.x += 100
                    elif event.key == pygame.K_j:
                        player2.x -= 100
                        if player2.x < 0:
                            player2.x += 100
                    elif event.key == pygame.K_l:
                        player2.x += 100
                        if player2.x + 300 >= WIDTH:
                            player2.x -= 100

        if p1_life <= 0 or p2_life <= 0:
            game_over = True

        player.update()
        player2.update()
        draw(player, player2, current_screen, p1_life, p2_life)

    pygame.quit()

if __name__ == "__main__":
    main()
