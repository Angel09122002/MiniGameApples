import pygame
import sys
import random
#init means initialize.
#first, start pygame using the function init().

pygame.init()

#create a variable that contains the screen of the game
#pygame.display.set_mode((350, 600), im creating a a module to control the the display of the game and update the screen content.
#a tuple is a data structure similar to a list, but tuples are immutable, meaning it cannot be change after the tuple is created.
#set_module is a function to create a window or screen, using a tuple  to set the whith and heigh of the screen.

screen = pygame.display.set_mode((350, 600))
clock = pygame.time.Clock()#this will set the fps of the game.
running = True # boolean, true or false.

#classes
class Apple:
     def __init__(self, image, position, speed):
          self.image = image
          self.rect = self.image.get_rect(topleft = position)
          self.speed = speed

     def move(self):
          self.rect.y += self.speed
#variables
speed = 3
score = 0
#constants
TILESIZE = 32

#floor
floor_img = pygame.image.load("apple_game/assets/floor.png"). convert_alpha()
floor_img = pygame.transform.scale(floor_img,(TILESIZE*15, TILESIZE*5))
floor_rect = floor_img.get_rect(bottomleft = (0, screen.get_height()))#create a variable, the content of the variable will be the img tha we want to position, then especify where in the rect the img will be display(bottonleft)


#player
player_img = pygame.image.load("apple_game/assets/player_static.png").convert_alpha()# .convert_alpha() this method optimize the load of the img.

player_img = pygame.transform.scale(player_img,(TILESIZE, TILESIZE*2))

player_rect = player_img.get_rect(center = (screen.get_width()/2,
                                            screen.get_height()-floor_img.get_height()-(player_img.get_height()/2)))

#apple
apple_img =pygame.image.load("apple_game/assets/apple.png").convert_alpha()
apple_img = pygame.transform.scale(apple_img,(TILESIZE, TILESIZE))
apples= [
     Apple(apple_img,(100,0), 3),
     Apple(apple_img,(300,0), 3),
]

#Fonts
font = pygame.font.Font('apple_game/assets/PixeloidMono.ttf', TILESIZE//2)
#sounds
pickup = pygame.mixer.Sound("apple_game/assets/powerup.mp3")
pickup.set_volume(0.1)
#game loop, a loop is necessary to keep the window of the game open.

#The indentation is crucial, if the code is outside the indentation is not going to be part of the loop.

def update():
     global speed
     global score
     keys = pygame.key.get_pressed()
     if keys[pygame.K_LEFT]:
          player_rect.x -= 8
     if keys[pygame.K_RIGHT]:
          player_rect.x += 8

     #apple management

     for apple in apples:
          apple.move()
          if apple.rect.colliderect(floor_rect):
               apples.remove(apple)
               apples.append(Apple(apple_img,(random.randint(50,300),-50),speed))

          elif apple.rect.colliderect(player_rect):
               apples.remove(apple)
               apples.append(Apple(apple_img,(random.randint(50,300),-50),speed))
               speed += 0.2
               score += 1
               pickup.play()
def draw():
     screen.fill((173, 216, 230))
     screen.blit(floor_img, floor_rect)
     screen.blit(player_img, player_rect)

     for apple in apples:
          screen.blit(apple.image, apple.rect)


     score_text = font.render(f"Score: {score}", True, "white")
     screen.blit(score_text,(5, 5))
#game loop
while running:
     #for loops are limited. While loops are unlimited
    #pygame.event.get is a method used to know if there are any interaction, like a handleEvent.
        for event in pygame.event.get(): # this line checked any interactions one by one.
            if event.type == pygame.QUIT:# this line has another condition, IF event.type is equal to pygame.QUIT the game ends.
                pygame.quit()
                sys.exit()
        update()
        draw()

        clock.tick(60)
        pygame.display.update()#update  method is used to update the content of the display.
        #outside the loop.