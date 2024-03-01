import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT)  

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #! 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #! 2) - Tecnología que mas se votó.
    #! 3) - Porcentaje de empleados por cada genero
    #! 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #! 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #! 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        seguir = True

        nombre_minimo = ""
        genero_minimo = ""

        contador_masculino_IOT_IA = 0

        contador_IOT = 0
        contador_IA = 0
        contador_RV_RA = 0

        contador_mas = 0
        contador_fem = 0
        contador_otro = 0

        contador_IOT_edad = 0

        contador_femenino_IA = 0
        acumulador_edad_femenino_IA = 0

        bandera_primer_RV_RA = False

        minimo_edad = 0

        while seguir == True:
            #ingreso de datos
            nombre = input("Ingrese su nombre")
    
            edad = input("ingrese su edad")
            edad = int(edad)
            while  edad < 18:
                edad = input("Reingrese su edad")
                edad = int(edad)

            genero = input("Ingrese genero")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input("Reingreso genero")

            tecnologia = input("Ingrese tecnologia")
            while tecnologia != "IA" and tecnologia != "IOT" and tecnologia != "RC/RA":
                tecnologia = input("Reingreso tecnologia")

            #procesamiento de datoas (repite)
            #! 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
            if genero == "Masculino" and tecnologia == "IOT" or tecnologia == "IA" and edad >= 25 and edad <= 50:
                contador_masculino_IOT_IA += 1

            #2) - Tecnologia que mas se votó   ( se puede hacer con if)
            match tecnologia :
                case "IOT":
                    contador_IOT += 1
                    #! 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.
                    if (edad > 18 and edad < 25) or (edad > 33 and edad < 42):
                        contador_IOT_edad += 1
                case "IA" :
                    contador_IA += 1
                case "RV_RA":
                    contador_RV_RA += 1
                    #! 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
                    if edad < minimo_edad or bandera_primer_RV_RA == False :
                        minimo_edad = edad
                        nombre_minimo = nombre
                        genero_minimo = genero
                        bandera_primer_RV_RA = True

            #! 3) - Porcentaje de empleados por cada genero
            match genero:
                case "Masculino":
                    contador_mas += 1
                case "Femenino":
                    contador_fem += 1
                    #! 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
                    if tecnologia == "IA":
                        contador_femenino_IA += 1
                        acumulador_edad_femenino_IA += edad
                case _:
                    contador_otro += 1


            seguir = question("Seguir", "Ingresa otro empleado?")

        #procesamiento de datoas (no se repite)
        #2)- Tecnologia que mas se votó 
        if contador_IOT > contador_IA and contador_IOT > contador_RV_RA:
            mas_votado = "2. se voo mas a IOT"
        elif contador_IA > contador_IOT and contador_IA > contador_RV_RA:
            mas_votado = "2. se voo mas a IA"
        else:
            mas_votado = "2. se voo mas a RV_RA"

        #! 3) - Porcentaje de empleados por cada genero
        total_empleados = contador_otro + contador_fem + contador_mas

        porcentaje_fem = (contador_fem * 100) / total_empleados
        porcentaje_mas = (contador_mas * 100) / total_empleados
        porcentaje_otro = 100 - (porcentaje_fem + porcentaje_mas)

        #! 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.

        porcentaje_IOT_edad = (contador_IOT_edad * 100) / total_empleados

        #! 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA

        if contador_femenino_IA > 0:
            promedio_edad_femenino = acumulador_edad_femenino_IA / contador_femenino_IA
        else:
            promedio_edad_femenino = "No se ingresaron femeninos que votaron IA"




        #salidas
        print("1. la cantidad Masculinos que votaron IA / IOT {0}".format(contador_masculino_IOT_IA))
        print("{0}".format(mas_votado))
        print("3. Porcentajes:\n\tMasculino {0}\n\tFemenino {1}\n\tOtro {2} ".format(porcentaje_mas,porcentaje_fem,porcentaje_otro))
        print("4. Porcentaje IOT rango edad. {0}".format(porcentaje_IOT_edad))
        print("5. Promedio de edad {0}".format(promedio_edad_femenino))
        print("6. {0} {1} {2}".format(minimo_edad, nombre_minimo, genero_minimo))


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
