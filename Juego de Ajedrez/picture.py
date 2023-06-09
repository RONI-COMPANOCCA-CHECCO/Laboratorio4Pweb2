import chessPictures
import tkinter as tk

class Game():
    def __init__(self, L_QUADRADO):
        self.gs = chessPictures.gameState()
        self.L_QUADRADO = L_QUADRADO
        self.img = {}

        self.ventana = tk.Tk()
        self.ventana.title("AJEDREZ")
        self.ventana.geometry(f"{str(L_QUADRADO*8)}x{str(L_QUADRADO*8)}")
        self.ventana.resizable(0,0)

        self.interfaz = tk.Canvas(Self.ventana)
        self.interfaz.pack(fill="both", expand=tk.true)
    
    def __call__(self):
        self.ventana.mainloop()

    def chessPicture(self):
        for i in range(8):
            for j in range(8):
                if(i+j) % 2 == 0:
                    self.interfaz.create_rectangle(i*self.L_QUADRADO, j*self.L_QUADRADO, (i+1)*self.L_QUADRADO, (j+1)*self.L_QUADRADO, fill="#dfc07f")
                else:
                    self.interfaz.create_rectangle(i*self.L_QUADRADO, j*self.L_QUADRADO, (i+1)*self.L_QUADRADO, (j+1)*self.L_QUADRADO, fill="#7a4f37")
    
    def ocuparImgen(self):
        piezas = ["bB","bK","bN","bp","bQ","bR","wB","wK","wN","wp","wQ","wR"]
        for pieza in piezas:
            self.img[pieza] = tk.PhotoImage(file="./img/"+pieza+".png").zoom(self.L_QUADRADO).subsample(60)

    def mostrarPiezas(self):
        for indice_i, i in enumerate(self.gs.piezas):
            for indice_j, j in enumerate(i):
                if j!="--":
                    self.interfaz.create_image(indice_j*self.L_QUADRADO, indice_i*self.L_QUADRADO, image=self.img[j], anchor="nw")

TableroAjedrez = Game(70)
TableroAjedrez.chessPicture()
TableroAjedrez.ocuparImgen()
TableroAjedrez.mostrarPiezas()

TableroAjedrez()
