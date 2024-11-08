from tkinter import Tk, Label, Button, Entry, Toplevel, messagebox

class VentanaEconomica:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        ventana_principal.title("Ventana Principal - Economía")
        ventana_principal.geometry("400x400")
        
        # Botones para abrir las ventanas de ejercicios
        Button(ventana_principal, text="Costo de Oportunidad", command=self.abrir_ventana_costo_oportunidad, font=("Helvetica", 14), width=20, bg="#99ccff").pack(pady=10)
        Button(ventana_principal, text="Inflación", command=self.abrir_ventana_inflacion, font=("Helvetica", 14), width=20, bg="#99ccff").pack(pady=10)
        Button(ventana_principal, text="Producto Bruto Interno (PBI)", command=self.abrir_ventana_pbi, font=("Helvetica", 14), width=20, bg="#99ccff").pack(pady=10)
        Button(ventana_principal, text="Salir", command=ventana_principal.quit, font=("Helvetica", 14), width=20, bg="#ff6666").pack(pady=10)

    def abrir_ventana_costo_oportunidad(self):
        ventana_costo = Toplevel(self.ventana_principal)
        ventana_costo.title("Costo de Oportunidad")
        ventana_costo.geometry("400x300")
        
        Label(ventana_costo, text="Costo de oportunidad = Beneficio del bien sacrificado\n(valor del bien sacrificado)", font=("Helvetica", 12)).pack(pady=10)
        Label(ventana_costo, text="Descripción: Representa el costo de elegir un bien sobre otro.").pack(pady=10)
        
        Button(ventana_costo, text="Volver", command=ventana_costo.destroy, font=("Helvetica", 14), width=20, bg="#ff6666").pack(pady=10)

    def abrir_ventana_inflacion(self):
        ventana_inflacion = Toplevel(self.ventana_principal)
        ventana_inflacion.title("Tasa de Inflación")
        ventana_inflacion.geometry("400x300")
        
        Label(ventana_inflacion, text="Tasa de inflación = ((IPCt − IPCt-1) / IPCt-1) × 100", font=("Helvetica", 12)).pack(pady=10)
        Label(ventana_inflacion, text="Descripción: La inflación mide el aumento en los precios\nde los bienes y servicios en una economía.").pack(pady=10)
        
        Label(ventana_inflacion, text="Ingrese IPC actual (IPCt):").pack()
        self.ipc_actual = Entry(ventana_inflacion)
        self.ipc_actual.pack(pady=5)
        
        Label(ventana_inflacion, text="Ingrese IPC del año anterior (IPCt-1):").pack()
        self.ipc_anterior = Entry(ventana_inflacion)
        self.ipc_anterior.pack(pady=5)
        
        Button(ventana_inflacion, text="Calcular Inflación", command=self.calcular_inflacion, font=("Helvetica", 14), width=20, bg="#99ccff").pack(pady=10)
        Button(ventana_inflacion, text="Volver", command=ventana_inflacion.destroy, font=("Helvetica", 14), width=20, bg="#ff6666").pack(pady=10)

    def abrir_ventana_pbi(self):
        ventana_pbi = Toplevel(self.ventana_principal)
        ventana_pbi.title("Producto Bruto Interno (PBI)")
        ventana_pbi.geometry("400x400")
        
        Label(ventana_pbi, text="PBI = C + I + G + (X − M)", font=("Helvetica", 12)).pack(pady=10)
        Label(ventana_pbi, text="Descripción: Representa el valor total de bienes y servicios\nproducidos en un país durante un periodo específico.").pack(pady=10)
        
        Label(ventana_pbi, text="Ingrese Consumo (C):").pack()
        self.consumo = Entry(ventana_pbi)
        self.consumo.pack(pady=5)
        
        Label(ventana_pbi, text="Ingrese Inversión (I):").pack()
        self.inversion = Entry(ventana_pbi)
        self.inversion.pack(pady=5)
        
        Label(ventana_pbi, text="Ingrese Gasto del Gobierno (G):").pack()
        self.gasto_gobierno = Entry(ventana_pbi)
        self.gasto_gobierno.pack(pady=5)
        
        Label(ventana_pbi, text="Ingrese Exportaciones (X):").pack()
        self.exportaciones = Entry(ventana_pbi)
        self.exportaciones.pack(pady=5)
        
        Label(ventana_pbi, text="Ingrese Importaciones (M):").pack()
        self.importaciones = Entry(ventana_pbi)
        self.importaciones.pack(pady=5)
        
        Button(ventana_pbi, text="Calcular PBI", command=self.calcular_pbi, font=("Helvetica", 14), width=20, bg="#99ccff").pack(pady=10)
        Button(ventana_pbi, text="Volver", command=ventana_pbi.destroy, font=("Helvetica", 14), width=20, bg="#ff6666").pack(pady=10)

    def calcular_inflacion(self):
        try:
            ipc_actual = float(self.ipc_actual.get())
            ipc_anterior = float(self.ipc_anterior.get())
            inflacion = ((ipc_actual - ipc_anterior) / ipc_anterior) * 100
            messagebox.showinfo("Resultado", f"Tasa de Inflación: {inflacion:.2f}%")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos para IPC.")

    def calcular_pbi(self):
        try:
            c = float(self.consumo.get())
            i = float(self.inversion.get())
            g = float(self.gasto_gobierno.get())
            x = float(self.exportaciones.get())
            m = float(self.importaciones.get())
            pbi = c + i + g + (x - m)
            messagebox.showinfo("Resultado", f"PBI: {pbi:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos en todos los campos.")

# Crear ventana principal y ejecutar aplicación
ventana = Tk()
app = VentanaEconomica(ventana)
ventana.mainloop()
