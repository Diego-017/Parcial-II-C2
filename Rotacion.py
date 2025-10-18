from vpython import *

scene.title = "Rotación de un cubo"
scene.background = color.purple

# Creacion de  un cubo central
cubo = box(pos=vector(0,0,0), size=vector(2, 1, 1), color=color.white)

while True:
    rate(40)
    # se rota alrededor del eje Z un poco cada iteración
    cubo.rotate(angle=0.02, axis=vector(0, 0, 1))
