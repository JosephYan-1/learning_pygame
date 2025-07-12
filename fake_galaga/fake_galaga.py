#while true
#game events (player activity)
# loops for gameworld stuff like npc/player/ai
#render for printing out graaphic
import pygame
from enemy_galaga import Enemy
from player_galaga import Player
from pellet import Pellet


def show_score(x, y, screen, score):
    font = pygame.font.Font(None, 20)
    dis_score = font.render(f"SCORE :{str(score)}", True, "white")
    screen.blit(dis_score, (x,y))

def gameover(screen):
    go_font = pygame.font.Font(None, 40)
    display_go = go_font.render("GAME OVER", True, "red")
    q_go = go_font.render("Q to Quit", True, "red")
    r_go = go_font.render("R to Restart", True, "red")
    screen.fill("black")
    screen.blit(display_go, (115,450))
    screen.blit(q_go, (115, 480))
    screen.blit(r_go, (115, 510))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if event.type == pygame.QUIT or keys[pygame.K_q]:
                pygame.quit()
                exit()
            elif keys[pygame.K_r]:
                waiting = False  # You can replace this with a quit or restart flag

def main():
    pygame.init()

    PELLET_COOLDOWN = 500
    ENEMY_COOLDOWN = 800

    score = 0
    clock = pygame.time.Clock()
    pygame.display.set_caption("FAKE GALAGA")
    screen = pygame.display.set_mode((400,900))            
    player = Player()
    dt = 0
    enemies = []
    pellets = []
    last_shot_time = 0
    last_enemy_time = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        screen.fill("black")
        show_score(0, 0, screen, score)
        enemies_to_remove = set()
        pellets_to_remove = set()

        for pellet in pellets:
            for enemy in enemies:
                if pellet.hit(enemy):
                    enemies_to_remove.add(enemy)
                    pellets_to_remove.add(pellet)
                    break

        for enemy in enemies_to_remove:
            score += enemy.y_location
            enemies.remove(enemy)
        
        for pellet in pellets_to_remove:
            pellets.remove(pellet)
                    
        # keys = pygame.key.get_pressed()
        # if keys[]

        keys = pygame.key.get_pressed()

        pellet_current_time = pygame.time.get_ticks() #get time for cooldown
        if keys[pygame.K_p] and pellet_current_time - last_shot_time > PELLET_COOLDOWN : #sub to makesure the cool down is met
            pellets.append(player.shoot())
            last_shot_time = pellet_current_time
            print("NEW PELLET")
        
        player.move(keys)

        enemy_current_time = pygame.time.get_ticks()
        if enemy_current_time - last_enemy_time > ENEMY_COOLDOWN:
            enemies.append(Enemy())
            last_enemy_time = enemy_current_time

        
        for enemy in enemies[:]:
            if enemy.y_location > 850: #greater than point we can shoot
                enemies.remove(enemy)
                gameover(screen)
                return main()
            enemy.move(enemy.speed)
            enemy.draw(screen)

        for pellet in pellets[:]:
            if pellet.y < 0:
                pellets.remove(pellet)
                continue
                
            pellet.draw(screen)
            pellet.move()

        player.draw(screen)

        dt = clock.tick(60) / 1000
        pygame.display.flip()

main()