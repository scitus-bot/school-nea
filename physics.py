""" This is going to be the main library file thingy im going to use throughout """
from vpython import *



class Ground(box):
    def __init__(self, **args) -> None:
        """ Iniitalises a Ground object (a flat plane 50x50 centred at origin) """
        super().__init__(
            pos=vector(0, 0, 0),
            length=50,
            height=0,
            width=50,
            **args,
            )


class Object(sphere):
    def __init__(self, **args) -> None:
        super().__init__(
            radius=1,
            **args
            )
        
    def set_pos(self, new_pos: tuple) -> None:
        self.pos = vector(new_pos)






def main() -> None:
    pass

if __name__ == "__main__":
    main()