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

# if on the ground/on a planet
if config[1]["type"] == "normal":

    # ground object
    ground = box(pos=vector(0, 0, 0), size=vector(50, 0, 50))

    # setting up relevent constants
    g = config[0]["g_accel"]
    refresh_rate = config[0]["refresh_rate"]
    # round to ms
    dt = round(1/refresh_rate, 3) 

    
    objects: list[simple_sphere] = []
    # for i in range(len(config[1])):
        # objects.append(Object(config[1][i]))



    ball = Object(config[1][0])



    """ Loop section """
    while True:
        sleep(dt)
        if pause: continue
        
        ball.pos += ball.v*dt
        ball.v.y += g*dt

        if ball.pos.y < ball.radius:
            # ball.pos.y = ball.radius
            ball.v.y *= -0.75
        
        