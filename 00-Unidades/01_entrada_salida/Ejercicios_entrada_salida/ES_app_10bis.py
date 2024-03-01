import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.clientes = []

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        nombre = prompt("Nombre:")
        if not nombre:
            return
        edad = int(prompt("Edad:"))
        if edad <= 12:
            alert("Error", "La edad debe ser mayor a 12")
            return
        altura = float(prompt("Altura:"))
        if altura < 0:
            alert("Error", "La altura no puede ser negativa")
            return
        dias_asistencia = int(prompt("Días que asiste a la semana (1, 3, 5):"))
        if dias_asistencia not in [1, 3, 5]:
            alert("Error", "Los días de asistencia deben ser 1, 3 o 5")
            return
        peso_muerto = float(prompt("Kilos que levanta en peso muerto:"))
        if peso_muerto <= 0:
            alert("Error", "El peso muerto debe ser mayor a cero")
            return

            cliente = Cliente(nombre, edad, altura, dias_asistencia, peso_muerto)
            self.clientes.append(cliente)

        def calcular_promedio_peso_tres_dias(clientes):
            pesos = [cliente.peso_muerto for cliente in clientes if cliente.dias_asistencia == 3]
            if pesos:
                return sum(pesos) / len(pesos)
            else:
                return 0

        def porcentaje_asiste_un_dia(clientes):
            total_clientes = len(clientes)
            if total_clientes == 0:
                return 0
            else:
                return (sum(1 for cliente in clientes if cliente.dias_asistencia == 1) / total_clientes) * 100

        def cliente_mas_alto(clientes):
            if not clientes:
                return None
            cliente_mas_alto = max(clientes, key=lambda x: x.altura)
            return cliente_mas_alto.nombre, cliente_mas_alto.edad

        def dias_mas_elegidos(clientes):
            dias = [cliente.dias_asistencia for cliente in clientes]
            dias_count = {1: dias.count(1), 3: dias.count(3), 5: dias.count(5)}
            return max(dias_count, key=dias_count.get)

        def cliente_mas_joven_cinco_dias(clientes):
            clientes_cinco_dias = [cliente for cliente in clientes if cliente.dias_asistencia == 5]
            if not clientes_cinco_dias:
                return None, None
            cliente_mas_joven = min(clientes_cinco_dias, key=lambda x: x.edad)
            return cliente_mas_joven.nombre, cliente_mas_joven.peso_muerto

        nombre = prompt("Nombre")
        if not nombre:
            return
        edad = int(prompt("Edad"))
        if edad <= 12:
            alert("Error", "La edad debe ser mayor a 12")
            return
        altura = float(prompt("Altura"))
        if altura < 0:
            alert("Error", "La altura no puede ser negativa")
            return
        dias_asistencia = int(prompt("Días que asiste a la semana (1, 3, 5)"))
        if dias_asistencia not in [1, 3, 5]:
            alert("Error", "Los días de asistencia deben ser 1, 3 o 5")
            return
        peso_muerto = float(prompt("Kilos que levanta en peso muerto"))
        if peso_muerto <= 0:
            alert("Error", "El peso muerto debe ser mayor a cero")
            return

        cliente = Cliente(nombre, edad, altura, dias_asistencia, peso_muerto)
        self.clientes.append(cliente)

        promedio_peso_tres_dias = calcular_promedio_peso_tres_dias(self.clientes)
        porcentaje_un_dia = porcentaje_asiste_un_dia(self.clientes)
        nombre_cliente_mas_alto, edad_cliente_mas_alto = cliente_mas_alto(self.clientes)
        dias_mas_elegido = dias_mas_elegidos(self.clientes)
        nombre_cliente_mas_joven_cinco_dias, peso_cliente_mas_joven_cinco_dias = cliente_mas_joven_cinco_dias(self.clientes)

        alert("Resultados",
            f"Promedio de kilos levantados por personas que asisten 3 días a la semana: {promedio_peso_tres_dias}\n"
            f"Porcentaje de clientes que asisten solo 1 día a la semana: {porcentaje_un_dia}%\n"
            f"Nombre y edad del cliente más alto: {nombre_cliente_mas_alto}, {edad_cliente_mas_alto}\n"
            f"Días más elegidos por los clientes: {dias_mas_elegido}\n"
            f"Nombre y kilos levantados en peso muerto por el cliente más joven que asiste 5 días a la semana: {nombre_cliente_mas_joven_cinco_dias}, {peso_cliente_mas_joven_cinco_dias}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()