from physics import *
from time import sleep
from vpython import *


# want all objects defined in this way
# none of this one-line object defining
ground = Ground(
    g_accel=-9.81
)


x, y, z = 0, 10, 0
r_b = 1

ball = Object(
    pos=vector(x, y, z),
    color=color.red,
)

ball_label = label(
    xoffset=100,
    yoffset=50
)


a = ground.acceleration
v = 0 # initial velocity 
dt = 0.01 # should decide on a single value of dt that i use for now (later) 

while True:
    
    # chaning the balls position
    y += v*dt
    v += a*dt
    ball.set_pos(x, y, z)    

    # adjusting the label so it shows accurate info 
    ball_label.text = f"vy = {round(v, 2)}"
    ball_label.pos = ball.pos

    # so that the obj doesnt fall underneath the surface
    if y < r_b:
        v *= -0.90


    sleep(dt/1000)