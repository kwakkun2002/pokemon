import pygame as pg
pg.init()

display_width=800
display_height=600

ourScreen=pg.display.set_mode((display_width,display_height))
pg.display.set_caption('파이게임')
myImg=pg.image.load("coil.png")

def myimg(x,y):
    ourScreen.blit(myImg,(x,y))

x=(display_height*0.5)
y=(display_width*0.5)

finish=False
while not finish:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            finish=True
    ourScreen.fill((255,255,255))
    myimg(x,y)
    pg.display.flip()
pg.quit()
quit()


















