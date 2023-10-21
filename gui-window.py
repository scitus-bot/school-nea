""" GUI """
from tkinter import *
from typing_extensions import Literal

window = Tk()


# frame that holds the general environmental attributes
frm_gen_info = Frame(
    master=window,
    relief=RIDGE,
    borderwidth=5,
)

# frame that holds the frames that hold the object attributes
frm_objects = Frame(
    master=window,
    relief=SUNKEN,
    borderwidth=5,
)



label = Label(
    text="Environmental Attributes",
    master=frm_gen_info,
)
label.pack()



lbl_obj = Label(
    text="Test objects",
    master=frm_objects,
)
lbl_obj.pack()

ent_obj_name = Entry(
    width=50,
    master=frm_objects,
)
ent_obj_name.insert(0, "Object1")
ent_obj_name.pack()




frm_gen_info.pack(side=LEFT)
frm_objects.pack(side=RIGHT)

window.mainloop()