from physics import *
from time import sleep
from vpython import *

# want all objects defined in this way
# none of this one-line object defining
ground = Ground(
    g_accel=-9.81
)


x, y, z = 0, 1, 0
r_b = 1

ball = Object(
    pos=vector(x, y, z),
    color=color.red,
    make_trail=True
)

ball_label = label(
    xoffset=100,
    yoffset=50
)


a = ground.acceleration
vy = 10 # initial velocity 
vx = 10
refresh_rate = 60
dt = 1/60 # should decide on a single value of dt that i use for now (later) 

while True:
    
    # chaning the balls position
    y += vy*dt
    vy += a*dt
    x += vx*dt
    ball.set_pos(x, y, z)    

    # adjusting the label so it shows accurate info 
    ball_label.text = f"y = {round(y, 2)}\nvy = {round(vy, 2)}"
    ball_label.pos = ball.pos

    # so that the obj doesnt fall underneath the surface
    if y < r_b:
        vy *= -0.70 # making it not -1 makes it so that it eventually stops bouncing
        vx *= 0.75

    sleep(dt)