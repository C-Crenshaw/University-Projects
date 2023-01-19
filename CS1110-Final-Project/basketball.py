# Carson Crenshaw, cgc8gdt
# Vanessa Rossi, ndc9pz
# Final Project
#Game Description:  This is a two player game.  Player 1 and Player 2 have their respective keyboard controls
# (W, A, S, D, and the arrow keys) which control their player. The objective of the game is to score the most baskets
# before the timer runs out.  For added complexity, there is a turkey, representing the enemy, and when the player
# moves and touches the turkey, their score is reset to zero and the player is placed back to the starting position.
#Three Basic Features:
#[1]User Input:  Player 1 controls their character using the arrow keys, indicating which direction they are moving in.  Player 2 controls their character with W, A, S, D.
#[2]Game Over:  Game ends when the timer runs out, and depending on the score, ends with Player 1 winning, Player 2 winning, or a tie
#[3]Graphics:  Background, Player Images, Enemy
#Four Additional Features:  Restart, Two Players Simaltaneously, Timer, Enemies

import uvage
import random
camera = uvage.Camera(800, 600)

# Define Global Variables that will be referenced throughout the code
current_frame = 0
score1 = 0
score2 = 0
timer = 60
enemylist = []
game_over = False
counter = 0

# PLAYER 1
player_images1 = uvage.load_sprite_sheet("player1spritesheet.png", 1, 2)  # Sprite sheet code modeled from lect31
player1 = uvage.from_image(600, 500, player_images1[-1])

def move_player1(): # Function which controls the movement of player 1
  walker_move = False
  # check which keys are being pressed
  if uvage.is_pressing("up arrow"):
     player1.y -= 3
     walker_move = True
  if uvage.is_pressing("down arrow"):
     player1.y += 3
     walker_move = True
  if uvage.is_pressing("left arrow"):
     player1.x -= 3
     walker_move = True
  if uvage.is_pressing("right arrow"):
     player1.x += 3
     walker_move = True

  if walker_move:
     if uvage.is_pressing("left arrow"):
        player1.image =  player_images1[-2]
  else:
     player1.image = player_images1[-1]

# PLAYER 2
player_images2 = uvage.load_sprite_sheet("player2spritesheet.png", 1, 2)
player2 = uvage.from_image(300, 500, player_images2[-1])

def move_player2(): # Function which controls the movement of player 1
  walker_move = False
  # check which keys are being pressed
  if uvage.is_pressing("w"):
     player2.y -= 3
     walker_move = True
  if uvage.is_pressing("s"):
     player2.y += 3
     walker_move = True
  if uvage.is_pressing("a"):
     player2.x -= 3
     walker_move = True
  if uvage.is_pressing("d"):
     player2.x += 3
     walker_move = True

  if walker_move:
     if uvage.is_pressing("a"):
        player2.image =  player_images2[-2]
  else:
     player2.image = player_images2[-1]

