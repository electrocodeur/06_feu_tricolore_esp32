import time
from machine import Pin

# Définir les broches pour chaque LED
led_rouge = Pin(23, Pin.OUT)
led_orange = Pin(22, Pin.OUT)
led_verte = Pin(21, Pin.OUT)

# Durées d'allumage pour chaque LED en secondes
durees = [3, 1, 3]  # Rouge, Orange, Vert

# Boucle infinie pour le feu tricolore
while True:
    for led, duree in zip([led_rouge, led_orange, led_verte], durees):
        led.on()
        time.sleep(duree)
        led.off()
