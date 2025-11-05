# LM  Pygame Notes

import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 720)) # tuple
pygame.display.set_caption("Pygame Tutorial")

pos_x = 100
pos_y = 200

ufo = pygame.image.load("notes/py_notes/pygame_notes/ufo.png")
ufo_rect = ufo.get_rect(topleft = (512, 512))


while True: # or could be *While running:* or *While game:*, this is basic so just True.
    screen.fill((200,200,200))

    pygame.draw.rect(screen, (250,0,0), (pos_x, pos_y, 100, 100))
    pygame.draw.circle(screen, (0,0,0), (500,500), 50)

    screen.blit(ufo, ufo_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pos_x -= 5
        elif keys[pygame.K_RIGHT]:
            pos_x += 5
        elif keys[pygame.K_UP]:
            pos_y -= 5
        elif keys[pygame.K_DOWN]:
            pos_y += 5

    
    pygame.display.flip()




#   Note Questions:
# How do you set up pygame?
    # pip install pygame-ce
    # import pygame
    # pygame.init()
    # And everthing else shown above (make the screen, etc.)

# What is the purpose of the "While running" loop?
    # To keep the game going and the screen still running, unless the X button is clicked

# How do you create a screen in pygame?
    # screen = pygame.display.set_mode((width, height))

# How are objects placed on the screen in pygame?
    # pygame.draw.rect(screen, (250,0,0), (x, y, rect_w, rect_h))

# What events can I listen for in pygame? What do those events do?
    # QUIT, K_LEFT, other keys, etc.
    # They listen for if a button or key is clicked.

# How can I detect collision with pygame?
    # Example: self.rect.collidepoint(pos)

# How do you add sounds in pygame?
    # You can import music from files or import mixer from pygame

    # One Example:
        # mixer.music.load('resources/background.wav')
        # mixer.music.play(-1)

    # Another Example:
        # mixer.Sound('resources/explosion.wav').play()


# Extra:
    # Origin (0,0) is top left, y axis goes down (positive still), x axis goes right