def tick():

    global current_frame
    global score1
    global score2
    global timer
    global game_over
    global enemylist
    global counter

    # BACKGROUND
    camera.clear("black")
    basketballcourt = uvage.from_image(400, 300, "basketballcourt.jpg")
    camera.draw(basketballcourt)

    # PLAYER 1
    move_player1()
    camera.draw(player1)

    # SCORE COUNTER
    # Left Basket
    if (player1.x > 150) and (player1.x < 210) and (player1.y > 125) and (player1.y < 186):
            score1 += 1
            player1.center = [600, 500]
    # Middle Basket
    if (player1.x > 370) and (player1.x < 430) and (player1.y > 125) and (player1.y < 186):
            score1 += 1
            player1.center = [600, 500]
    # Right Basket
    if (player1.x > 610) and (player1.x < 670) and (player1.y > 125) and (player1.y < 186):
            score1 += 1
            player1.center = [600, 500]

    # Store totals from all three baskets (per player)
    camera.draw(uvage.from_text(520, 40, "PLAYER ONE: " + str(int(score1)), 35, "Red", bold=True))

    # PLAYER 2
    move_player2()
    camera.draw(player2)

    # SCORE COUNTER
    # Left Basket
    if (player2.x > 150) and (player2.x < 210) and (player2.y > 125) and (player2.y < 186):
        score2 += 1
        player2.center = [300, 500]
    # Middle Basket
    if (player2.x > 370) and (player2.x < 430) and (player2.y > 125) and (player2.y < 186):
        score2 += 1
        player2.center = [300, 500]
    # Right Basket
    if (player2.x > 610) and (player2.x < 670) and (player2.y > 125) and (player2.y < 186):
        score2 += 1
        player2.center = [300, 500]

    # Store totals from all three baskets (per player)
    camera.draw(uvage.from_text(280, 40, "PLAYER TWO: " + str(int(score2)), 35, "Blue", bold=True))

    # ENEMY
    if timer < 55:
        counter += 1
        places = [180, 400, 640]
        randompoint = random.choice(places)  # Randomize where the turkeys appear
        if counter % 100 == 0:  # Code adapted from the starfield lesson
            randomenemy = uvage.from_image(randompoint, 300, "blockedshot.png")
            enemylist.append(randomenemy)
        # Code which physically moves the enemies around
        for enemy in enemylist:
            camera.draw(enemy)
        while len(enemylist) > 1:
            for enemy in enemylist:
                enemylist.remove(enemy)
        # Turkeys stop basketball if the ball hits them and score resets to zero
        # PLAYER 1
        # Left Basket
        for enemy in enemylist:
            if enemy.x == 180 and (player1.x > 150) and (player1.x < 210) and (player1.y > 300) and (player1.y < 340):
                score1 = 0
                player1.center = [600, 500]
        # Middle Basket
        for enemy in enemylist:
            if enemy.x == 400 and (player1.x > 370) and (player1.x < 430) and (player1.y > 300) and (player1.y < 340):
                score1 = 0
                player1.center = [600, 500]
        # Right Basket
        for enemy in enemylist:
            if enemy.x == 640 and (player1.x > 610) and (player1.x < 670) and (player1.y > 300) and (player1.y < 340):
                score1 = 0
                player1.center = [600, 500]
        #PLAYER 2
        # Left Basket
        for enemy in enemylist:
            if enemy.x == 180 and (player2.x > 150) and (player2.x < 210) and (player2.y > 300) and (player2.y < 340):
                score2 = 0
                player2.center = [300, 500]
        # Middle Basket
        for enemy in enemylist:
            if enemy.x == 400 and (player2.x > 370) and (player2.x < 430) and (player2.y > 300) and (player2.y < 340):
                score2 = 0
                player2.center = [300, 500]
        # Right Basket
        for enemy in enemylist:
            if enemy.x == 640 and (player2.x > 610) and (player2.x < 670) and (player2.y > 300) and (player2.y < 340):
                score2 = 0
                player2.center = [300, 500]

    # TIMER and GAME OVER
    camera.draw(uvage.from_text(50, 40, str(int(timer)), 50, "Black", bold=True))
    if game_over == False:
        timer -= 0.010
    if timer < 0:
        game_over = True
        camera.clear("black")
        finishscreen = uvage.from_text(400, 200, 'GAME OVER', 50, "Red", bold=True)
        camera.draw(finishscreen)
        if score1 > score2:
            player1wins = uvage.from_text(400, 300, 'PLAYER ONE WINS!', 50, "Red", bold=True)
            camera.draw(player1wins)
        elif score2 > score1:
            player2wins = uvage.from_text(400, 300, 'PLAYER TWO WINS!', 50, "Blue", bold=True)
            camera.draw(player2wins)
        else:
            tie = uvage.from_text(400, 300, 'TIE!', 50, "Yellow", bold=True)
            camera.draw(tie)

    # RESTART GAME FROM GAME OVER
    if game_over == True:
        camera.draw(uvage.from_text(400, 500, "Press R to restart!", 50, "Green", bold=False))
        if uvage.is_pressing("r"):
            game_over = False
            timer = 60
            score1 = 0
            score2 = 0

    camera.display()

ticks_per_second = 100

uvage.timer_loop(ticks_per_second, tick)