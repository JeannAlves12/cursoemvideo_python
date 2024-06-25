import pygame
import time

# Inicializar o pygame
pygame.init()

# Carregar o arquivo MP3
pygame.mixer.music.load('ex021.mp3')

# Reproduzir o arquivo MP3
pygame.mixer.music.play()

# Aguardar o término da reprodução
while pygame.mixer.music.get_busy():
    time.sleep(1)

# Finalizar o pygame
pygame.quit()