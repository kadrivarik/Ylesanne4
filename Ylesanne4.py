import pygame #impordin pygame mooduli
import random  # impordin random mooduli

# kutsun ellu mooduli pygame
pygame.init()

#ekraani suuruse määramine
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Automäng")  #panen ekraanile nime

#mängus kasuatatavad värvid
sinine = (0, 0, 255)  #punktiskoori värv

#laen mängus kasutatavad pildid
taustapilt = pygame.image.load("bg_rally.jpg")  # taustapilt
punase_auto_pilt = pygame.image.load("f1_red.png")  # punane auto
sinise_auto_pilt = pygame.image.load("f1_blue.png")  # sinine auto

#punase auto alguskoordinaadid
punane_x = WIDTH // 2
punane_y = HEIGHT - 100
speedX = 0
speedY = 0

#siniste autode alguskoordinaadid
sinised_autod = [] #tekib list autode koordinaatidest
for _ in range(3): #loon kolm autot
    sinised_autod.append([random.randint(0, WIDTH - 50), random.randint(-200, -50)])

# Mängija punktiskoor
punktid = 0  #algne seis
font = pygame.font.Font(None, 36)

# Mängutsükkel
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Liiguta taustapilti
    screen.blit(taustapilt, (0, 0))

    # Liiguta siniseid autosid
    for sinine_auto in sinised_autod:
        sinine_auto[1] += 3
        screen.blit(sinise_auto_pilt, sinine_auto)

        #määrame siniste autode koordinaadid
        if sinine_auto[1] > HEIGHT:
            sinine_auto[1] = random.randint(-200, -50)
            sinine_auto[0] = random.randint(145, 495)
            punktid += 1

    # Liiguta mängija autot  (https://moodle.edu.ee/mod/page/view.php?id=2193396)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speedX = 3
            elif event.key == pygame.K_LEFT:
                speedX = -3
            elif event.key == pygame.K_UP:
                speedY = -3
            elif event.key == pygame.K_DOWN:
                speedY = 3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                speedX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speedY = 0

    #liigutame punast autot
    punane_x += speedX
    punane_y += speedY
    screen.blit(punase_auto_pilt, (punane_x, punane_y))

    #kuvab punktid, määran värvitooni ja teksti suuruse
    punktide_tekst = font.render("Score: " + str(punktid), True, sinine)
    screen.blit(punktide_tekst, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
