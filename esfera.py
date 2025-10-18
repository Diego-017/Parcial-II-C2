from vpython import *

# Creacion del espacio (escena)
scene.title = "Movimiento de esfera con rastro"
scene.background = color.black

# Creacion de  la esfera en el origen con rastro
bola = sphere(pos=vector(0, 0, 0), radius=0.8, color=color.red, make_trail=True)

# Velocidad inicial
vel = vector(0.12, 0.08, 0)  # se mueve en X y Y
    
while True:
    rate(60)  # control de fotogramas por segundo
    bola.pos += vel
    # si alcanza cierto límite en X o Y, invierte la dirección
    if abs(bola.pos.x) > 5:
        vel.x = -vel.x
    if abs(bola.pos.y) > 3:
        vel.y = -vel.y
