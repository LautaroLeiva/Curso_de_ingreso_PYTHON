import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        max_num = prompt("Ingrese un número", "Por favor, ingrese un número:")
        if max_num:
                max_num = int(max_num)
                numeros_primos = []
                for num in range(2, max_num + 1):
                    es_primo = True
                    for i in range(2, int(num * 0.5) + 1):
                        if num % i == 0:
                            es_primo = False
                            break
                    if es_primo:
                        numeros_primos.append(num)
                mensaje_alerta = "Números primos encontrados:\n"
                for primo in numeros_primos:
                    mensaje_alerta += str(primo) + "\n"
                mensaje_alerta += f"\nCantidad de números primos encontrados: {len(numeros_primos)}"
                alert("Números Primos", mensaje_alerta)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()