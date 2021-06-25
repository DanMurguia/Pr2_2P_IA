from tkinter import *
import tkinter as tk
from tkinter import filedialog
import genetico2


class MainWindow(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Algoritmo Genetico")
        self.parent.geometry("750x650")
        self.configure(bg='#6B0002')
        self.filename = ""
        self.var_key = StringVar()
        self.var_iv = StringVar()
        self.var_funcion = IntVar()
        self.var_cromosoma = IntVar()
        self.var_gen = IntVar()
        self.var_ekis = IntVar()
        self.var_modo = IntVar()
        self.ivname=""
        self.imagen = []
        self.img_enc = []
        self.cabecera = []
    
        lbl = tk.Label(self, text="Algoritmo genetico",font=('Arial',32,'bold italic')
                        ,background='#6B0002', foreground = '#91722F')
        lbl.grid(row=0,column=0,columnspan=5, padx=140, pady=15)        
        
        lblmod = tk.Label(self, text="Seleccione una función",
                         font=('Arial',18,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=1,column=0,columnspan=3,pady=15)
        
        
        rad0 = Radiobutton(self,text='x^2', value=1,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_funcion)
        rad0.grid(row=2, column=0)
        
        rad1 = Radiobutton(self,text='sin(x) * 40', value=2,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_funcion)
        rad1.grid(row=2, column=1) 
        
        rad2 = Radiobutton(self,text='cos(x)+x', value=3,
                           font=('Arial',14,'bold italic'),
                           background='#6B0002',foreground = '#968118',variable=self.var_funcion)
        rad2.grid(row=2, column=2)

        rad3 = Radiobutton(self,text='[1000/|(50-x)|]+x', value=4,
                           font=('Arial',14,'bold italic'),
                           background='#6B0002',foreground = '#968118',variable=self.var_funcion)
        rad3.grid(row=3, column=0, pady=15)
        
        rad4 = Radiobutton(self,text='[1000/|(30-x)|]+[1000/|(50-x)|]+[1000/|(80-x)|]+x', value=5,
                           font=('Arial',11,'bold italic'),
                           background='#6B0002',foreground = '#968118',variable=self.var_funcion)
        rad4.grid(row=3, column=1, pady=15, columnspan=2, padx=15 )
        
                
        lblmod = tk.Label(self, text="Seleccione lo que desea buscar",
                         font=('Arial',18,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=4,column=0,columnspan=3 ,pady=15)
        
        
        rad0 = Radiobutton(self,text='Máximo', value=1,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_modo)
        rad0.grid(row=5, column=0)
        
        rad1 = Radiobutton(self,text='Mínimo', value=2,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_modo)
        rad1.grid(row=5, column=1)
        
        lblmod = tk.Label(self, text="Ingrese los parametros adicionales",
                         font=('Arial',18,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=6,column=0,columnspan=3 ,pady=15)
        
        lblmod = tk.Label(self, text="Num. Cromosomas:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=7,column=0 ,pady=15)
        
        self.cromosoma = tk.Entry(self, width = 5,textvariable=self.var_cromosoma,
                             font=('Arial',14))
        self.cromosoma.grid(row=7, column=1)

        lblmod = tk.Label(self, text="Num Generaciones:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=8,column=0 ,pady=15)
        
        self.gen = tk.Entry(self, width = 5,textvariable=self.var_gen,
                             font=('Arial',14))
        self.gen.grid(row=8, column=1)
        
        lblmod = tk.Label(self, text="Intervalo de X:",
                         font=('Arial',14,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=9,column=0 ,pady=15)
        
        self.ekis = tk.Entry(self, width = 5,textvariable=self.var_ekis,
                             font=('Arial',14))
        self.ekis.grid(row=9, column=1)
                
        btn_Descifrar = tk.Button(self, text="Iniciar", 
                               bg='#4B7D23',width=10,height = 2, command=self.init,
                               foreground='white',font=('Arial',10,'bold italic'))
        btn_Descifrar.grid(row=10,column=1,pady=20)
        
        
    def init(self):
        funcion = self.var_funcion.get()
        modo = self.var_modo.get()
        cromo = self.var_cromosoma.get()
        gens = self.var_gen.get()
        x = self.var_ekis.get()
        genetico2.init(funcion,modo,cromo,gens,x)
        

        
        
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
