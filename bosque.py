from vpython import *
import random, math

# Creamos la escena 

scene.title = "Bosque"
scene.width = 1200
scene.height = 700
scene.background = vector(0.5, 0.8, 1)
scene.range = 80
scene.forward = vector(-1, -0.3, -1)
scene.autoscale = False

# Luz ambiental
distant_light(direction=vector(-1, -1, -1), color=color.white)
distant_light(direction=vector(1, 0, 0), color=color.yellow)

brown = vector(0.45, 0.25, 0.05)

# Terreno
terreno = box(pos=vector(0, -1, 0), size=vector(600, 1, 600), color=vector(0.2, 0.7, 0.2))

# Lago
lago = cylinder(pos=vector(50, -1, 50), axis=vector(0, 1, 0), radius=45,
                color=vector(0.3, 0.6, 0.9), opacity=0.6)

ondas = []
for i in range(12):
    o = ring(pos=vector(50, -0.3, 50), axis=vector(0,1,0),
             radius=5+i*2, thickness=0.1, color=vector(0.7,0.9,1), opacity=0.3)
    ondas.append(o)

# Montañas
for i in range(22):
    x = random.uniform(-280, 280)
    z = random.uniform(-300, -150)
    h = random.uniform(50, 100)
    pyramid(pos=vector(x, -1, z), size=vector(90, h, 90), color=vector(0.4, 0.4, 0.4))

# Árboles

arboles = []
for i in range(500):
    x = random.uniform(-250, 250)
    z = random.uniform(-250, 250)
    if (x - 50)**2 + (z - 50)**2 < 70**2:
        continue
    h = random.uniform(5, 14)
    trunk = cylinder(pos=vector(x, -1, z), axis=vector(0, h, 0), radius=0.5, color=brown)
    tipo = random.choice(["pino", "roble", "acacia"])
    if tipo == "pino":
        leaves = cone(pos=vector(x, h - 1, z), axis=vector(0, 5, 0), radius=3.5, color=vector(0, 0.5, 0))
    elif tipo == "roble":
        leaves = sphere(pos=vector(x, h + 1, z), radius=3.2, color=vector(0, 0.7, 0))
    else:
        leaves = ellipsoid(pos=vector(x, h + 1, z), length=3, height=4.5, width=2.5, color=vector(0, 0.6, 0))
    arboles.append((trunk, leaves))

# Se crean flores y rocas

for i in range(300):
    x = random.uniform(-200, 200)
    z = random.uniform(-200, 200)
    if (x - 50)**2 + (z - 50)**2 < 70**2:
        continue
    sphere(pos=vector(x, -0.8, z), radius=0.2,
           color=vector(random.random(), random.random(), random.random()))

for i in range(100):
    x = random.uniform(-220, 220)
    z = random.uniform(-220, 220)
    if (x - 50)**2 + (z - 50)**2 < 70**2:
        continue
    ellipsoid(pos=vector(x, -0.8, z),
              length=random.uniform(1, 4),
              height=random.uniform(0.5, 2),
              width=random.uniform(1, 3),
              color=vector(0.4, 0.4, 0.4))

# Se crea un campa
carpa = pyramid(pos=vector(-40, -1, 20), size=vector(10, 5, 12), color=vector(0.8, 0.3, 0.3))
fogata = [cylinder(pos=vector(-20+random.uniform(-1,1), -1, 10+random.uniform(-1,1)),
                   axis=vector(0,0.5,0), radius=0.3, color=brown) for _ in range(8)]
llamas = [sphere(pos=vector(-20, -0.5+random.uniform(0,1), 10),
                 radius=random.uniform(0.2, 0.5),
                 color=vector(1, random.uniform(0.4, 0.1), 0), opacity=0.8) for _ in range(15)]

# Fauna

pajaros = [sphere(pos=vector(random.uniform(-200,200), random.uniform(20,40), random.uniform(-200,200)), 
                radius=0.7, color=color.black) for _ in range(10)]
mariposas = [sphere(pos=vector(random.uniform(-150,150), random.uniform(2,10), random.uniform(-150,150)),
                      radius=0.3, color=vector(1, 0.5, random.random())) for _ in range(15)]
pescados = [ellipsoid(pos=vector(50+random.uniform(-30,30), -0.4, 50+random.uniform(-25,25)),
                  length=1.5, height=0.7, width=0.5, color=vector(1,0.5,0.2)) for _ in range(15)]
patos = []
for i in range(8):
    x = 50 + random.uniform(-30,30)
    z = 50 + random.uniform(-25,25)
    body = ellipsoid(pos=vector(x,-0.2,z), length=3, height=1.2, width=2, color=vector(1,1,0))
    head = sphere(pos=vector(x,0.5,z+0.3), radius=0.4, color=vector(1,1,0))
    beak = cone(pos=vector(x,0.5,z+0.8), axis=vector(0,0,0.3), radius=0.1, color=vector(1,0.5,0))
    patos.append((body, head, beak))


conejos = [ellipsoid(pos=vector(random.uniform(-100,100), -0.6, random.uniform(-100,100)),
                     length=1.5, height=1, width=1, color=vector(1,1,1)) for _ in range(6)]
zorros = [ellipsoid(pos=vector(random.uniform(-120,120), -0.5, random.uniform(-120,120)),
                   length=3, height=1.2, width=1.2, color=vector(1,0.3,0)) for _ in range(3)]
