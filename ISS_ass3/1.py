import pygame
import random
pygame.init()

play =["player1", "player2"]

points = [0, 0]

score = [0, 0]

state=0

lives = [3, 3]

p_color = [(255,0,255),(255,255,0)]

#display window
win = pygame.display.set_mode((500,900))
pygame.display.set_caption("game")

right = False
left = False
up = False
down = False

x = 225
y = 650
width = 50
height = 50
vel = 10

active = [1, 2]

enemy_sprite = ['sprites/1.png','sprites/2.png','sprites/3.png','sprites/4.png','sprites/5.png','sprites/6.png']
static_sprite = ['sprites/11.png','sprites/12.png','sprites/13.png','sprites/14.png','sprites/15.png','sprites/16.png']
enemy_surface = list(range(6))
static_surface = list(range(6))
for i in range(5):
    enemy_surface[i] = pygame.image.load(enemy_sprite[i])
    enemy_surface[i] = pygame.transform.scale(enemy_surface[i],(50,50))
    static_surface[i] = pygame.image.load(static_sprite[i])
    static_surface[i] = pygame.transform.scale(static_surface[i],(50,50))



class obs:
    x = 1
    y = 1 
    width = 50
    height = 50
    vel = 4
    index = 0
r = random.randrange(-20,520)
rv = random.randrange(2, 8)

obs1 = obs()
ind = random.randrange(0,5)
obs1.index = ind
obs1.x = r
obs1.y = 110
obs1.vel = rv





rv = random.randrange(2, 8)
r = random.randrange(-20,520)
ind = random.randrange(1,5)
obs2 = obs()
obs2.index = random.randrange(1,5)

obs2.x = r
obs2.y = 230
obs2.vel = rv

rv = random.randrange(2, 8)
r = random.randrange(-20,520)
obs3 = obs()
ind = random.randrange(1,5)
obs3.index = ind

obs3.x = r
obs3.y = 350
obs3.vel = rv

rv = random.randrange(2, 8)
r = random.randrange(-20,520)
ind = random.randrange(1,5)
obs4 = obs()
obs4.index = ind

obs4.x = r
obs4.y = 470
obs4.vel = rv

r = random.randrange(0,450)
s_ob1 = obs()
ind = random.randrange(0,5)
s_ob1.index = ind
s_ob1.x = r
s_ob1.y = 170


r = random.randrange(0,450)
s_ob2 = obs()
ind = random.randrange(0,5)
s_ob2.index = ind
s_ob2.x = r
s_ob2.y = 290

r = random.randrange(0,450)
s_ob3 = obs()
ind = random.randrange(0,5)
s_ob3.index = ind
s_ob3.x = r
s_ob3.y = 410

r = random.randrange(0,450)
s_ob4 = obs()
ind = random.randrange(0,5)
s_ob4.index = ind
s_ob4.x = r
s_ob4.y = 530



def disp():
    
    win.fill((0, 0, 0))
    win.blit(background, (0,0))
    pygame.draw.rect(win, (0,0,0), (0, 700, 500, 300))
    str = "player1 score:{} lives:{}".format(score[0]*100 + points[0], lives[0], )
    #font = pygame.font.Font('freesanbold.ttf', 32)
    txt1 = myfont.render(str, 1, (100,200,250))
    win.blit(txt1,(0, 800))
    str = "player2 score:{} lives:{}  ".format(score[1]*100 + points[1], lives[1])
    #font = pygame.font.Font('freesanbold.ttf', 32)
    txt1 = myfont.render(str, 1, (100,200,250))
    win.blit(txt1,(0, 850))
    str = "Active player: {}".format(active[state]) 
    #font = pygame.font.Font('freesanbold.ttf', 32)
    txt1 = myfont.render(str, 1, (100,200,250))
    win.blit(txt1,(0, 750))

    #pygame.draw.rect(win, p_color[state], (x, y, width, height))
    win.blit(player, (x, y))
    # pygame.draw.rect(win, (0, 0, 255), (obs1.x, obs1.y, obs1.width, obs1.height))
    # pygame.draw.rect(win, (0, 0, 255), (obs2.x, obs2.y, obs2.width, obs2.height))
    win.blit(enemy_surface[obs1.index], (obs1.x, obs1.y))
    win.blit(enemy_surface[obs2.index], (obs2.x, obs2.y))
    win.blit(enemy_surface[obs3.index], (obs3.x, obs3.y))
    win.blit(enemy_surface[obs4.index], (obs4.x, obs4.y))
    win.blit(static_surface[s_ob1.index], (s_ob1.x, s_ob1.y))
    win.blit(static_surface[s_ob2.index], (s_ob2.x, s_ob2.y))
    win.blit(static_surface[s_ob3.index], (s_ob3.x, s_ob3.y))
    win.blit(static_surface[s_ob4.index], (s_ob4.x, s_ob4.y))
    # pygame.draw.rect(win, (0, 0, 255), (obs3.x, obs3.y, obs3.width, obs3.height))
    # pygame.draw.rect(win, (0, 0, 255), (obs4.x, obs4.y, obs4.width, obs4.height))
    # pygame.draw.rect(win, (0, 255, 255), (s_ob1.x, s_ob1.y, s_ob1.width, s_ob1.height))
    # pygame.draw.rect(win, (0, 255, 255), (s_ob2.x, s_ob2.y, s_ob2.width, s_ob2.height))
    # pygame.draw.rect(win, (0, 255, 255), (s_ob3.x, s_ob3.y, s_ob3.width, s_ob3.height))
    # pygame.draw.rect(win, (0, 255, 255), (s_ob4.x, s_ob4.y, s_ob4.width, s_ob4.height))
    
    pygame.display.update()

