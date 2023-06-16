

# Colores
BUTTON_BG_COLOR = pygame.Color(68, 93, 255)
BUTTON_BORDER_COLOR = pygame.Color(85, 50, 232)
BUTTON_TEXT_COLOR = pygame.Color(255, 255, 255)

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ejemplo de Botón")

# Fuente y tamaño del texto
font = pygame.font.Font(None, 24)

# Definir las dimensiones y posición del botón
button_width = 200
button_height = 50
button_x = (screen_width - button_width) // 2
button_y = (screen_height - button_height) // 2

# Crear el rectángulo del botón
button_rect = Rect(button_x, button_y, button_width, button_height)

# Texto del botón
button_text = "Cambiar Skin"


    # Dibujar el botón en la pantalla
    pygame.draw.rect(screen, BUTTON_BG_COLOR, button_rect, 0)
    pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button_rect, 2)

    # Renderizar el texto del botón
    text_surface = font.render(button_text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=button_rect.center)

    # Dibujar el texto en la pantalla
    screen.blit(text_surface, text_rect)

