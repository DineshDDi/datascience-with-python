import  pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()
#Declare the colors using thier RGB codes
orangecolor = (255,123,7)
blackcolor = (0,0,0)
redcolor = (213,50,80)
greencolor = (0,255,0)
bluecolor = (50,153,213)
#Display the window's width and height
display_width=600
display_height=400
dis = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("snake game")
snake_block = 10
snake_speed = 15
snake_list = []
#defines the snake's structure and postion
def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orangecolor, [x[0], x[1], snake_block, snake_block])

#main function
def snakegame():
    game_over = False
    game_end = False
   #co-ordinates of the snake
    x1 = display_width/2
    y1 = display_height/2
   #when the snake moves
    x1_change = 0
    y1_change = 0
    #define the lenth of the snake
    snake_list = []
    Length_of_the_snake = 1

    #the co-ordinates of the food element
    foodx = round(random.randrange(0,display_width - snake_block)/10.0)*10.0
    foody = round(random.randrange(0,display_height - snake_block)/10.0)*10.0

    while not game_over:
        while game_end == True:
            #for displaying the score
            score = Length_of_the_snake - 1
            score_font = pygame.font.SysFont("comicsansms",35)
            value = score_font.render("your score: "+ str(score) ,True,greencolor)
            dis.blit(value,[display_width / 3, display_height / 5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame .KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True
        # updetes the co=ordinates with change postions
        x1 += x1_change
        y1 += y1_change
        dis.fill(blackcolor)
        pygame.draw.rect(dis,greencolor,[foodx,foody,snake_block,snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        # when the length of the snake exceeds,delete the snake_list which will the end game
        if len(snake_list) > Length_of_the_snake:
            del snake_list[0]
        # when the snake hits itself,game ends
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_end = True
        snake(snake_block,snake_list)
        pygame.display.update()
        # when snake hits the food,length of the snake increased by 1
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_the_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


snakegame()


