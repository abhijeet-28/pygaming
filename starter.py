import pygame,time,random
from collections import Counter
pygame.init()
max_width=600
max_height=500
gameDisplay=pygame.display.set_mode((max_width,max_height))
pygame.display.set_caption("snake")

font_chosen_small=pygame.font.SysFont("comicsansms",25)
font_chosen_medium=pygame.font.SysFont("comicsansms",45)
font_chosen_large=pygame.font.SysFont("monospace",60)
	

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
yellow=(255,255,0)
snake_size=20
apple_size=10
clock=pygame.time.Clock()
direction="down"

snakehead=pygame.image.load('final.png')



def write_text(message,color,size,offset):
	if(size=="small"):

		rendering=font_chosen_small.render(message,True,color)
	elif(size=="medium"):
		rendering=font_chosen_medium.render(message,True,color)
	else:
		rendering=font_chosen_large.render(message,True,color)
	area=rendering.get_rect()
	area.center=max_width/2,max_height/2+offset
	gameDisplay.blit(rendering,area)

def snakecheck(all_points):
	seen=[]
	for pt in all_points:
		if(pt in seen):
			return False
		else:
			seen.append(pt)
	return True

def snakecheck2(all_points):
	head=all_points[-1]
	for i in range(0,len(all_points)-1):
		if(head==all_points[i]):
			return False
	return True


def snake(points):
	
	if(direction=="right"):
		snakehead_disp=pygame.transform.rotate(snakehead,90)
	elif(direction=="left"):
		snakehead_disp=pygame.transform.rotate(snakehead,270)
	elif(direction=="up"):
		snakehead_disp=pygame.transform.rotate(snakehead,180)
	else:
		snakehead_disp=snakehead

	gameDisplay.blit(snakehead_disp,(points[-1][0],points[-1][1]))
	for point in points[:-1]:
		pygame.draw.rect(gameDisplay,black,[point[0],point[1],snake_size,snake_size])




def start_game():
	starting=True
	while(starting==True):
		gameDisplay.fill(yellow)
		write_text("Welcome to snake game",green,"medium",0)
		write_text("Press space to play",red,"small",40)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if(event.key==pygame.K_SPACE):
					starting=False
		




def loop():
	global direction
	all_points=[]
	snakelength=1
	x=200
	y=200
	speed_x=0
	speed_y=0
	speed=10

	pygame.display.update()

	exit=False
	end=False

	apple_x=(random.randrange(0,max_width)/10)*10
	apple_y=(random.randrange(0,max_height)/10)*10

	while not exit:
		pygame.display.set_caption(str(apple_x)+" "+str(apple_y) )

		while(end==True):
			write_text("Game over :)",red,"large",0)
			write_text("Press space key to play again",red,"medium",60)
			all_points=[]
			pygame.display.update()
			for event in pygame.event.get():
				if(event.type==pygame.KEYDOWN):
					if(event.key==pygame.K_ESCAPE):
						end=False
						exit=True
						break
					elif(event.key==pygame.K_SPACE):
						exit=False
						end=False
						loop()

		for event in pygame.event.get():
			
			if event.type==pygame.QUIT:
				end=True
				exit=True
			if event.type==pygame.KEYDOWN:
				if(event.key==pygame.K_ESCAPE):
					exit=True
					
				if(event.key==pygame.K_LEFT):
					speed_x=-speed
					speed_y=0
					direction="left"
				elif(event.key==pygame.K_RIGHT):
					speed_x=speed
					speed_y=0
					direction="right"
				elif(event.key==pygame.K_UP):
					speed_x=0
					speed_y=-speed
					direction="up"
				elif(event.key==pygame.K_DOWN):
					speed_x=0
					speed_y=speed
					direction="down"
		if(x+snake_size+speed_x>=max_width and speed_x>0):
			end=True
		if(x+speed_x<=0 and speed_x<0):
			end=True
		if(y+snake_size+speed_y>=max_height and speed_y>0):
			end=True
		if(y+speed_y<0 and speed_y<0):
			end=True
		x+=speed_x
		y+=speed_y
		
		start_point=[x,y]

		all_points.append(start_point)
		
		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay,red,[apple_x,apple_y,apple_size,apple_size])

		if(len(all_points)>snakelength):
			del all_points[0]
		
		# if(len(list(set(all_points))) != len(all_points)):
		# 	end=True
		print start_point
		print all_points
		print "---"
		
		check=snakecheck2(all_points)
		if(check==False):
			end=True

		
		snake(all_points)
		pygame.display.update()

		# if(x==apple_x and y==apple_y):
		# 	apple_x=(random.randrange(0,max_width)/10)*10
		# 	apple_y=(random.randrange(0,max_height)/10)*10
		# 	snakelength+=1


		# if(x>=apple_x and x<=apple_x+apple_size):
		# 	if(y>=apple_y and y<apple_y+apple_size):
		# 		apple_x=(random.randrange(0,max_width)/10)*10
		# 		apple_y=(random.randrange(0,max_height)/10)*10
		# 		snakelength+=1

		isCollision=True
		if(apple_x+apple_size<=x):
			isCollision=False
		elif(apple_x>=x+snake_size):
			isCollision=False
		else:
			if(apple_y+apple_size<=y):
				isCollision=False
			elif(y+snake_size<=apple_y):
				isCollision=False

		if(isCollision==True):
			apple_x=(random.randrange(0,max_width)/10)*10
			apple_y=(random.randrange(0,max_height)/10)*10
			snakelength+=1


		clock.tick(30)
	pygame.quit()
	quit()
start_game()
loop()
write_text("You lose",red)
pygame.display.update()

