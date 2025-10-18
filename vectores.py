from vpython import *

scene.title = "Esfera con vector de velocidad"
scene.background = color.black

# Creación de la  esfera
bola = sphere(pos=vector(0, 0, 0), radius=0.7, color=color.red, make_trail=True)

# Vector de velocidad como flecha
vel_vector = arrow(pos=bola.pos, axis=vector(2, 1.5, 0), color=color.green)

while True:
    rate(60)
    # suponemos movimiento proporcional al vector, la flecha parte de la esfera
    bola.pos += vel_vector.axis * 0.01
    vel_vector.pos = bola.pos  
