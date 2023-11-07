""" This is going to be the main library file thingy im going to use throughout """
from vpython import *


class Ground(box):
    def __init__(self) -> None:
        """ Iniitalises a Ground object (a flat plane 50x50 centred at origin) """
        super().__init__(self, pos=vector(0, 0, 0),
            length=50,
            height=0,
            width=50,
            )


class Object(simple_sphere):
    def __init__(self, d: dict) -> None:
        newd: dict = {}
        for k, v in d.items():
            if isinstance(v, list):
                newd[k] = vector(*v)
            else:
                newd[k] = v

        super().__init__(**newd)




def main() -> None:
    pass

if __name__ == "__main__":
    main()