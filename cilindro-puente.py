from vpython import *

scene.title = "Esfera rodando sobre rampa cilíndrica"
scene.background = color.white

# Creación del piso como caja para referencia visual
piso = box(pos=vector(0, -1, 0), size=vector(12, 0.2, 6), color=color.gray(0.6))

# Creación del cilindro inclinado como rampa
rampa = cylinder(pos=vector(-5, 0, 0), axis=vector(10, 4, 0), radius=0.4, color=color.blue)

# Creación de la esfera que rodará sobre la rampa
bola = sphere(pos=vector(-5, 0.4, 0), radius=0.5, color=color.red, make_trail=True)

# Velocidad inicial hacia abajo de la rampa
vel = vector(0.2, -0.05, 0)

while True:
    rate(80)
    bola.pos += vel
    # si toca la rampa (aproximado), procede a invertir dirección vertical
    # condición más simple: cuando bola.pos.y baja de cierto valor relativo
    if bola.pos.y < 0.4:
        vel.y = -vel.y
