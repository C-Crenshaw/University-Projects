# Carson Crenshaw, cgc8gdt
# Vanessa Rossi, ndc9pz
# Final Project Checkpoint 1
# Game Description: For the purposes of this project, the game will be structured around a first-person point-of-view basketball shooter. Similar to that of shooting free-throw points during a regulation basketball game or a standard basketball arcade game, two players will compete over scoring the most points in under sixty seconds. Both players will be tasked with shooting as many baskets as possible during the designated time period (with each basket totalling one point). When the time concludes, the player with the most points will be deemed the winner. For added complexity, the remaining thirty seconds of the game will involve random opposing basketball players who will emerge and attempt to block the shots of Player 1 and Player 2.

# Three Basic Features
# User Input: Both players will have the ability to move left and right, as well as make the basketball shot. For Player 1, the user will operate the left and right arrow keys to control the aim of the basketball, as well as the up arrow to shoot. Player 2 will use the W, A, and D keys to play. The W key will cause Player 2 to shoot, with the D key shifting the aim to the right and the A key shifting the aim to the left.
# Game Over: The game will be over when the timer runs out after 1 minute. One basket is the equivalent of one point. Whoever has the most points at the end of the time will be declared winner. When the game ends, the players will be shown a game over screen that also notes who won the game.
# Graphics/Image: The background image for this game will be a basketball court that is centered on three baskets. Player 1 and Player 2 will both be represented by one image of an emoji basketball player (differentiated by the color of the player) and the enemy will be a large turkey representing Virginia Tech. The basketballs the players are shooting will be a simple graphic of a standard basketball. Text will be used to represent the timer and the score totals.

# Four Additional Features – Enemies, Timer, Two Players, Restart from Game Over
# Enemies: Enemies will be a large turkeys who will appear on the screen during the last 50 seconds of the competition. The enemies will move across the screen, and if the basketball that Player 1 or Player 2 shoots hits the enemy, the ball will disappear and the score for that player will revert to zero.
# Timer: There will be a one-minute timer displayed on the screen.  Once the timer reaches 0, the game will stop and the winner will be declared.
# Two Players: The game will involve two players who are simultaneously shooting basketballs into a basket, competing to see who can make the most baskets. The two players will play on the same keyboard, using their respective key controls (see above).
# Restart from Game Over:  After the timer stops and announces the winner and “Game Over” on the final screen of the game, there will also be an option to restart the game. This will be represented by pressing the "R" key for "Restart."

import pygame
import uvage as gamebox
import random

camera = gamebox.Camera(800, 600)
clock = pygame.time.Clock()

# CHARACTERS
class Player1:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = 2
    def draw(self):
        player_images = gamebox.load_sprite_sheet("player1spritesheet.png", 1, 2)
        walker = gamebox.from_image(self.x, self.y, player_images[-1])
    def no_movement(self):
        self.x = self.x
        player_images = gamebox.load_sprite_sheet("player1spritesheet.png", 1, 2)
        walker = gamebox.from_image(self.x, self.y, player_images[-1])
        camera.draw(walker)
    def move_left(self):
        self.x -= self.speed
        player_images = gamebox.load_sprite_sheet("player1spritesheet.png", 1, 2)
        walker = gamebox.from_image(self.x, self.y, player_images[-2])
        camera.draw(walker)
    def move_right(self):
        self.x += self.speed
        player_images = gamebox.load_sprite_sheet("player1spritesheet.png", 1, 2)
        walker = gamebox.from_image(self.x, self.y, player_images[-1])
        camera.draw(walker)
