import pygame


pygame.init()

width = 1000
height = 700

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame basics")

running = True

#
# background_color = pygame.Color("#39b4a2")

# Grass = pygame.image.load("assets/Tiles/Grass/land_grass11.png")
# Grass = pygame.transform.scale(Grass,(width,height))
#
# Road = pygame.image.load("assets/Tiles/Asphalt road/road_asphalt01.png")
# Road = pygame.transform.scale(Road,(600,200))
#
# div_width = 20
# div_hieght = 60
# div_Color = "9cc0c2"
# div_speed = 5
# div_gap = 40
#
# lane_center = 480
# div_y_pos = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # div_y_pos += div_speed
    #
    # if div_y_pos >= div_hieght + div_gap:
    #     div_y_pos = 0
    #
    #
    # screen.blit(Grass,(0,0))
    #
    # y_road = 0
    #
    # for i in range(4):
    #     screen.blit(Road,(250,y_road))
    #     y_road+= 200


    pygame.display.flip()