import pygame
import os
import random
import numpy as np



pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# chargement des images 

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))


SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]


CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))


#######################################################################################

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5


    def __init__(self):

        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.done=False
        self.distance=0
        self.arbre=0
        self.type=0
        self.rew=0.1
        
        self.points=0
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS


    #############################
    #reactions aux touches 
    def update(self, userInput):

        

        self.rew=0.1
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput==0 and not self.dino_jump:

            self.dino_run = False
            self.dino_jump = True

        elif not (self.dino_jump or userInput==1):
         
            self.dino_run = True
            self.dino_jump = False

        if len(obstacles) == 0:
            if random.randint(0, 1) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 1) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
        

        for obstacle in obstacles:
            obstacle.update()

            if player.dino_rect.colliderect(obstacle.rect):
                ###print("colision")
                self.done=True
                self.rew=-1
        
        for obstacle in obstacles:
  
            if(obstacle.dis()-player.X_POS<0):
                pass
            else:
                player.distance=obstacle.dis()-player.X_POS
        score(player)


    ################
    # run on prend la bonne image 
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    ##################
    #
    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 1
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))



###############################################################################################
class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

##################################################################################################################
class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)
    def dis(self):
        return self.rect.x

##########################################################################################################################
class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        player.arbre=self.type
        player.type=0
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        player.arbre=self.type
        player.type=1
        super().__init__(image, self.type)
        self.rect.y = 300


def menu():
    global game_speed, x_pos_bg, y_pos_bg, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    obstacles = []
    run=False

#########################################################################


global game_speed, x_pos_bg, y_pos_bg,obstacles
run = True
clock = pygame.time.Clock()
player = Dinosaur()
cloud = Cloud()
game_speed = 20
x_pos_bg = 0
y_pos_bg = 380
obstacles = []
font = pygame.font.Font('freesansbold.ttf', 20)


###########################################################################
# fonctions utiles
def score(player):
    global game_speed
    player.points += 1
    #if player.points % 100 == 0:
        #game_speed += 1

   
    
def scoreDraw(player):
    text = font.render("Points: " + str(player.points), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1000, 40)
    SCREEN.blit(text, textRect)


def background():
    global x_pos_bg, y_pos_bg
    image_width = BG.get_width()
    SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
    SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
    if x_pos_bg <= -image_width:
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        x_pos_bg = 0
    x_pos_bg -= game_speed


############################################################################
def dessiner():
    SCREEN.fill((255, 255, 255))
    player.draw(SCREEN)
  
        

    for obstacle in obstacles:
        obstacle.draw(SCREEN)

        background()
        scoreDraw(player)
        cloud.draw(SCREEN)
        cloud.update()

        
        clock.tick(30)
        pygame.display.update()
      