class Player2:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = 2
    def draw(self):
        player_images = gamebox.load_sprite_sheet("player2spritesheet.png", 1, 2)
        walker = gamebox.from_image(self.x, self.y, player_images[-1])
    def no_movement(self):
        self.x = self.x
        player_images = gamebox.load_sprite_sheet("player2spritesheet.png", 1, 2)
        walker = gamebox.from_image(self.x, self.y, player_images[-1])
        camera.draw(walker)
    def move_left(self):
        self.x -= self.speed
        player_images = gamebox.load_sprite_sheet("player2spritesheet.png", 1, 2)
        walker = gamebox.from_image(self.x, self.y, player_images[-2])
        camera.draw(walker)
    def move_right(self):
        self.x += self.speed
        player_images = gamebox.load_sprite_sheet("player2spritesheet.png", 1, 2)
        walker = gamebox.from_image(self.x, self.y, player_images[-1])
        camera.draw(walker)

# BASKETBALLS
class Basketball1:
    def __init__(self, x, y):
        self.radius = 20
        self.speed = 5
        self.x = x
        self.y = y
    def update(self):
        self.y -= self.speed
    def draw(self):
        basketballimg = gamebox.from_image(self.x, self.y, "basketball.png")
        camera.draw(basketballimg)
class Basketball2:
    def __init__(self, x, y):
        self.radius = 20
        self.speed = 5
        self.x = x
        self.y = y
    def update(self):
        self.y -= self.speed
    def draw(self):
        basketballimg = gamebox.from_image(self.x, self.y, "basketball.png")
        camera.draw(basketballimg)

basketballs1 = []
basketballs2 =[]
p11 = Player1(600, 500, 50, 30)
p22 = Player2(300, 500, 50, 30)

current_frame = 0

score1 = 0
score2 = 0

timer = 60
game_over = False

counter = 0
enemylist = []

