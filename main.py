from tkinter import *

def elegir():
    monitor.config(text="{}".format(opcion.get()))
def reiniciar():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)


Radiobutton(root, text="River Plate", variable=opcion,
            value='River Plate', command=elegir).pack(anchor=N)
Radiobutton(root, text="Real Madrid", variable=opcion,
            value='Real Madrid', command=elegir).pack(anchor=N)
Radiobutton(root, text="Juventus", variable=opcion,
            value='Juventus', command=elegir).pack(anchor=N)


monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reiniciar).pack()

root.mainloop()