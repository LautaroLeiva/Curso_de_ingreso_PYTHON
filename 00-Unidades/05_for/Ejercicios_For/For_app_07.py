import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # Pedir al usuario un número
        numero = prompt("Ingrese un número", "Número")

        if numero:
            numero = int(numero)
            if numero <= 1:
                alert("Resultado", f"{numero} no es un número primo.")
            else:
                es_primo = True
        for i in range(2, int(numero * 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            alert("Resultado", f"{numero} es un número primo.")
        else:
            alert("Resultado", f"{numero} no es un número primo.")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()