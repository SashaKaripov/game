import pygame
import sys
from funcs import *
from Enemy1 import Enemy
# Заимствований кода из учебников или других проектов не было


pygame.display.set_caption("the Game")
pygame.init()


walk_a_w, walk_a_s, walk_d_s, walk_d_w, walk_a, walk_d, walk_s, walk_w, = [], [], [], [], [], [], [], []   # Переменные
fight_w, fight_s, fight_a, fight_d, fight_a_w, fight_a_s, fight_d_s, fight_d_w = [], [], [], [], [], [], [], []
healthbar = []
health_arr = []
fire = []
clock = pygame.time.Clock()
spawn_time = pygame.time.get_ticks()
bg = pygame.image.load("gamedamn/_floor/_flooor.png")
dark = pygame.image.load("gamedamn/_floor/_123.png")
screen = pygame.display.set_mode((800, 600))
walk_off = pygame.image.load("gamedamn/_stay/слой-1.png")
window_width = 800
window_height = 600
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)   # pygame.display.set_caption("Game Menu")
font = pygame.font.SysFont('sitkatext', 32)
player_anime_count = 0
fire_anime_count = 0
dark_count = 0
fight_anime_count = 0
fight_anime_1 = 0
repeat_walk_anim = 0
repeat_fight_anim = 0
repeat_fire_anim = 0
wave = 1
with open("gamedamn/_best.txt") as f:
    best_score = int(f.readline())
player_speed = 5
player_x = 380
player_y = 280


background_image = pygame.image.load("gamedamn/menubg/menu3.png")   # Создание меню
play_button_image = pygame.image.load("gamedamn/menubuttons/play_250x62.png")
quit_button_image = pygame.image.load("gamedamn/menubuttons/quit_250x62.png")
play_button_pos = (window_width//2 - play_button_image.get_width()//2, 300)
quit_button_pos = (window_width//2 - quit_button_image.get_width()//2, 400)


enemy1 = Enemy(-100, 300, 1)   # Made the enemy
enemy2 = Enemy(800, 300, 1)
enemy3 = Enemy(400, -100, 1)
enemy4 = Enemy(400, 700, 1)
enemy5 = Enemy(-100, 300, 1)
enemy6 = Enemy(800, 300, 1)
enemy7 = Enemy(400, -100, 1)
enemy8 = Enemy(400, 700, 1)
enemy9 = Enemy(-100, 300, 1)
enemy10 = Enemy(800, 300, 1)
enemy11 = Enemy(400, -100, 1)
enemy12 = Enemy(400, 700, 1)
enemy13 = Enemy(-100, 300, 1)
enemy14 = Enemy(800, 300, 1)
enemy15 = Enemy(400, -100, 1)
enemy16 = Enemy(400, 700, 1)
enemies1 = [enemy1, enemy2]
enemies2 = [enemy1, enemy2, enemy3, enemy4]
enemies3 = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]
enemies4 = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11, enemy12, enemy13,
            enemy14, enemy15, enemy16]


for i in '12345678':  # Массивы с покадровой анимацией
    walk_a_w.append(pygame.image.load("gamedamn/_aw/слой-" + i + '.png'))
    walk_a_s.append(pygame.image.load("gamedamn/_as/слой-" + i + '.png'))
    walk_d_s.append(pygame.image.load("gamedamn/ds/слой-" + i + '.png'))
    walk_d_w.append(pygame.image.load("gamedamn/dw/слой-" + i + '.png'))
    walk_a.append(pygame.image.load("gamedamn/_a/слой-" + i + '.png'))
    walk_w.append(pygame.image.load("gamedamn/w/слой-" + i + '.png'))
    walk_d.append(pygame.image.load("gamedamn/d/слой-" + i + '.png'))
    walk_s.append(pygame.image.load("gamedamn/s/слой-" + i + '.png'))
    fight_w.append(pygame.image.load("gamedamn/_fight/w/_" + i + ".png"))
    fight_a.append(pygame.image.load("gamedamn/_fight/_a/_" + i + ".png"))
    fight_s.append(pygame.image.load("gamedamn/_fight/s/_" + i + ".png"))
    fight_d.append(pygame.image.load("gamedamn/_fight/d/_" + i + ".png"))
    if i != '8' and i != '7' and i != '6':
        healthbar.append(pygame.image.load("gamedamn/healthbar/_" + i + '.png'))
    for enemy in enemies4:
        enemy.image_l.append(pygame.image.load("gamedamn/enemy/_a/слой-" + i + '.png'))
        enemy.image_r.append(pygame.image.load("gamedamn/enemy/d/слой-" + i + '.png'))
        enemy.image_u.append(pygame.image.load("gamedamn/enemy/w/_" + i + '.png'))
        enemy.image_d.append(pygame.image.load("gamedamn/enemy/s/_" + i + '.png'))
        if i != '8' and i != '7' and i != '6':
            enemy.image_die.append(pygame.image.load("gamedamn/enemy/dyin/_" + i + '.png'))
        if i != '8' and i != '7':
            enemy.enemy_fight_l.append(pygame.image.load("gamedamn/enemy/_fight_l/_" + i + '.png'))
            enemy.enemy_fight_r.append(pygame.image.load("gamedamn/enemy/_fight_r/_" + i + '.png'))
