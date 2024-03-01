import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Lautaro
apellido:Leiva
---
Ejercicio: entrada_salida_02
---
Enunciado:
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Ventana")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_f = 0
        contador_m = 0
        contador_gato = 0
        contador_perro = 0
        contador_exotico = 0
        nombre_mascota_menos_pesada = ""
        tipo_mascota_menos_pesada = ""
        peso_mascota_menos_pesada = float('inf')
        nombre_perro_mas_joven = ""
        edad_perro_mas_joven = float('inf')
        acumulador_peso_total = 0
        cantidad_mascotas = 5
        
        for _ in range(cantidad_mascotas):
            nombre = prompt("Ingrese el nombre de la mascota:", "Nombre")
            if nombre is None:
                return  # Entrada cancelada por el usuario, función de salida
            
            tipo = prompt("Ingrese el tipo de mascota (gato, perro o exotico):", "Tipo")
            if tipo is None:
                return
            
            peso_str = prompt("Ingrese el peso de la mascota (entre 10 y 80):", "Peso")
            if peso_str is None:
                return
            peso = float(peso_str)
            while peso < 10 or peso > 80:
                peso_str = prompt("Peso fuera de rango. Ingrese el peso de la mascota (entre 10 y 80):", "Peso")
                if peso_str is None:
                    return
                peso = float(peso_str)
            
            sexo = prompt("Ingrese el sexo de la mascota (F o M):", "Sexo")
            if sexo is None:
                return
            while sexo.upper() not in ['F', 'M']:
                sexo = prompt("Sexo no válido. Ingrese el sexo de la mascota (F o M):", "Sexo")
                if sexo is None:
                    return
            
            edad_str = prompt("Ingrese la edad de la mascota (mayor a 0):", "Edad")
            if edad_str is None:
                return
            edad = int(edad_str)
            while edad <= 0:
                edad_str = prompt("Edad no válida. Ingrese la edad de la mascota (mayor a 0):", "Edad")
                if edad_str is None:
                    return
                edad = int(edad_str)
            
            # Informe A - Sexo menos ingresado
            if sexo.upper() == 'F':
                contador_f += 1
            elif sexo.upper() == 'M':
                contador_m += 1
            
            # Informe B - Porcentaje de mascotas por tipo
            if tipo.lower() == 'gato':
                contador_gato += 1
            elif tipo.lower() == 'perro':
                contador_perro += 1
            elif tipo.lower() == 'exotico':
                contador_exotico += 1
            
            # Informe C - Mascota menos pesada
            if peso < peso_mascota_menos_pesada:
                nombre_mascota_menos_pesada = nombre
                tipo_mascota_menos_pesada = tipo
                peso_mascota_menos_pesada = peso
            
            # Informe D - Perro más joven
            if tipo.lower() == 'perro' and edad < edad_perro_mas_joven:
                nombre_perro_mas_joven = nombre
                edad_perro_mas_joven = edad
            
            # Informe E - Promedio de peso de todas las mascotas
            acumulador_peso_total += peso
        
        # Calcular porcentajes
        porcentaje_f = (contador_f / cantidad_mascotas) * 100
        porcentaje_m = (contador_m / cantidad_mascotas) * 100
        porcentaje_gato = (contador_gato / cantidad_mascotas) * 100
        porcentaje_perro = (contador_perro / cantidad_mascotas) * 100
        porcentaje_exotico = (contador_exotico / cantidad_mascotas) * 100
        
        # Calcular promedio de peso
        promedio_peso = acumulador_peso_total / cantidad_mascotas
        
        # Mostrar resultados
        alert("Informes",
            f"Informe A: El sexo menos ingresado es {'Femenino' if contador_f < contador_m else 'Masculino'}\n"
            f"Informe B: Porcentaje de mascotas por tipo:\n"
            f"\tGato: {porcentaje_gato}%\n"
            f"\tPerro: {porcentaje_perro}%\n"
            f"\tExótico: {porcentaje_exotico}%\n"
            f"Informe C: La mascota menos pesada es un/a {tipo_mascota_menos_pesada} llamado/a {nombre_mascota_menos_pesada} con un peso de {peso_mascota_menos_pesada} kg\n"
            f"Informe D: El perro más joven se llama {nombre_perro_mas_joven} y tiene {edad_perro_mas_joven} años\n"
            f"Informe E: El promedio de peso de todas las mascotas es {promedio_peso:.2f} kg")
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()