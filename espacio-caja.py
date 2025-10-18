from vpython import *

scene.title = "Creación de un escenario"
scene.background = color.gray(0.3)

# Dimensiones del contenedor
ancho = 10
alto = 6
prof = 8

# Creación de  paredes y piso tipo estilo cajas
piso = box(pos=vector(0, -alto/2, 0), size=vector(ancho, 0.2, prof), color=color.green)
pared_izq = box(pos=vector(-ancho/2, 0, 0), size=vector(0.2, alto, prof), color=color.blue, opacity=0.4)
pared_der = box(pos=vector(ancho/2, 0, 0), size=vector(0.2, alto, prof), color=color.blue, opacity=0.4)
pared_fondo = box(pos=vector(0, 0, -prof/2), size=vector(ancho, alto, 0.2), color=color.blue, opacity=0.4)
pared_frente = box(pos=vector(0, 0, prof/2), size=vector(ancho, alto, 0.2), color=color.blue, opacity=0.2)
bola = sphere(pos=vector(0, 0, 0), radius=0.6, color=color.white,)

# Velocidad inicial vectorial
vel = vector(0.11, 0.09, 0.07)

# Cálculo de los límites internos para rebote
lim_x = (ancho/2) - bola.radius
lim_y = (alto/2) - bola.radius
lim_z = (prof/2) - bola.radius

while True:
    rate(100)
    bola.pos += vel

    # Rebote en el eje X
    if bola.pos.x > lim_x or bola.pos.x < -lim_x:
        vel.x = -vel.x
    # Rebote en Y  incluye el techo / piso
    if bola.pos.y > lim_y or bola.pos.y < -lim_y:
        vel.y = -vel.y
    # Rebote en el eje Z  para los fondos
    if bola.pos.z > lim_z or bola.pos.z < -lim_z:
        vel.z = -vel.z
