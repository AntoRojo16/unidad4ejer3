from tkinter import *
from tkinter import ttk
class Aplicacion():
    

    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title("Conversor de moneda")
        self.__ventana.geometry("300x100")
        self.__dolares=StringVar()
        self.__pesos=StringVar()
        mainframe=ttk.Frame(self.__ventana,padding=(10,10,10,10))
        mainframe.grid()
        self.__dolares.trace("w",self.calcular)
        texto1=ttk.Label(mainframe,text="Es equivalente a",padding=(5,5))
        texto1.grid(column=0,row=1)
        self.valor=ttk.Entry(mainframe,textvariable=self.__dolares,width=7)
        self.valor.grid(column=1,row=0)
        dolar=ttk.Label(mainframe,text="dolares",padding=(10,10))
        dolar.grid(column=2,row=0)
        peso=ttk.Label(mainframe,text="pesos",padding=(10,10))
        peso.grid(column=2,row=1)
        mustra=ttk.Label(mainframe,textvariable=self.__pesos,padding=(5,5))
        mustra.grid(column=1,row=1)
        self.__ventana.mainloop()
    def calcular(self,*args):
        num=0
        num=self.valor.get()
        print(num)
        self.__pesos.set(400*num)
    
    





if __name__=="__main__":
    aplicacion=Aplicacion()
