import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: Adivinaste el numero secreto ;)

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_secreto = 73  # Número secreto predefinido (podría ser generado aleatoriamente)
        intentos = 0
        
        for _ in range(7):  # Realiza un máximo de 7 intentos
            intentos += 1
            guess = prompt("Ingresa un número entre 1 y 100:")  # Proporciona el mensaje adecuado
            if guess is None:  # Si el usuario cancela el diálogo
                return 
                guess = int(guess)
                if guess == numero_secreto:
                    alert("Adivinaste", "¡Adivinaste el número secreto!")
                    return
                elif guess < numero_secreto:
                    alert("Falta...", f"El número secreto es mayor que {guess}")
                else:
                    alert("Se pasó...", f"El número secreto es menor que {guess}")
                
                if intentos == 1:
                    alert("Intento 1", "Usted es un psíquico")
                elif intentos == 2:
                    alert("Intento 2", "Excelente percepción")
                elif intentos == 3:
                    alert("Intento 3", "Esto es suerte")
                elif 4 <= intentos <= 6:
                    alert("Intento", "Excelente técnica")
                elif intentos == 7:
                    alert("Intento 7", "Perdiste, suerte para la próxima")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()