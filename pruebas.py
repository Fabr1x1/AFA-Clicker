#Importamos los módulos con los que trabajaremos
import pygame
import sys
from pygame.locals import *

# Definimos AFA por segundo
CPS = 0.0
# Definimos el AFA inicial
AFA = 0
# Definimos la velocidad del juego
FPS = 20
Background_pos = (0, 0)
# Establecemos cambiar como falso

# Creamos la clase item
class Item:
    def __init__(self, rect, text, precio_base, cps_base_each):
        self.rect = rect
        self.text = text
        self.count = 0
        self.precio_base = precio_base
        self.cps_each = cps_base_each

    # Dibujamos los botones que vamos a utilizar
    def draw(self, surface):
        # Dibujar Fondo
        pygame.draw.rect(surface, BUTTON_BG_COLOR, self.rect, 0)
        # Dibujar Borde
        pygame.draw.rect(surface, BUTTON_BG_COLOR, self.rect, 2)
        # Dibujar Texto
        text_surface = font.render(str(self.count) + "x" + self.text + " $" + str(int(self.precio())), False, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface, text_rect)

    # Creamos la funcion Total_cps
    def total_cps(self):
        return self.cps_each * self.count

    # Creamos la funcion precio
    def precio(self):
        return self.precio_base * 1.15 ** self.count

    # Creamos la funcion click
    def click(self):
        precio = self.precio()
        global AFA
        if AFA >= precio:
            self.count += 1
            AFA -= precio

    def collidepoint(self, point):
        return self.rect.collidepoint(point)


class Personaje(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imagenes = []  # Lista para almacenar las imágenes del personaje
        self.indice_imagen_actual = 0  # Índice de la imagen actual a mostrar
        self.cargar_imagenes()  # Método para cargar las imágenes del personaje
        self.imagen_actual = self.imagenes[self.indice_imagen_actual]
        self.rect = self.imagen_actual.get_rect()
        self.rect.topleft = (x, y)

    def cargar_imagenes(self):
        # Cargar las imágenes del personaje y añadirlas a la lista de imágenes
        imagen_1 = pygame.image.load("imagenes/nicoRobin/nicoRobinCensurada.png")
        imagen_2 = pygame.image.load("imagenes/nicoRobin/nicoRobinMediaCensurada.png")
        imagen_3 = pygame.image.load("imagenes/nicoRobin/nicoRobinSinCensura.png")

        self.imagenes.append(imagen_1)
        self.imagenes.append(imagen_2)
        self.imagenes.append(imagen_3)

    def cambiar_imagen(self):
        self.indice_imagen_actual += 1

        # Volver al inicio si se supera el índice máximo
        if self.indice_imagen_actual >= len(self.imagenes):
            self.indice_imagen_actual = 0

        self.imagen_actual = self.imagenes[self.indice_imagen_actual]

    def dibujar(self):
        screen.blit(self.imagen_actual, self.rect)


# Crear un objeto de la clase Personaje
personaje = Personaje(3, 5)
personaje_rect = Rect(3, 5, 300, 500)

# Definimos los colores de los botones
BUTTON_BG_COLOR = pygame.Color(68, 93, 255)
BUTTON_BORDER_COLOR = pygame.Color(85, 50, 232)

# Creamos una lista de objetos
def make_items(text_list, base_price_list, cps_list, rect, spacing):
    button_height = rect.height / len(text_list)
    button_width = rect.width
    buttons = []
    for i in range(len(text_list)):
        text = text_list[i]
        base_price = base_price_list[i]
        base_cps = cps_list[i]
        button_rect = Rect(rect.left, rect.top + i * (button_height + spacing), button_width, button_height)
        button = Item(button_rect, text, base_price, base_cps)
        buttons.append(button)
    return buttons


def click_personaje():
    global AFA
    AFA = AFA + 1
    return AFA


# Nos permite calcular cuanto CPS ganamos
def calculate_cps():
    global CPS
    cps = 0.0
    for item in items:
        cps += item.total_cps()
    CPS = (cps / FPS)


# Inicializar Pygame
pygame.init()
pygame.mixer.init()

fpsClock = pygame.time.Clock()

# Configuración de la pantalla
screen_width = 801
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("AFA Clicker")
FONT = pygame.font.SysFont("sysfont", 24)

# Colores
PINK = (186, 46, 172)
BLACK = (0, 0, 0)

# Fuente y tamaño del texto
font = pygame.font.Font(None, 36)

# Posición del texto en la pantalla
text_x = 500
text_y = 10

# Dentro de la clase Item creamos stats
items = make_items([" Caramelo", " Alfajor", " Chocolate", " Flores", " Anillo", " Ropa"],
                   [15, 100, 500, 3000, 10000, 40000],
                   [0.1, 2, 5, 10, 17, 22],
                   Rect(530, 20, 300, 530), 6)

# cargamos el fondo y una imagen (se crea objetos "Surface")
background_image = pygame.image.load("imagenes/fondo_beta.png").convert()

# Cargamos la música
pygame.mixer.music.load("sonidos/tema_principal.mp3")
pygame.mixer.music.play(loops=-1)

# Indicamos la posición de las "Surface" sobre la ventana
screen.blit(background_image, (Background_pos))

# Se muestran los cambios en pantalla
pygame.display.flip()

def update_afa():
    global AFA
    AFA += CPS
    return AFA

def cambiar_skin():
    return personaje.cambiar_imagen()

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
button_text = "Quitar Censura x 200000"


# Bucle principal del juego
while True:
    screen.blit(background_image, (Background_pos))

    
    # Dibujar el botón en la pantalla
    pygame.draw.rect(screen, BUTTON_BG_COLOR, button_rect, 0)
    pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button_rect, 2)

    # Renderizar el texto del botón
    text_surface = font.render(button_text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=button_rect.center)

    # Dibujar el texto en la pantalla
    screen.blit(text_surface, text_rect)


    for button in items:
        button.draw(screen)
    # Dibuja contador de afa
    text_surface = FONT.render(str(int(AFA)) + "+" + str(CPS) + "APS", False, PINK)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (400, 15)
    screen.blit(text_surface, text_rect)
    calculate_cps()
    update_afa()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_button = event.button
            if mouse_button == 1:
                for button in items:
                    if button.collidepoint(mouse_pos):
                        button.click()
                        break
                if personaje_rect.collidepoint(mouse_pos):
                    click_personaje()
                if button_rect.collidepoint(mouse_pos) and AFA >= 200000:
                    cambiar_skin()
                    AFA -= 200000
    # Actualizar la pantalla
    personaje.dibujar()
    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(FPS)
