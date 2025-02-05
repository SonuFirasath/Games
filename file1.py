import pygame as pg
import random
pg.init()
screen = pg.display.set_mode((640, 480))
running = True
#player properties
player_width , player_height = 100, 50
player_speed = 0.4
player_x, player_y = 200, 300
player_rect = pg.Rect(0, 0, player_width, player_height)
#obstacle properties
obstacle_width, obstacle_height = 50, 50
obstacle_speed = 0.1
obstacle_rect = pg.FRect(random.randint(0, 400), 0 , obstacle_width, obstacle_height)

#score properties
score = 0
font = pg.font.Font(None, 36)
score_text = font.render(f"Score: {score}", True, (0, 0, 0))
score_text_rect = score_text.get_rect(center = (320, 50))
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((255, 255, 255))

    #rendering your player
    pg.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_width, player_height))
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player_x -= player_speed
    if keys[pg.K_RIGHT]:
        player_x += player_speed

    #moving obstacle downwards
    obstacle_rect.y += obstacle_speed

    #rendering your obstacle
    pg.draw.rect(screen,'black', obstacle_rect)
    if obstacle_rect.y > 480:
        obstacle_rect.y = 0
        obstacle_rect.x = random.randint(0, 400)
    #reseting obstacle position on collision with player
    if obstacle_rect.colliderect(pg.Rect(player_x, player_y, player_width, player_height)):
        score += 1
        obstacle_rect.y = 0
        obstacle_rect.x = random.randint(0, 400)
    #updating score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, score_text_rect)
    pg.display.flip()
pg.quit()
