from vpython import *
import random, math

# Creación de la escena
scene.title = "Cielo Estrellado"
scene.background = color.black
scene.width = 1000
scene.height = 600

# Creación de  estrellas aleatorias
estrellas = []
for i in range(200):
    x = random.uniform(-50, 50)
    y = random.uniform(-30, 30)
    z = random.uniform(-10, 10)
    estrella = sphere(pos=vector(x, y, z), radius=0.2, color=color.white)
    estrellas.append(estrella)

# Se crea una constelacion
puntos = [vector(-10, 5, 0), vector(-5, 8, 0), vector(0, 3, 0), vector(5, 6, 0), vector(10, 2, 0)]
constelacion = []  # Presentación de la lista de esferas.
for p in puntos:
    estrella_constelacion = sphere(pos=p, radius=0.2, color=color.cyan, emissive=True)
    constelacion.append(estrella_constelacion)

# Se crea la estrella fugaz 
estrella_fugaz = sphere(pos=vector(-50, 20, 0), radius=0.3, color=color.yellow, make_trail=False)

# Creación de luna
luna = sphere(pos=vector(30, 20, -20), radius=3, color=color.white, emissive=True, shininess=0.8, texture=textures.rock)
radio_x = 30
radio_z = 20
vel_rotacion = 0.10  #Velocidad de la luna

# Se presenta una animación
t = 0
while True:
    rate(60)
    t += 0.05

    # Parpadeo aleatorio de las  estrellas
    for e in estrellas:
        brillo = random.uniform(0.5, 1)
        e.color = vector(brillo, brillo, brillo)

    # Presentacion de movimiento de la estrella fugaz
    estrella_fugaz.pos.x += 1
    estrella_fugaz.pos.y -= 0.2
    if estrella_fugaz.pos.x > 50:
        estrella_fugaz.pos = vector(-50, random.uniform(10, 25), 0)

    # Onda suave en la constelación
    for i, e in enumerate(constelacion):
        e.pos.y = puntos[i].y + 0.2 * math.sin(t + i)

    # Rotación de la luna alrededor del cielo
    luna.pos.x = radio_x * math.cos(vel_rotacion * t)
    luna.pos.z = radio_z * math.sin(vel_rotacion * t)
    luna.pos.y = 20  # altura como constante