for i in range(16):
    fire.append(pygame.image.load("gamedamn/_fire/слой-" + str(i + 1) + '.png'))


# Game loop
start = 0
running = True
while running:
    pygame.display.update()

    for event in pygame.event.get():   # Event handling
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start == 0:
                if (quit_button_pos[0] <= mouse_pos[0] <= quit_button_pos[0] + quit_button_image.get_width() and
                        quit_button_pos[1] <= mouse_pos[1] <= quit_button_pos[1] + quit_button_image.get_height()):
                    # Quit the game
                    running = False
                    pygame.quit()
                    sys.exit()
                if (play_button_pos[0] <= mouse_pos[0] <= play_button_pos[0] + play_button_image.get_width() and
                        play_button_pos[1] <= mouse_pos[1] <= play_button_pos[1] + play_button_image.get_height()):
                    start = 1

    if start == 0:
        window.fill((0, 0, 0))
        window.blit(background_image, (0, 0))
        window.blit(play_button_image, play_button_pos)
        window.blit(quit_button_image, quit_button_pos)

    if start == 1:
        screen.blit(bg, (0, 0))  # Stratin settings
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
            # Счётчики задержки кадров анимации
            repeat_walk_anim += 1
            repeat_fight_anim += 1
        repeat_fire_anim += 1

        if wave == 1:  # Анимация передвижения врага
            for enemy in enemies1:
                enemy.movement_plus_anim_enemys(player_x, player_y, screen)
                health_arr.append(enemy.health_anim_count)
            health_anim_count = sum(health_arr)
            health_arr = []
        if wave == 2:
            for enemy in enemies2:
                enemy.movement_plus_anim_enemys(player_x, player_y, screen)
                health_arr.append(enemy.health_anim_count)
            health_anim_count = sum(health_arr)
            health_arr = []
        if wave == 3:
            for enemy in enemies3:
                enemy.movement_plus_anim_enemys(player_x, player_y, screen)
                health_arr.append(enemy.health_anim_count)
            health_anim_count = sum(health_arr)
            health_arr = []
        if wave == 4:
            for enemy in enemies4:
                enemy.movement_plus_anim_enemys(player_x, player_y, screen)
                health_arr.append(enemy.health_anim_count)
            health_anim_count = sum(health_arr)
            health_arr = []

        screen.blit(healthbar[health_anim_count], (player_x - 21, player_y - 30))  # Анимация здоровья персонажа

        for i in [(-70, 230), (350, -100), (780, 230), (355, 560)]:  # Анимация огня
            screen.blit(fire[fire_anime_count], i)

        if keys[pygame.K_w] and keys[pygame.K_e]:  # Анимация ударов
            if fight_anime_1 < 15:
                screen.blit(fight_w[0], (player_x, player_y))
            else:
                screen.blit(fight_w[fight_anime_count], (player_x, player_y))
        elif keys[pygame.K_a] and keys[pygame.K_e]:
            if fight_anime_1 < 15:
                screen.blit(fight_a[0], (player_x, player_y))
            else:
                screen.blit(fight_a[fight_anime_count], (player_x, player_y))
        elif keys[pygame.K_s] and keys[pygame.K_e]:
            if fight_anime_1 < 15:
                screen.blit(fight_s[0], (player_x, player_y))
            else:
                screen.blit(fight_s[fight_anime_count], (player_x, player_y))
        elif keys[pygame.K_d] and keys[pygame.K_e]:
            if fight_anime_1 < 15:
                screen.blit(fight_d[0], (player_x, player_y))
            else:
                screen.blit(fight_d[fight_anime_count], (player_x, player_y))

        elif keys[pygame.K_a]:  # Анимация передвижения
            screen.blit(walk_a[player_anime_count], (player_x, player_y))
        elif keys[pygame.K_d]:
            screen.blit(walk_d[player_anime_count], (player_x, player_y))
        elif keys[pygame.K_w]:
            screen.blit(walk_w[player_anime_count], (player_x, player_y))
        elif keys[pygame.K_s]:
            screen.blit(walk_s[player_anime_count], (player_x, player_y))
        elif keys[pygame.K_w] and keys[pygame.K_a]:
            screen.blit(walk_a_w[player_anime_count], (player_x, player_y))
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            screen.blit(walk_d_w[player_anime_count], (player_x, player_y))
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            screen.blit(walk_a_s[player_anime_count], (player_x, player_y))
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            screen.blit(walk_d_s[player_anime_count], (player_x, player_y))
        else:
            screen.blit(walk_off, (player_x, player_y))

        movement_body_box(enemies4)  # Столкновения врагов

        if wave_enemy_alive(enemies1) == 0 and wave == 1:  # Счётчик волн
            wave = 2
        if wave_enemy_alive(enemies2) == 0 and wave == 2:
            wave = 3
        if wave_enemy_alive(enemies3) == 0 and wave == 3:
            wave = 4
        if (wave_enemy_alive(enemies4) == 0 and wave == 4 and
                ((enemies4[8].repeat_anim_die == 4 and enemies4[8].anim_die_count == 3) or
                 (enemies4[9].repeat_anim_die == 4 and enemies4[9].anim_die_count == 3) or
                 (enemies4[10].repeat_anim_die == 4 and enemies4[10].anim_die_count == 3) or
                 (enemies4[11].repeat_anim_die == 4 and enemies4[11].anim_die_count == 3) or
                 (enemies4[12].repeat_anim_die == 4 and enemies4[12].anim_die_count == 3) or
                 (enemies4[13].repeat_anim_die == 4 and enemies4[13].anim_die_count == 3) or
                 (enemies4[14].repeat_anim_die == 4 and enemies4[14].anim_die_count == 3) or
                 (enemies4[15].repeat_anim_die == 4 and enemies4[15].anim_die_count == 3))):
            wave = 6

        if not (keys[pygame.K_e]):  # Передвижение
            fight_anime_count = 0
            fight_anime_1 = 0
            if wave != 5:
                if (keys[pygame.K_a] and keys[pygame.K_w] and player_x > 40 and player_y > 40 and
                        'w' not in allow_move(player_x, player_y, enemies4) and
                        'a' not in allow_move(player_x, player_y, enemies4)):
                    player_x -= player_speed / 2**0.5
                    player_y -= player_speed / 2**0.5
                elif (keys[pygame.K_d] and keys[pygame.K_w] and player_x < 710 and player_y > 40 and
                      'w' not in allow_move(player_x, player_y, enemies4) and
                      'd' not in allow_move(player_x, player_y, enemies4)):
                    player_x += player_speed / 2**0.5
                    player_y -= player_speed / 2**0.5
                elif (keys[pygame.K_a] and keys[pygame.K_s] and player_y < 510 and player_x > 40 and
                      'a' not in allow_move(player_x, player_y, enemies4) and
                      's' not in allow_move(player_x, player_y, enemies4)):
                    player_x -= player_speed / 2**0.5
                    player_y += player_speed / 2**0.5
                elif (keys[pygame.K_d] and keys[pygame.K_s] and player_y < 510 and player_x < 710 and
                      'd' not in allow_move(player_x, player_y, enemies4) and
                      's' not in allow_move(player_x, player_y, enemies4)):
                    player_x += player_speed / 2**0.5
                    player_y += player_speed / 2**0.5
                elif keys[pygame.K_a] and player_x > 40 and 'a' not in allow_move(player_x, player_y, enemies4):
                    player_x -= player_speed
                elif keys[pygame.K_d] and player_x < 710 and 'd' not in allow_move(player_x, player_y, enemies4):
                    player_x += player_speed
                elif keys[pygame.K_w] and player_y > 40 and 'w' not in allow_move(player_x, player_y, enemies4):
                    player_y -= player_speed
                elif keys[pygame.K_s] and player_y < 510 and 's' not in allow_move(player_x, player_y, enemies4):
                    player_y += player_speed
        else:
            fight_anime_1 += 1

        for enemy in enemies4:  # Сражение с врагами
            if fight_anime_count == 5 and repeat_fight_anim == 2:
                if (keys[pygame.K_w] and keys[pygame.K_e] and 0 <= player_y - enemy.enemy_pos_y <= 60 and
                        abs(player_x - enemy.enemy_pos_x) <= 50):
                    enemy.hp -= 0.5
                elif (keys[pygame.K_a] and keys[pygame.K_e] and abs(player_y - enemy.enemy_pos_y) <= 50 and
                      0 <= player_x - enemy.enemy_pos_x <= 50):
                    enemy.hp -= 0.5
                elif (keys[pygame.K_s] and keys[pygame.K_e] and 0 <= enemy.enemy_pos_y - player_y <= 60 and
                      abs(player_x - enemy.enemy_pos_x) <= 50):
                    enemy.hp -= 0.5
                elif (keys[pygame.K_d] and keys[pygame.K_e] and abs(player_y - enemy.enemy_pos_y) <= 50 and
                      0 <= enemy.enemy_pos_x - player_x <= 50):
                    enemy.hp -= 0.5
                if enemy.hp == 0:
                    enemy.alive = 0

        if wave == 6 and dark_count < 40:
            screen.blit(dark, (0, 0))
            if dark_count == 39:
                wave = 5
                with open('gamedamn/_best.txt', 'w') as f:
                    f.write("4")
            dark_count += 1

        if repeat_walk_anim == 4:  # Измения счётчиков задержки кадров анимации
            player_anime_count += (player_anime_count != 7) - player_anime_count*(player_anime_count == 7)
            repeat_walk_anim = 0
        if repeat_fight_anim == 6:
            fight_anime_count += (fight_anime_count != 7) - fight_anime_count*(fight_anime_count == 7)
            repeat_fight_anim = 0
        if repeat_fire_anim == 4:
            fire_anime_count += (fire_anime_count != 15) - fire_anime_count*(fire_anime_count == 15)
            repeat_fire_anim = 0
        if wave <= 4:
            screen.blit(font.render("Score " + str(wave-1), 1, (255, 0, 0)), (600, 50))
            screen.blit(font.render("Best " + str(best_score), 1, (255, 0, 0)), (600, 100))
        else:
            screen.blit(font.render("Passed", 1, (255, 0, 0)), (340, 280))

        if health_anim_count == 4:
            start = 2
            if best_score < (wave-1):
                with open('gamedamn/_best.txt', 'w') as f:
                    f.write(str(wave-1))
                with open('gamedamn/_best.txt') as f:
                    best_score = int(f.readline())

        clock.tick(60)

    if start == 2:
        k = 1
        for enemy in enemies4:
            enemy.alive = 1
            enemy.hp = 1
            if k % 4 == 1:
                enemy.enemy_pos_x, enemy.enemy_pos_y = -100, 300
            if k % 4 == 2:
                enemy.enemy_pos_x, enemy.enemy_pos_y = 800, 300
            if k % 4 == 3:
                enemy.enemy_pos_x, enemy.enemy_pos_y = 400, -100
            if k % 4 == 0:
                enemy.enemy_pos_x, enemy.enemy_pos_y = 400, 700
            k += 1
            enemy.health_anim_count = 0
            enemy.enemy_anim_count = 0
            enemy.enemy_fight_anim_count = 0
            enemy.anim_die_count = 0
        fight_anime_count = 0
        health_anim_count = 0
        player_x, player_y = 380, 280
        wave = 1
        start = 1
