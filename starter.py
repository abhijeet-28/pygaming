import pygame
pygame.init()
max_width=600
max_height=500
gameDisplay=pygame.display.set_mode((max_width,max_height))
pygame.display.set_caption("snake")


white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

x=200
y=200
speed_x=0
speed_y=0

pygame.display.update()
exit=False
while not exit:
	pygame.display.set_caption("Snake")
	for event in pygame.event.get():
		
		if event.type==pygame.QUIT:
			exit=True
		if event.type==pygame.KEYDOWN:
			if(event.key==pygame.K_ESCAPE):
				exit=True
			if(event.key==pygame.K_LEFT):
				speed_x=-1
				speed_y=0
			elif(event.key==pygame.K_RIGHT):
				speed_x=1
				speed_y=0
			elif(event.key==pygame.K_UP):
				speed_x=0
				speed_y=-1
			elif(event.key==pygame.K_DOWN):
				speed_x=0
				speed_y=1
	if(x+20>max_width and speed_x>0):
		speed_x=0
	if(x<0 and speed_x<0):
		speed_x=0
	if(y+20>max_height and speed_y>0):
		speed_y=0
	if(y<0 and speed_y<0):
		speed_y=0
	x+=speed_x
	y+=speed_y
	
	
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay,red,[x,y,20,20])
	pygame.display.update()


pygame.quit()
quit()
