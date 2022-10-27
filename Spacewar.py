# SpaceWar
# by Austin # HACK:
# www.Cozzmobot.github.io




import time, random
WIDTH = 1000
HEIGHT = 1000
ship1_x = 600
ship1_y = 350
ship2_x = 350
ship2_y = 350
bullet1_x = 600
bullet2_x = 430
bullet1_y = 350
bullet2_y = 350
health_1 = 10000
health_2 = 10000
num_f1 = 0
num_f2 = 0



global dronex, droney
dronex = random.randint(1, 1000)
droney = random.randint(1, 1000)

def __init__():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (50, 50))
    screen.blit(images.spaceship1, (ship1_x, ship1_y))
    screen.blit(images.ship, (ship2_x, ship2_y))
    screen.blit(images.energy_ball2, (bullet1_x, bullet1_y))
    screen.blit(images.energy_ball, (bullet2_x, bullet2_y))
    screen.blit(images.positioning_system, (0, 0))
    screen.blit(images.drone, (dronex, droney))






def game_loop():
    __init__()
    global ship1_x, ship1_y, ship2_x, ship2_y, bullet1_x, bullet2_x, bullet1_y, bullet2_y, health_1, health_2, dronex, droney, ex, ey, num_f1, num_f2
    dronex = random.randint(1, 1000)
    droney = random.randint(1, 1000)


    if bullet2_x in range (ship1_x, ((ship1_x) + 100)) and bullet2_y in range (ship1_y, ((ship1_y) + 100)):
        health_1 -= 100
        sounds.fire.play()
        print("Ship 1 has",health_1,"health")
        if health_1 <=0:
            print("Ship 1 went off with a bang")
            sounds.e2.play()
            time.sleep(2)
            exit()



    if bullet1_x in range (ship2_x, ((ship2_x) + 120)) and bullet1_y in range (ship2_y, ((ship2_y) + 270)):
        health_2 -= 100
        sounds.fire.play()
        print("Ship 2 has",health_2,"health")
        if health_2 <=0:
            print("Ship 2 went off with a bang")
            sounds.e2.play()
            time.sleep(2)
            exit()


    else:

        pass



    if keyboard.right:
        ship1_x += 5
        bullet1_x +=5


    elif keyboard.left:
        ship1_x -= 5
        bullet1_x -=5


    elif keyboard.up:
        ship1_y -= 5
        bullet1_y -= 5


    elif keyboard.down:
        ship1_y += 5
        bullet1_y += 5


    elif keyboard.s:
        ship2_y += 5
        bullet2_y += 5


    elif keyboard.w:
        ship2_y -= 5
        bullet2_y -= 5


    elif keyboard.a:
        ship2_x -= 5
        bullet2_x -= 5



    elif keyboard.d:
        ship2_x += 5
        bullet2_x += 5

    elif keyboard.f:
        sounds.laser.play()
        bullet2_y -= 10
        health_2 += 50
        num_f1 +=10
        if bullet2_x in range (ship1_x, ((ship1_x) + 100)) and bullet2_y in range (ship1_y, ((ship1_y) + 100)):
            health_1 -= 100
            sounds.fire.play()
            print("Ship 1 has",health_1,"health")
            if health_1 <=0:
                print("Ship 1 has been hit with an energy ball. Ship 1 has died.")
                sounds.explosion.play()
                time.sleep(2)
                exit()
        print("Shields raised! gaining health")


    elif keyboard.j:
        sounds.laser.play()
        bullet1_y -= 10
        health_1 += 50
        num_f2 += 10
        if bullet1_x in range (ship2_x, ((ship2_x) + 120)) and bullet1_y in range (ship2_y, ((ship2_y) + 270)):
            health_2 -= 100
            sounds.fire.play()
            print("Ship 2 has",health_2,"health")
            if health_2 <=0:
                print("Ship 2 has been hit with an energy ball. Ship 2 has died.")
                sounds.e2.play()
                time.sleep(2)
                exit()
        print("Shields raised! gaining health")




    elif keyboard.v:
        bullet2_y += num_f1
        num_f1 -= num_f1


    elif keyboard.n:
        bullet1_y += num_f2
        num_f2 -= num_f2


    randomsum1 = random.randint(1, 100)
    randomsum2 = random.randint(1, 100)
    dronex += randomsum1
    droney += randomsum2

    if dronex == 1000 or droney == 1000:
        dronex -= 1000
        droney -= 1000


    else:
        pass


    if dronex in range (ship1_x, (ship1_x + 100)) and droney in range (ship1_y, (ship1_y + 100)):
        health_1 -= 30
        sounds.fire.play()
        print("Spaceship 1 lost health due to drone. It has", health_1 , " health")
        if health_1 <= 0:
            sounds.e2.play()
            time.sleep(2)
            quit()

    else:
        pass



    if dronex in range (ship2_x, (ship2_x + 120)) and droney in range (ship2_y, (ship2_y + 720)):
        health_2 -= 30
        sounds.fire.play()
        print("Spaceship 2 lost health due to drone. It has", health_2, " health")
        if health_2 <= 0:
            sounds.e2.play()
            time.sleep(2)
            quit()


    else:
        pass




#########################
##         end        ###
#########################






if __name__ == "__main__":
    game_loop()

clock.schedule_interval(game_loop, 0.03)
