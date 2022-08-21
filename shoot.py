from random import randint

apple = Actor("apple")
score = 0
game_over = False

def draw():
    screen.fill("yellow")
    apple.draw()
    screen.draw.text("Score: "+str(score), color="Black", topleft=(10, 10))
    
def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    
def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        print("Good Shot!")
        place_apple()
        score = score + 10
        print(score)
        draw()
    
    else:
        game_over = True
        print("You missed :(")
        print("Total Score: ", score)
        quit()

place_apple()
