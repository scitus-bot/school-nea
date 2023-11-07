import json
import sys
from physics import *
from time import sleep
from vpython import *




""" Simulator set-up """

config_file: str = "config.json"

with open(config_file, "r") as cf:
    file_content_str: str = "".join([l.strip() for l in cf.readlines()])
    config: dict = json.loads(file_content_str)



# if true then the sim. pauses 
pause: bool = False

def pause_button(b) -> None:
    """ Pauses the simulation and changed the button text """
    global pause
    pause = not pause
    b.text = "Pause" if not pause else "Run"

button(bind=pause_button, text="Pause")

def end_button(b) -> None:
    """ Ends the simulation when pressed. """
    sys.exit()

button(bind=end_button, text="End Simulation")



""" Physics Related Stuff starts here """

# if on the ground/on a planet
if config[0]["type"] == "normal":

    # ground object
    ground: box = box(pos=vector(0, 0, 0), size=vector(50, 0, 50))

    # setting up relevent constants
    g: float = config[0]["g_accel"]
    refresh_rate: int = config[0]["refresh_rate"]
    # round to ms
    dt: float = round(1/refresh_rate, 3) 


    objects: list[simple_sphere] = []
    # for i in range(len(config[1])):
        # objects.append(Object(config[1][i]))



    ball: Object = Object(config[1][0])

    """ poor mans select case 
    0 -> position
    1 -> velocity
    2 -> acceleration
    anything else is text and will be displayed as is
    """
    txt: str = ""
    if ball.label == 0:
        txt = ball.pos
    elif ball.label == 1:
        txt = ball.v 
    elif ball.label == 2:
        txt = ball.a 
    elif ball.label == -1:
        txt = None
    else:
        txt = str(ball.label)
    
    # the ball's label 
    ball_lbl: label = label(
        pos=ball.pos,
        text=txt,
        xoffset=40,
        yoffset=20
    )


    """ Loop section """
    while True:
        sleep(dt)
        if pause: continue
        
        # updating ball position and velocity
        ball.pos += ball.v*dt
        ball.v.y += g*dt

        # check collision with floor 
        if ball.pos.y < ball.radius:
            ball.pos.y = ball.radius
            ball.v.y *= -0.75
        
        ball_lbl.pos = ball.pos
        ball_lbl.text = ball.v
        