myfont = pygame.font.SysFont("comicsans", 30)

def reset_player():
    global x
    global y 
    global lives
    global state
    x = 225
    lives[state] -= 1
    
    if lives[state] == 0:
       
        state += 1
        state %= 2
        y = 650 - state*650
        print ("chod ", y)
    else :
        y = 650 - state*650
    

def success():
    
    
    global x
    global y 
    global lives
    global state
    win.fill((100,100,100))
    s = "player {} finished".format(state+1)
    #font = pygame.font.Font('freesanbold.ttf', 32)
    t = myfont.render(s, 1, (00,10,10))
    win.blit(t,(20, 200))
    pygame.display.update()
    pygame.time.delay(500)
    x = 225
    print(lives[state])
    score[state] += 1  
    state += 1
    state %= 2
    if lives[state] ==0:
        state += 1
        state %= 2
    if state == 0:
        y = 650
    else :
        y = 0
flag =0

def collision_detect(obs1):
    global state
    if abs(x - obs1.x) >= 0 and abs(x - obs1.x )<= 50 and abs( y - obs1.y) >= 0 and abs(y-obs1.y) <= 50 :
        
        win.fill((100,100,100))
        s = "player {} died".format(state+1)
        #font = pygame.font.Font('freesanbold.ttf', 32)
        t = myfont.render(s, 1, (00,10,10))
        win.blit(t,(20, 200))
        pygame.display.update()
        pygame.time.delay(500)
        reset_player()
        
run = True

def conclude():
    win.fill((100,100,100))
    if score[0] > score[1]:
        s = "player1 won"
    else:
        s = "player2 won"
    #font = pygame.font.Font('freesanbold.ttf', 32)
    t = myfont.render(s, 1, (00,10,10))
    win.blit(t,(20, 200))
    pygame.display.update()
    pygame.time.delay(500)
    i = 0
while run:
    i += 1
    if i%20 == 0:
        points[state] -= 1
    print (state, x, y)
    
    play_img = ['./sprites/p_up.png','./sprites/p_down.png']

    background = pygame.image.load('bg.jpeg')
    player = pygame.image.load(play_img[state])
    player = pygame.transform.scale(player, (50, 50))
    

    if y==0 and state == 0:

        success()
    if y==650 and state ==1:
        success()
    if lives[state] == 0 :
        state += 1
        state %= 2
    if lives[0] == 0 and lives[1] == 0:
        conclude()
        if  (score[0]>score[1]):
            print ("player 1")
        else:
            print("player 2")
        run = False
    if lives[state] == 0:
        state+= 1
        state%= 2
    pygame.time.delay(50)
    collision_detect(obs1)
    collision_detect(obs2)
    collision_detect(obs3)
    collision_detect(obs4)
    collision_detect(s_ob1)
    collision_detect(s_ob2)
    collision_detect(s_ob3)
    collision_detect(s_ob4)

    
    for event in pygame.event.get():
        #quit(close button)
        if event.type == pygame.QUIT:
            run = False
    
    #moving obstacles
    obs1.x += obs1.vel + 2*(score[state])
    obs2.x += obs2.vel + 2*(score[state])
    obs3.x += obs3.vel + 2*(score[state])
    obs4.x += obs4.vel + 2*(score[state])

    if obs1.x > 520:
        obs1.x-=540
    if obs2.x > 520:
        obs2.x-=540
    if obs3.x > 520:
        obs3.x-=540
    if obs4.x > 520:
        obs4.x-=540
    move = pygame.key.get_pressed()
    if (move[pygame.K_LEFT] and state == 0) or (move[pygame.K_a] and state ==1):
        if (x > 0):
            x -= vel
        
    if (move[pygame.K_RIGHT] and state == 0) or (move[pygame.K_d] and state ==1) :
        if(x < 500 - width ):
            x +=  vel
        
    if (move[pygame.K_UP] and state == 0) or (move[pygame.K_w] and state ==1) : 
        if (y > 0):
            if state == 0 and (y - 110)%60 ==0:
                points[state]+=5
            y-=vel
        
    if (move[pygame.K_DOWN] and state == 0) or (move[pygame.K_s] and state ==1):
        if (y < 700-height):
            y+=vel
            if state == 1 and (y - 110)%60 ==0:
                points[state]+=5
        
    disp()
    

    #text = font.render(str, (255, 0 , 0))
    #textRect = text.get_rect()
     

pygame.quit()