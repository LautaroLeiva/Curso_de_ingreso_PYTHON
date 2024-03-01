import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
"""""
Enunciado:
De los 50 participantes del torneo de UTN-TETRIS, se debe ingresar los siguientes datos:
Nombre
Categoría (Principiante - Intermedio - Avanzado)
Edad (entre 18 y 99 inclusive)
Score (mayor que 0)
Nivel alcanzado (1 , 2 o 3)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál es la categoría que tiene menos participantes.
Informe B- El Porcentaje de jugadores de la categoría intermedios sobre el total
Informe C- La categoría del participante de mayor Score
Informe D- El score y nombre del intermedios con menor score
Informe E- Promedio de score de los participantes avanzados.
"""
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Ventana")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_principiante = 0
        contador_intermedio = 0
        contador_avanzado = 0
        suma_score_avanzado = 0
        max_score = float('-inf')
        max_score_categoria = ""
        menor_score_intermedio = float('inf')
        nombre_menor_score_intermedio = ""
        suma_score_menor_intermedio = 0

        while True:
            nombre = prompt("Ingrese el nombre del participante:", "Nombre")
            if nombre is None:
                break
            categoria = prompt("Ingrese la categoría del participante (Principiante - Intermedio - Avanzado):", "Categoría")
            while categoria.lower() not in ['principiante', 'intermedio', 'avanzado']:
                categoria = prompt("Categoría no válida. Ingrese la categoría del participante (Principiante - Intermedio - Avanzado):", "Categoría")
            edad = int(prompt("Ingrese la edad del participante (entre 18 y 99 años inclusive):", "Edad"))
            while edad < 18 or edad > 99:
                edad = int(prompt("Edad fuera de rango. Ingrese la edad del participante (entre 18 y 99 años inclusive):", "Edad"))
            score = float(prompt("Ingrese el score del participante (mayor que 0):", "Score"))
            while score <= 0:
                score = float(prompt("Score no válido. Ingrese el score del participante (mayor que 0):", "Score"))
            nivel_alcanzado = int(prompt("Ingrese el nivel alcanzado por el participante (1, 2 o 3):", "Nivel Alcanzado"))
            while nivel_alcanzado not in [1, 2, 3]:
                nivel_alcanzado = int(prompt("Nivel alcanzado no válido. Ingrese el nivel alcanzado por el participante (1, 2 o 3):", "Nivel Alcanzado"))


            if categoria.lower() == 'principiante':
                contador_principiante += 1
            elif categoria.lower() == 'intermedio':
                contador_intermedio += 1

                if score < menor_score_intermedio:
                    menor_score_intermedio = score
                    nombre_menor_score_intermedio = nombre
                suma_score_menor_intermedio += score
            elif categoria.lower () == 'avanzado':
                contador_avanzado += 1
                suma_score_avanzado += score

            #Informe C
            if score > max_score:
                max_score= score
                max_score_categoria = categoria

        #Informe A
        categoria_menos_participantes = min(contador_principiante, contador_intermedio, contador_avanzado)

        #Informe B 
        porcentaje_intermedio_total = (contador_intermedio / (contador_principiante + contador_intermedio + contador_avanzado)) * 100

        # Informe D 
        promedio_score_intermedio = suma_score_menor_intermedio / contador_intermedio if contador_intermedio > 0 else 0


        #RESULTADOS
        alert("Informes",
            f"Informe A: La categoría con menos participantes es {'Principiante' if categoria_menos_participantes == contador_principiante else 'Intermedio' if categoria_menos_participantes == contador_intermedio else 'Avanzado'}\n"
            f"Informe B: El porcentaje de jugadores intermedios sobre el total es {porcentaje_intermedio_total:.2f}%\n"
            f"Informe C: La categoría del participante con mayor score es {max_score_categoria}\n"
            f"Informe D: El score y nombre del intermedio con menor score es {menor_score_intermedio} - {nombre_menor_score_intermedio}\n")




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()