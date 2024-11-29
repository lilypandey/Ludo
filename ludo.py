import pygame
import random
import  time
pygame.init()
width_screen,height_screen = 1000, 700
screen = pygame.display.set_mode((width_screen,height_screen))
pygame.display.set_caption('Ludo: You vs Computer')

#colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
yellow=(255,255,0)
grey = (150, 150, 150)
length_pathway = 40


#function to draw tokens in a teardrop shape
def draw_tokens(color, c_tx, c_ty, w_tx, h_ty):
    pygame.draw.ellipse(screen, color, [c_tx-(w_tx//2), c_ty-(2*h_ty), w_tx, h_ty], 0)
    pygame.draw.ellipse(screen, black, [c_tx-(w_tx//2), c_ty-(2*h_ty), w_tx, h_ty], 2)
    point1 = (c_tx-(w_tx//2),c_ty-h_ty)
    point2 = (c_tx+(w_tx//2),c_ty-h_ty)
    point3 = (c_tx, c_ty)
    pygame.draw.polygon(screen, color, [point1, point2, point3], 0)
    pygame.draw.polygon(screen, black, [point1, point2, point3], 2)
    
    
turn = "user"

#dice_coordinates
x_dice1 = 50
x_dice2 = 850
y_dice1 = 480
y_dice2 = 120
width_dice = 100
height_dice = 100
dice_value1 = 1
dice_value2 = 1
dice_rect1 = pygame.Rect(x_dice1, y_dice1, width_dice, height_dice)
dice_rect2 = pygame.Rect(x_dice2, y_dice2, width_dice, height_dice)

#function to draw the dice
def draw_dice(dice_rect, dice_value):
    pygame.draw.rect(screen, black, dice_rect)
    c_dx, c_dy = dice_rect.center
    dot_position = {
        1: [(c_dx,c_dy)], 
        2: [(c_dx-25, c_dy-25), (c_dx+25, c_dy+25)], 
        3: [(c_dx-25, c_dy-25), (c_dx,c_dy), (c_dx+25, c_dy+25)], 
        4: [(c_dx-25, c_dy-25), (c_dx+25, c_dy-25), (c_dx-25, c_dy+25), (c_dx+25, c_dy+25)], 
        5: [(c_dx-25, c_dy-25), (c_dx+25, c_dy-25), (c_dx-25, c_dy+25), (c_dx+25, c_dy+25), (c_dx, c_dy)], 
        6:[(c_dx-25, c_dy-25), (c_dx+25, c_dy-25), (c_dx-25, c_dy+25), (c_dx+25, c_dy+25), (c_dx-25, c_dy),(c_dx+25,c_dy)]}
    
    for dot in dot_position[dice_value]:
        pygame.draw.circle(screen, white, dot, 7)
    
user_dice_clicked = False  
computer_roll_time = None  
user_dice_updated = False
    
#main loop
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN and turn == "user":
            if dice_rect1.collidepoint(e.pos) and not user_dice_clicked:
                dice_value1 = random.randint(1, 6)  
                print(f"user rolled: {dice_value1}")
                user_dice_clicked = True  
                user_dice_updated = True  
                computer_roll_time = time.time() + 3 

    if user_dice_clicked and time.time() >= computer_roll_time and user_dice_updated:
        dice_value2 = random.randint(1, 6) 
        print(f"computer rolled: {dice_value2}")
        turn = "user"  
        user_dice_clicked = False  
        user_dice_updated = False
    

    screen.fill(white)

    #coloring each quadrant 
    quadrant = [(red, (200, 50, 240, 240)), (green, (560, 50, 240, 240)), (blue, (200, 410, 240, 240)), (yellow, (560, 410, 240, 240))]
    for color_quadrant, dimension_quadrant in quadrant:
        pygame.draw.rect(screen, color_quadrant, dimension_quadrant)
        pygame.draw.rect(screen, black, dimension_quadrant, 2)
    
    #for white part in each colored quadrant
    block = [(250, 100, 140, 140),(610, 100, 140, 140), (250, 460, 140, 140), (610, 460, 140, 140)]
    for dimension_block in block:
        pygame.draw.rect(screen, white, dimension_block)
        pygame.draw.rect(screen, black, dimension_block, 2)

    #circles for placing tokens inside the blocks in quadrants
    token_holder =  [(red, [(280, 130), (360, 130), (280, 210), (360, 210)]), (green, [(640, 130), (720, 130), (640, 210), (720, 210)]), (blue, [(280, 490), (360, 490), (280, 570), (360, 570)]), (yellow,[(640, 490), (720, 490), (640, 570), (720, 570)])]
    for color_holder, center_holder in token_holder:
        for cen_holder in center_holder:
            pygame.draw.circle(screen, color_holder, cen_holder, 10, 0)
            pygame.draw.circle(screen, black, cen_holder, 10, 2)
    
    #for triangular part in the middle of board
    triangle = [(green, ((440,290),(560, 290),(500, 350))),  (red, ((440,290),(440, 410),(500, 350))), (blue, ((440, 410),(560, 410),(500, 350))), (yellow, ((560, 410),(560, 290),(500, 350)))]
    for color_triangle,dimension_triangle in triangle:
        pygame.draw.polygon(screen, color_triangle, dimension_triangle, 0)
        pygame.draw.polygon(screen, black, dimension_triangle, 2)

    #for the colored pathway in the board
    for x in range(240, 440, length_pathway):
        pygame.draw.rect(screen, red, (x,330, length_pathway, length_pathway))

    for x in range(560, 760, length_pathway):
        pygame.draw.rect(screen, yellow, (x,330, length_pathway, length_pathway))

    for y in range(90, 290, length_pathway):
        pygame.draw.rect(screen, green, (480,y, length_pathway, length_pathway))

    for y in range(410, 610, length_pathway):
        pygame.draw.rect(screen, blue, (480, y, length_pathway, length_pathway))

    safe_colored_position = [(red, (240, 290, length_pathway, length_pathway)), (yellow, (720, 370, length_pathway, length_pathway)), (green, (520, 90, length_pathway, length_pathway)), (blue, (440, 570, length_pathway, length_pathway))]
    for safe_color, safe_position in safe_colored_position:
        pygame.draw.rect(screen, safe_color, safe_position)

    safe_zone = [(440, 130, length_pathway, length_pathway), (280, 370, length_pathway, length_pathway),(680, 290, length_pathway, length_pathway),(520, 530, length_pathway, length_pathway)]
    for safe_zone_position in safe_zone:
        pygame.draw.rect(screen, grey, safe_zone_position)

    #making the pathway in the board
    for x in range(440, 540, length_pathway):
        for y in range(610, 370, -length_pathway):
            pygame.draw.rect(screen, black, (x, y, length_pathway, length_pathway), 1)
    for y in range(290, 410, length_pathway):
        for x in range(200, 440, length_pathway):
            pygame.draw.rect(screen, black, (x, y, length_pathway, length_pathway), 1)

    for y in range(290, 410, length_pathway):
        for x in range(560, 800, length_pathway):
            pygame.draw.rect(screen, black, (x, y, length_pathway, length_pathway), 1)

    for x in range(440, 540, length_pathway):
        for y in range(50, 290, length_pathway):
            pygame.draw.rect(screen, black, (x, y, length_pathway, length_pathway), 1)

    #to keep the screen where  dices appear black
    #pygame.draw.rect(screen, black, (750,0,250,750))

    #this is for function to draw tokens at their home position
    tokens = [(green, [(640, 130), (720, 130), (640, 210), (720, 210)]), (blue, [(280, 490), (360, 490), (280, 570), (360, 570)])]
    
    for color_token, token in tokens:
        for shape in token:
            draw_tokens(color_token, *shape, 12, 14)

    #function to draw dice
    
    draw_dice(dice_rect2, dice_value2)
    draw_dice(dice_rect1, dice_value1)
    
    pygame.display.update()

pygame.quit()