from vpython import *
import math

# Creación de la escena

scene.title = "Sistema Solar"
scene.background = color.black
scene.width = 1000
scene.height = 600

# Variables de la camara

cam_angle_x = 0  
cam_angle_y = 0  
cam_distance = 50 

# Función para actualizar cámara según  sus ángulos
def actualizar_camara():
    scene.camera.pos = vector(
        cam_distance*math.sin(cam_angle_x)*math.cos(cam_angle_y),
        cam_distance*math.sin(cam_angle_y),
        cam_distance*math.cos(cam_angle_x)*math.cos(cam_angle_y)
    )
    scene.camera.axis = vector(0,0,0) - scene.camera.pos 

actualizar_camara()


sol = sphere(pos=vector(0,0,0), radius=3, texture="sol.jpg", emissive=True)

# Creación de los  planetas
planetas_info = [
    ["Mercurio", 0.3, 5, "mercurio.jpg", 0.04],
    ["Venus", 0.5, 7, "vennus.jpg", 0.03],
    ["Tierra", 0.5, 10, "tierra.jpg", 0.02],
    ["Marte", 0.4, 13, "marte.jpg", 0.015],
    ["Júpiter", 1.0, 18, "jupiter.jpg", 0.01],
    ["Saturno", 0.9, 22, "saturno.jpg", 0.008],
    ["Urano", 0.7, 26, "urano.jpg", 0.006],
    ["Neptuno", 0.7, 30, "neptuno.jpg", 0.005]
]

planetas = []
angulos = []
for info in planetas_info:
    p = sphere(pos=vector(info[2],0,0), radius=info[1], texture=info[3], trail_radius=0.05)
    planetas.append(p)
    angulos.append(0)

# Botones para mover cámara
def giro_izq(b):
    global cam_angle_x
    cam_angle_x -= 0.1
    actualizar_camara()

def giro_der(b):
    global cam_angle_x
    cam_angle_x += 0.1
    actualizar_camara()

def giro_arriba(b):
    global cam_angle_y
    cam_angle_y += 0.1
    if cam_angle_y > math.pi/2: cam_angle_y = math.pi/2
    actualizar_camara()

def giro_abajo(b):
    global cam_angle_y
    cam_angle_y -= 0.1
    if cam_angle_y < -math.pi/2: cam_angle_y = -math.pi/2
    actualizar_camara()

# Creación de los  botones
button(text="Izquierda", pos=scene.title_anchor, bind=giro_izq)
button(text="Derecha", pos=scene.title_anchor, bind=giro_der)
button(text="Arriba", pos=scene.title_anchor, bind=giro_arriba)
button(text="Abajo", pos=scene.title_anchor, bind=giro_abajo)


while True:
    rate(60)
    for i, p in enumerate(planetas):
        # Incrementación del  ángulo
        angulos[i] += planetas_info[i][4]
        # Actualiza la posición según órbita circular alrededor del Sol
        radio = planetas_info[i][2]
        p.pos.x = radio * math.cos(angulos[i])
        p.pos.z = radio * math.sin(angulos[i])
        p.pos.y = 0