buho = [sphere(pos=vector(random.uniform(-150,150), random.uniform(10,20), random.uniform(-150,150)),
               radius=1, color=vector(0.7,0.7,0.5)) for _ in range(3)]
ciervo = [box(pos=vector(random.uniform(-80,-20),0,random.uniform(10,50)), 
            size=vector(2,2,4), color=vector(0.6,0.3,0.1)) for _ in range(3)]

luciernagas= [sphere(pos=vector(random.uniform(-120,120), random.uniform(2,15), random.uniform(-120,120)),
                    radius=0.15, color=vector(1,1,0.5), emissive=True, visible=False) for _ in range(25)]

# Se crea niebla

niebla = [sphere(pos=vector(random.uniform(-200,200), 1, random.uniform(-200,200)),
              radius=random.uniform(10, 20),
              color=vector(0.9,0.9,0.9), opacity=0.15) for _ in range(12)]

# MODOS AMBIENTALES

def modo_dia():
    scene.background = vector(0.5, 0.8, 1)
    for f in mariposas: f.visible = False
    for _, leaves in arboles: leaves.color = vector(0,0.7,0)
    for f in niebla: f.opacity = 0.1

def modo_tarde():
    scene.background = vector(1, 0.6, 0.3)
    for f in mariposas: f.visible = False
    for _, leaves in arboles: leaves.color = vector(0.4,0.5,0.1)
    for f in niebla: f.opacity = 0.2

def modo_noche():
    scene.background = vector(0.05,0.05,0.2)
    for f in mariposas: f.visible = True
    for _, leaves in arboles: leaves.color = vector(0,0.3,0)
    for f in niebla: f.opacity = 0.35

# CÁMARA INTERACTIVA

cam_angle_x = 0
cam_angle_y = 0
cam_distance = 130

def actualizar_camara():
    scene.camera.pos = vector(
        cam_distance * math.sin(cam_angle_x) * math.cos(cam_angle_y),
        cam_distance * math.sin(cam_angle_y),
        cam_distance * math.cos(cam_angle_x) * math.cos(cam_angle_y)
    )
    scene.camera.axis = vector(0,0,0) - scene.camera.pos

def giro_izq(b): 
    global cam_angle_x; cam_angle_x -= 0.1; actualizar_camara()
def giro_der(b): 
    global cam_angle_x; cam_angle_x += 0.1; actualizar_camara()
def giro_arriba(b): 
    global cam_angle_y; cam_angle_y += 0.1
    if cam_angle_y > math.pi/3: cam_angle_y = math.pi/3
    actualizar_camara()
def giro_abajo(b): 
    global cam_angle_y; cam_angle_y -= 0.1
    if cam_angle_y < -math.pi/3: cam_angle_y = -math.pi/3
    actualizar_camara()


# BOTONES

button(text=" Día", bind=lambda _: modo_dia())
button(text=" Atardecer", bind=lambda _: modo_tarde())
button(text=" Noche", bind=lambda _: modo_noche())
button(text="← ", pos=scene.title_anchor, bind=giro_izq)
button(text="→ ", pos=scene.title_anchor, bind=giro_der)
button(text="↑ ", pos=scene.title_anchor, bind=giro_arriba)
button(text="↓ ", pos=scene.title_anchor, bind=giro_abajo)

# ANIMACIÓN PRINCIPAL

angle = 0
actualizar_camara()

while True:
    rate(60)
    angle += 0.01

    for i, o in enumerate(ondas):
        o.radius = 5 + i*2 + math.sin(angle*2 + i*0.5)*0.8

    for body, head, beak in patos:
        body.pos.x += math.sin(angle*2 + random.uniform(0,1))*0.05
        body.pos.z += math.cos(angle*2 + random.uniform(0,1))*0.05
        head.pos = body.pos + vector(0,0.5,0.3)
        beak.pos = body.pos + vector(0,0.5,0.8)

    for f in pescados:
        f.pos.x += math.sin(angle*3 + random.uniform(0,1))*0.08
        f.pos.z += math.cos(angle*3 + random.uniform(0,1))*0.08

    for b in pajaros:
        b.pos.x += math.cos(angle)*0.4
        b.pos.z += math.sin(angle)*0.4
        if b.pos.x > 220: b.pos.x = -220

    for bf in mariposas:
        bf.pos.y = 4 + math.sin(angle*5 + bf.pos.x)*2
        bf.pos.x += math.sin(angle*2)*0.05

    for f in luciernagas:
        f.pos.y = 5 + math.sin(angle*6 + f.pos.x)*2
        f.color = vector(1, 1, random.uniform(0.3, 0.8))

    for r in conejos:
        r.pos.x += math.sin(angle*2 + r.pos.z)*0.03
        r.pos.z += math.cos(angle*2 + r.pos.x)*0.03

    for f in zorros:
        f.pos.x += math.sin(angle*1.5 + f.pos.z)*0.04
        f.pos.z += math.cos(angle*1.5 + f.pos.x)*0.04

    for d in ciervo:
        d.pos.x += math.sin(angle*1.2)*0.02
        d.pos.z += math.cos(angle*1.2)*0.02

    for o in buho:
        o.pos.y = 15 + math.sin(angle*3 + o.pos.x)*2

    for l in llamas:
        l.pos.y = -0.5 + random.uniform(0, 2)
        l.radius = random.uniform(0.2, 0.5)
        l.color = vector(1, random.uniform(0.2, 0.5), 0)