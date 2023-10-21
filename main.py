from physics import *
from time import sleep
from vpython import *



refresh_rate = 60
dt = round(1/refresh_rate, 3) # round to ms 


# want all objects defined in this way
# none of this one-line object defining
ground = Ground(
    g_accel=-9.81
)


# initial ball features
x, y, z = 0, 10, 0
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
# initial velocities
vy = 10
vx = 5

# if true then the sim. pauses 
pause = False

def pause_button(b) -> None:
    """ Pauses the simulation and changed the button text """
    global pause
    pause = not pause
    b.text = "Pause" if not pause else "Run"

button(bind=pause_button, text="Pause")

while True:
    # pause the sim. (do no processing) if the sim. is paused
    if pause: continue
    
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

        # if vy < epsilon: vy = 0
        # if vx < epsilon: vx = 0


    sleep(round(dt, 3))