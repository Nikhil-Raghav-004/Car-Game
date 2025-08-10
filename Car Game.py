import pygame


pygame.init()

width = 1000
height = 650

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame basics")

running = True

#
# background_color = pygame.Color("#39b4a2")
clocl = pygame.time.Clock()

Grass = pygame.image.load("assets/Tiles/Grass/land_grass11.png")
Grass = pygame.transform.scale(Grass,(width,height))

Road = pygame.image.load("assets/Tiles/Asphalt road/road_asphalt01.png")
Road = pygame.transform.scale(Road,(600,200))

div_width = 20
div_hieght = 100
div_Color = "#9cc0c2"
div_speed = 5
div_gap = 40

lane_center =535
div_y_pos = 0

car1 = pygame.image.load("assets/Cars/car_red_small_3.png")
car1 = pygame.transform.scale(car1,(60,120))
motorcycle1 = pygame.image.load("assets/Motorcycles/motorcycle_black.png")
motorcycle1 = pygame.transform.scale(motorcycle1, (45,120))

car2 = pygame.image.load("assets/Cars/car_blue_small_1.png")
car2 = pygame.transform.scale(car2,(60,120))
car2 = pygame.transform.flip(car2,False,True)
car_x = 400
car_y = 500
car_speed = 5

car2_x,car2_y = 450,40

right_limit = 756
left_limit = 343

mtr1_x,mtr1_y = 670,50
mtr_speed = 6.5

exit_button  = pygame.Rect(450,450,200,60)
resume_button = pygame.Rect(450,350,200,60)


def draw_button():
    pygame.draw.rect(screen,"blue", resume_button,border_radius=20)
    pygame.draw.rect(screen,"red", exit_button, border_radius=20)
    font = pygame.font.SysFont("Papyrus", 42)

    exit_text = font.render("Exit",True,'white')
    resume_text = font.render('Resume',True,'white')

    screen.blit(resume_text,(resume_button.x+25, resume_button.y+5))
    screen.blit(exit_text, (exit_button.x+55,exit_button.y+5))

def pasue_menu():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.collidepoint(event.pos):
                    paused = False
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        pygame.display.update()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and car_x > left_limit:
        car_x = car_x - car_speed
    if keys[pygame.K_RIGHT] and car_x +60 < right_limit :
        car_x += car_speed

    div_y_pos += div_speed

    if div_y_pos >= div_hieght + div_gap:
        div_y_pos = 0


    screen.blit(Grass,(0,0))

    # m_x,m_y = pygame.mouse.get_pos()
    # print(f"x position: {m_x}")



    y_road = 0

    for i in range(4):
        screen.blit(Road,(250,y_road))
        y_road+= 200

        current_y = -60+div_y_pos

    while current_y < height:
        pygame.draw.rect(screen,div_Color,(lane_center,current_y,div_width,div_hieght))
        current_y += div_hieght + div_gap

    car2_y += 5

    if car2_y > height:
        car2_y = -1000

    mtr1_y += mtr_speed
    if mtr1_y > height:
        mtr1_y = -2000



    screen.blit(car1, (car_x,car_y))
    screen.blit(car2,(car2_x,car2_y))
    screen.blit(motorcycle1,(mtr1_x,mtr1_y))

    player_rect = pygame.Rect(car_x, car_y, car1.get_width(),car1.get_height())
    # pygame.draw.rect(screen,"blue", player_rect,2 )

    player_rect2 = pygame.Rect(car2_x,car2_y, car2.get_width(), car2.get_height())
    # pygame.draw.rect(screen, "red", player_rect2,2)

    Player_rect = pygame.Rect(mtr1_x, mtr1_y, motorcycle1.get_width(), motorcycle1.get_height())
    # pygame.draw.rect(screen, "green",Player_rect, 2)

    # colliderect function : checks the collision for two elements
    if player_rect.colliderect(player_rect2) or player_rect.colliderect(Player_rect):

        font = pygame.font.SysFont('Papyrus ',72)
        text = font.render("Game Over!", True, 'black')
        screen.blit(text,(400,200))
        draw_button()
        # pygame.draw.rect(screen,"blue", resume_button)
        # pygame.draw.rect(screen,"red",exit_button )
        pygame.display.update()
        # pygame.time.wait(3000)
        pasue_menu()

        pygame.quit()
    pygame.display.flip()
    clocl.tick(100)