run = True
while run:
    clock.tick(100)

    # BACKGROUND
    camera.clear("black")
    basketballcourt = gamebox.from_image(400, 300, "basketballcourt.jpg")
    camera.draw(basketballcourt)

    # USER CONTROLS
    # Shoot Basketballs one at a time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                basketballs1.append(Basketball1(p11.x + p11.width // 2, p11.y))
            if event.key == pygame.K_w:
                basketballs2.append(Basketball2(p22.x + p11.width // 2, p22.y))

    # Move the basketball shooter aim for player 1 (red)
    p11.draw()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and p11.x > 0: # This also keeps the players on the screen
        p11.move_left()
    elif keys[pygame.K_RIGHT] and p11.x < 765:
        p11.move_right()
    else:
        p11.no_movement()
    # Move the basketball shooter aim for player 2 (blue)
    p22.draw()
    if keys[pygame.K_a] and p22.x > 0:
        p22.move_left()
    elif keys[pygame.K_d] and p22.x < 765:
        p22.move_right()
    else:
        p22.no_movement()
    for b in basketballs1:
        b.update()
        if b.y < 0:
            basketballs1.remove(b)
    for b in basketballs1:
        b.draw()
    for b in basketballs2:
        b.update()
        if b.y < 0:
            basketballs2.remove(b)
    for b in basketballs2:
        b.draw()

    # SCORE COUNTER
    # Left Basket
    for b in basketballs1:
        if (b.x > 150) and (b.x < 210):
            score1 += 0.02
        if (b.x > 150) and (b.x < 210) and (b.y < 200):
            basketballs1.remove(b)
    for b in basketballs2:
        if (b.x > 150) and (b.x < 210):
            score2 += 0.02
        if (b.x > 150) and (b.x < 210) and (b.y < 200):
            basketballs2.remove(b)
    # Middle Basket
    for b in basketballs1:
        if (b.x > 370) and (b.x < 430):
            score1 += 0.015
        if (b.x > 370) and (b.x < 430) and (b.y < 150):
            basketballs1.remove(b)
    for b in basketballs2:
        if (b.x > 370) and (b.x < 430):
            score2 += 0.015
        if (b.x > 370) and (b.x < 430) and (b.y < 150):
            basketballs2.remove(b)
    # Right Basket
    for b in basketballs1:
        if (b.x > 610) and (b.x < 670):
            score1 += 0.015
        if (b.x > 610) and (b.x < 670) and (b.y < 150):
            basketballs1.remove(b)
    for b in basketballs2:
        if (b.x > 610) and (b.x < 670):
            score2 += 0.015
        if (b.x > 610) and (b.x < 670) and (b.y < 150):
            basketballs2.remove(b)

    camera.draw(gamebox.from_text(520, 40, "PLAYER ONE: " + str(int(score1)), 35, "Red", bold=True))
    camera.draw(gamebox.from_text(280, 40, "PLAYER TWO: " + str(int(score2)), 35, "Blue", bold=True))

    # ENEMY
    if timer < 50:
        counter += 1
        places = [180, 400, 640]
        randompoint = random.choice(places)  # Randomize where the turkeys appear
        if counter % 100 == 0:  # Code adapted from the starfield lesson
            randomenemy = gamebox.from_image(randompoint, 300, "blockedshot.png")
            enemylist.append(randomenemy)
        # Code which physically moves the enemies around
        for enemy in enemylist:
            camera.draw(enemy)
        while len(enemylist) > 1:
            for enemy in enemylist:
                enemylist.remove(enemy)
        # Turkeys stop basketball if the ball hits them and score resets to zero
        # Left Basket
        for enemy in enemylist:
            for b in basketballs1:
                if enemy.x == 180 and (b.x > 150) and (b.x < 210) and (b.y > 300) and (b.y < 340):
                    basketballs1.remove(b)
                    score1 = 0
            for b in basketballs2:
                if enemy.x == 180 and (b.x > 150) and (b.x < 210) and (b.y > 300) and (b.y < 340):
                    basketballs2.remove(b)
                    score2 = 0
        # Middle Basket
        for enemy in enemylist:
            for b in basketballs1:
                if enemy.x == 400 and (b.x > 370) and (b.x < 430) and (b.y > 370) and (b.y < 430):
                    basketballs1.remove(b)
                    score1 = 0
            for b in basketballs2:
                if enemy.x == 400 and (b.x > 370) and (b.x < 430) and (b.y > 370) and (b.y < 430):
                    basketballs2.remove(b)
                    score2 = 0
        # Right Basket
        for enemy in enemylist:
            for b in basketballs1:
                if enemy.x == 640 and (b.x > 610) and (b.x < 670) and (b.y > 300) and (b.y < 340):
                    basketballs1.remove(b)
                    score1 = 0
            for b in basketballs2:
                if enemy.x == 640 and (b.x > 610) and (b.x < 670) and (b.y > 300) and (b.y < 340):
                    basketballs2.remove(b)
                    score2 = 0

    # TIMER and GAME OVER
    camera.draw(gamebox.from_text(50, 40, str(int(timer)), 50, "Black", bold=True))

    if game_over == False:
        timer -= 0.010
    if timer < 0:
        game_over = True
        camera.clear("black")
        finishscreen = gamebox.from_text(400, 200, 'GAME OVER', 50, "Red", bold=True)
        camera.draw(finishscreen)
        if score1 > score2:
            player1wins = gamebox.from_text(400, 300, 'PLAYER ONE WINS!', 50, "Red", bold=True)
            camera.draw(player1wins)
        elif score2 > score1:
            player2wins = gamebox.from_text(400, 300, 'PLAYER TWO WINS!', 50, "Blue", bold=True)
            camera.draw(player2wins)
        else:
            tie = gamebox.from_text(400, 300, 'TIE!', 50, "Yellow", bold=True)
            camera.draw(tie)

    # RESTART GAME FROM GAME OVER
    if game_over == True:
        camera.draw(gamebox.from_text(400, 500, "Press R to restart!", 50, "Green", bold=False))
        if keys[pygame.K_r]:
            game_over = False
            timer = 60
            score1 = 0
            score2 = 0
            p11.no_movement()
            p22.no_movement()

    # UPDATE DISPLAY
    pygame.display.update()