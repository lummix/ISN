import pygame


GREEN = (40, 230, 120) #Définition de RGA

pygame.init()
screen = pygame.display.set_mode((500, 420))
center_x, center_y = 320, 240

clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS,Arial', 24) #Option --> police
texte = font.render('Veuillez miser : ', True, GREEN) #Texte --> (String, boolean, COULEUR)
texte_rect = texte.get_rect(center=(center_x, center_y)) #Position du trexte

input_value = "" #On définit un input vide
input = font.render(input_value, True, GREEN)
input_rect = input.get_rect(topleft=texte_rect.topright)

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                continuer = False
                break
            elif event.key == pygame.K_BACKSPACE: #Supression
                 input_value =  input_value[:-1]
            else:
                 input_value += event.unicode
            input = font.render(input_value, True, GREEN)
            input_rect = input.get_rect(topleft=texte_rect.topright)

    clock.tick(30) #Limiter la frame à 30 fps

    screen.fill(0)
    screen.blit(texte, texte_rect)
    screen.blit(input, input_rect)
    pygame.display.flip()

print("Affichage de la mise", int(input_value))

pygame.quit()