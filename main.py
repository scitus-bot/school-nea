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


refresh_rate = config[0]["refresh_rate"]
# round to ms
dt = round(1/refresh_rate, 3) 

# ground object
ground = box(pos=vector(0, 0, 0), size=vector(50, 0, 50))
g = config[0]["g_accel"]

objects: list[simple_sphere] = []

# for i in range(len(config[1])):
    # objects.append(Object(config[1][i]))


ball = Object(config[1][0])

""" Loop section """
while True:
    # rate(refresh_rate)
    sleep(dt/1000)
    if pause: continue
    
    ball.pos += ball.v*dt
    ball.v.y += g*dt

    if ball.pos.y < ball.radius:
        ball.pos.y = ball.radius
        ball.v.y *= -1
    
    
    
    # for obj in objects:

    #     obj.pos = obj.pos + obj.v*dt
    #     obj.v.y += g*dt
        
    #     if obj.pos.y < obj.radius:
    #         obj.pos.y = obj.radius
    #         obj.v.y *= -0.50
    

    # sleep(dt/1000)