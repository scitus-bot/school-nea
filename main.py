import json
from physics import *
from time import sleep
from vpython import *




""" Simulator set-up """

config_file = "config.json"

with open(config_file, "r") as cf:
    file_content_str: str = "".join([l.strip() for l in cf.readlines()])
    config: dict = json.loads(file_content_str)


# if true then the sim. pauses 
pause = False

def pause_button(b) -> None:
    """ Pauses the simulation and changed the button text """
    global pause
    pause = not pause
    b.text = "Pause" if not pause else "Run"

button(bind=pause_button, text="Pause")



""" Physics Related Stuff starts here """

def object_from_dict(data: dict) -> simple_sphere:
    obj = simple_sphere()
    
    # all the yucky vector ones
    # in X Y Z
    obj.pos = vector(
        data["init_pos"][0], data["init_pos"][1], data["init_pos"][2]
    )
    
    obj.v = vector(
        data["init_vel"][0], data["init_vel"][1], data["init_vel"][2]
    )
    
    # in R G B 
    obj.color = vector(
        data["colour"][0], data["colour"][1], data["colour"][2]
    )
    
    obj.m = data["mass"]
    obj.cd = data["drag_coefficient"]
    obj.A = data["projected_area"]
    obj.make_trail = data["make_trail"]
    obj.radius = data["size"]

    return obj




refresh_rate = config[0]["refresh_rate"]
# round to ms
dt = round(1/refresh_rate, 3) 

# ground object
ground = Ground()
g = config[0]["g_accel"]

objects: list[simple_sphere] = []

for i in range(len(config[1])):
    objects.append(object_from_dict(config[1][i]))




""" Loop section """
while True:
    if pause: continue
    for obj in objects:

        obj.pos = obj.pos + obj.v*dt
        obj.v.y += g*dt
        
        if obj.pos.y < obj.radius:
            obj.pos.y = obj.radius
            obj.v.y *= -0.50
    
    sleep(dt/1000)