""" This is going to be the main library file thingy im going to use throughout """
from vpython import *



class Ground(box):
    def __init__(self, g_accel: float, **args) -> None:
        """ Iniitalises a Ground object (a flat plane 50x50 centred at origin) """
        super().__init__(
            pos=vector(0, 0, 0),
            length=50,
            height=0,
            width=50,
            **args,
            )
        self.acceleration = g_accel


class Object(sphere):
    def __init__(self, **args) -> None:
        super().__init__(
            radius=1,
            **args
            )
        
    def set_pos(self, newX: float, newY: float, newZ: float) -> None:
        self.pos = vector(newX, newY, newZ)






def main() -> None:
    pass

if __name__ == "__main__":
    main()