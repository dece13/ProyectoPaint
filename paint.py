import tkinter as tk
from tkinter import HORIZONTAL, Scale, ttk

class App(tk.Frame):
    def __init__(self):

        ## Estilos
        
        
        self.ventana1 = tk.Tk()
        self.ventana1.title("Mi Lienzo")
        self.colorFondo = "#FFFFFF"
        self.canvas1= tk.Canvas(self.ventana1, width = 600, height=400, background= self.colorFondo )
        self.canvas1.grid(column=0,row=0)

        
        
        self.botonRojo =tk.Button(text="",foreground="#ff0000",background="#ff0000",command=lambda:self.definir_color(0))
        self.botonRojo.place(x=100, y=0)
        self.botonNegro =tk.Button(text="", foreground="#ff0000",background="#000000",command=lambda:self.definir_color(1))
        self.botonNegro.place(x=120, y=0)
        self.botonAzul =tk.Button(text="",foreground="#ff0000",background="#0000ff" ,command=lambda:self.definir_color(2))
        self.botonAzul.place(x=140, y=0)
        self.botonAmarillo =tk.Button(text="",foreground="#ff0000",background="#ffff00" ,command=lambda:self.definir_color(3))
        self.botonAmarillo.place(x=160, y=0)
        self.botonVerde =tk.Button(text="",foreground="#ff0000",background="#00913f" ,command=lambda:self.definir_color(4))
        self.botonVerde.place(x=180, y=0)

        self.botonBorrador =tk.Button(text="Borrador",foreground="#ff0000",background=self.colorFondo ,command=lambda:self.definir_color(100))
        self.botonBorrador.place(x=220, y=0)
        
        self.vol = Scale(
           
            from_ = 1,
            to = 100,
            orient = HORIZONTAL ,
            resolution = 1,
            command=self.aumetar_grosor

        )
        self.vol.place(x=320, y=0)

        self.arrayColores = ["red","black","blue", "yellow", "green"]
        
        self.canvas1.bind("<ButtonPress-1>",self.boton_presion)
        self.canvas1.bind("<Motion>", self.mover_Mouse)
        self.canvas1.bind("<ButtonRelease-1>",self.boton_soltar)
        self.presionado=False
        self.color= "black"
        self.grosor= 3
        self.ventana1.mainloop()
    
    def definir_color(self, numero):
        
       if numero == 100:
           self.color = self.colorFondo
       else:
           self.color = self.arrayColores[numero]

                      

    def boton_presion(self, evento):
        self.presionado=True
        self.origenx=evento.x
        self.origeny=evento.y

    def boton_soltar(self, evento):
        self.presionado=False
    
    def mover_Mouse(self, evento):
        if self.presionado:
            # Dibuja una línea conectando el punto anterior con el nuevo punto para suavizar el trazo
            self.canvas1.create_line(self.origenx, self.origeny, evento.x, evento.y, fill=self.color, width=self.grosor, capstyle=tk.ROUND, smooth=True)
            self.origenx = evento.x
            self.origeny = evento.y
    
    def aumetar_grosor(self, _=None):
        self.grosor= self.vol.get()

    

appa=App()