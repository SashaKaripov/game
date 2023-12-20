def wave_enemy_alive(enemies: list, sum=0) -> int:  # счётчик выживших врагов
    """Returns sum of the living enemies

        :param enemies: enemies
        :type enemies: list
        :param sum: sum of the living enemies
        :type sum: int
        :returns: sum of the living enemies
        :rtype: int"""
    
    for enemy in enemies:
        sum += enemy.alive
    return sum


def movement_body_box(enemies: list):  # Столкновение врагов
    """Changes enemy's coordinate if enemies collide

        :param enemies: enemies
        :type enemies: list
        :changes: enemy's coordinate
        :ctype: float"""

    for i in range(len(enemies) - 1):
        for j in range(i + 1, len(enemies)):
            if (abs(enemies[j].enemy_pos_x - enemies[i].enemy_pos_x) <= 25 and
                    abs(enemies[j].enemy_pos_y - enemies[i].enemy_pos_y) <= 50):
                enemies[i].enemy_pos_y += 1
                enemies[i].enemy_pos_x += 1
                enemies[j].enemy_pos_y -= 1
                enemies[j].enemy_pos_x -= 1


def allow_move(player_x: float, player_y: float, enemies: list, cases_='') -> str:  # Врезается ли игрок во врага
    """Returns the cases when the button's disabled

        :param player_x: x-coordinate 
        :type player_x: float
        :param player_y: y-coordinate
        :type player_y: float
        :param enemies: enemies
        :type enemies: list
        :param cases_: limitation of movement
        :type cases_: str
        :returns: cases of button's disabled 
        :rtype: str"""

    for enemy in enemies:
        if enemy.alive == 1:
            if (0 <= player_y - enemy.enemy_pos_y <= 40 and
                    abs(enemy.enemy_pos_x - player_x) <= 20 and 'w' not in cases_):
                cases_ += 'w'
            if (abs(player_y - enemy.enemy_pos_y) <= 20 and
                    0 <= player_x - enemy.enemy_pos_x <= 40 and 'a' not in cases_):
                cases_ += 'a'
            if (0 <= enemy.enemy_pos_y - player_y <= 40 and
                    abs(enemy.enemy_pos_x - player_x) <= 20 and 's' not in cases_):
                cases_ += 's'
            if (abs(player_y - enemy.enemy_pos_y) <= 20 and
                    0 <= enemy.enemy_pos_x - player_x <= 40 and 'd' not in cases_):
                cases_ += 'd'
    return cases_
