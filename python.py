import pygame
import sys
import subprocess

# Configuración de la ventana
ANCHO = 800
ALTO = 600

# Inicialización de Pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("AFA Clicker Inicio")
reloj = pygame.time.Clock()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Función para iniciar el archivo .py utilizando Pygame
def iniciar_juego():
    subprocess.Popen(["python", "pruebas.py"])
    pygame.quit()
    sys.exit()

# Cargar la imagen de fondo
background_image = pygame.image.load("imagenes/MenuInicio/EscenarioInicio.jpg").convert()

# Función para mostrar la narrativa en la ventana
def mostrar_narrativa():
    # Crear una superficie del tamaño de la ventana
    superficie = pygame.Surface((ANCHO, ALTO))

    # Dibujar la imagen de fondo en la superficie
    superficie.blit(background_image, (0, 0))

    # Texto de la narrativa
    texto_narrativa = "Bienvenido a AFA Clicker ¿Listo para comenzar tu aventura?"

    # Configuración de la fuente
    fuente = pygame.font.Font(None, 24)

    # Renderizar el texto de la narrativa
    texto_renderizado = fuente.render(texto_narrativa, True, BLANCO)
    rectangulo_texto = texto_renderizado.get_rect()
    rectangulo_texto.center = (ANCHO // 2, ALTO // 2)

    # Mostrar la superficie en la ventana
    ventana.blit(superficie, (0, 0))

    # Mostrar el texto de la narrativa en la ventana
    ventana.blit(texto_renderizado, rectangulo_texto)

    # Crear el botón para iniciar el juego
    rectangulo_boton = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 100, 200, 50)
    pygame.draw.rect(ventana, NEGRO, rectangulo_boton)
    texto_boton = fuente.render("Iniciar Juego", True, BLANCO)
    rectangulo_texto_boton = texto_boton.get_rect()
    rectangulo_texto_boton.center = rectangulo_boton.center
    ventana.blit(texto_boton, rectangulo_texto_boton)

    # Actualizar la ventana
    pygame.display.flip()

    # Cargar y reproducir la música en bucle
    pygame.mixer.music.load("sonidos/SaxofonSexy.mp3")  # Reemplaza "nombre_de_archivo.mp3" con el nombre de tu archivo de música
    pygame.mixer.music.play(-1)  # -1 indica que se reproducirá en bucle

    # Esperar a que se presione el botón para iniciar el juego
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if rectangulo_boton.collidepoint(evento.pos):
                    iniciar_juego()

        reloj.tick(60)

# Mostrar la narrativa en la ventana
mostrar_narrativa()
