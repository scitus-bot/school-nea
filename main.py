from time import sleep
from vpython import *


class Ground(box):
    def __init__(self, **args):
        super().__init__(
            pos=vector(0, 0, 0), 
            length=50,
            height=0,
            width=50,
            **args
            )
        
        
        
class Object(sphere):
    def __init__(self, **args):
        super().__init__(**args)
        
        
        
        
        
ground = Ground()




x, y, z = 0, 10, 0
r_b = 1
ball = sphere(
    pos=vector(x, y, z),
    radius=r_b,
    color=color.red
)

ball_label = label(
    xoffset=100,
    yoffset=50
)



a = -9.81
dt = 0.01
v = 0

while True:
    
    # chaning the balls position
    y += v*dt
    v += a*dt
    ball.pos = vector(x, y, z)

    # adjusting the label so it shows accurate info 
    ball_label.text = f"vy = {round(v, 2)}"
    ball_label.pos = ball.pos

    # so that the obj doesnt fall underneath the surface
    if y < r_b:
        v *= -0.90


    sleep(dt/1000)