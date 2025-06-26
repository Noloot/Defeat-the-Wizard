import pygame

pygame.mixer.init()

try:
    sound = pygame.mixer.Sound("utils/sfx/slash.wav")
    sound.play()
    input("Press Enter to quit...")  # Keep app alive to hear the sound
except pygame.error as e:
    print(f"❌ Failed to load slash.wav: {e}")
