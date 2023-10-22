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


class Object(simple_sphere):
    def __init__(self, d):
        for k, v in d.items():
            if not isinstance(v, list):
                setattr(self, k, v)
            else:
                setattr(self, k, vector(*v))
                
        





def main() -> None:
    pass

if __name__ == "__main__":
    main()