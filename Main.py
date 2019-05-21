import pygame

pygame.init()
window=pygame.display.set_mode((1920,1080))

pygame.display.set_caption("Cubes Game")

WalkRight=[pygame.image.load('right_1.png'),pygame.image.load('right_2.png'),pygame.image.load('right_3.png'),pygame.image.load('right_4.png'),pygame.image.load('right_5.png'),pygame.image.load('right_6.png')]
WalkLeft=[pygame.image.load('left_1.png'),pygame.image.load('left_2.png'),pygame.image.load('left_3.png'),pygame.image.load('left_4.png'),pygame.image.load('left_5.png'),pygame.image.load('left_6.png')]
PlayerStand=pygame.image.load('idle.png')
backGround=pygame.image.load('bg.jpg')

clock=pygame.time.Clock()

x=0
y=650
width=213
height=430
speed=15

isJump=False
jumpCount=10

left=False
right=False
animCount=0
lastMove="right"

class projectile():
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=8*facing
    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)

def drawWindow():
    global animCount
    window.blit(backGround, (0, 0))

    if animCount+1>=30:
        animCount=0

    if left:
        window.blit(WalkLeft[animCount//5],(x,y))
        animCount+=1
    elif right:
        window.blit(WalkRight[animCount//5],(x,y))
        animCount+=1
    else:
        window.blit(PlayerStand,(x,y))

    for bullet in bullets:
        bullet.draw(window)

    pygame.display.update()

run=True
bullets=[]
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False


    for bullet in bullets :
        if bullet.x<1920 and bullet.x>0:
            bullet.x +=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys=pygame.key.get_pressed()

    if keys[pygame.K_f] :
        if lastMove=="right":
            facing=1
        else:
            facing=-1

        if len(bullets) < 10:

            bullets.append(projectile(round(x+width//2),round(y+height//2),5,(255,0,0),facing))


    if keys[pygame.K_LEFT] and x>5:
        x -=speed
        left=True
        right=False
        lastMove="left"
    elif keys[pygame.K_RIGHT] and x< 1920 - width -5:
        x +=speed
        left=False
        right=True
        lastMove="right"
    else:
        left=False
        right=False
        animCount=0
    if not(isJump):
        if keys[pygame.K_SPACE]:
           isJump=True
    else:
        if jumpCount >=-10:
            if jumpCount<0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2)/2
            jumpCount-=1
        else:
            isJump=False
            jumpCount=10


    drawWindow()



pygame.quit()