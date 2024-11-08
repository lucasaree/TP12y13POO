from tkinter import Tk, Label, PhotoImage, Button, messagebox, Frame, Toplevel
import tkinter as tk
import random as rd

# Clase para la interfaz principal
class Aplicacion:
    def __init__(self, ventana):
        ventana.title("Interfaces gráficas con Tkinter POO")
        ventana.geometry("900x600")

        # Creo etiquetas
        etiqueta = tk.Label(ventana, text="Bienvenido a la pagina oficial")
        etiqueta.grid(row=0, pady=10)

        etiqueta2 = tk.Label(ventana, text="De la Divina Misericordia")
        etiqueta2.grid(row=1, pady=10)

        # Cargar la imagen
        imagen = PhotoImage(file="fotillos/divinaposta.png")  # Cambia por la ruta de tu imagen
        etiqueta_imagen = tk.Label(ventana, image=imagen)
        etiqueta_imagen.config(width=300, height=316)
        etiqueta_imagen.grid(row=2, pady=10)

        # Mantener una referencia a la imagen
        self.imagen = imagen

        # Botón para abrir la ventana con todos los botones
        boton_abrir_ventana_botones = Button(ventana, text="Abrir Ventana de Botones", command=self.abrir_ventana_botones)
        boton_abrir_ventana_botones.grid(row=3, pady=10)

    def abrir_ventana_botones(self):
        # Crear una nueva ventana
        ventana_botones = Toplevel()
        ventana_botones.title("Ventana de Botones")
        ventana_botones.geometry("600x400")

        # Crear un frame para los botones
        frame_botones = Frame(ventana_botones)
        frame_botones.pack(pady=10)

        # Crear botones en la nueva ventana
        Button(frame_botones, text="Mostrar Átomo", command=self.mostrar_atomo).grid(row=0, pady=5)
        Button(frame_botones, text="Calcular Número Másico", command=self.calcular_numero_masico).grid(row=1, pady=5)
        Button(frame_botones, text="Ingresar Elemento", command=self.ingresar_elemento).grid(row=2, pady=5)
        Button(frame_botones, text="Determinar configuración electrónica", command=self.determinar_configuracion).grid(row=3, pady=5)
        Button(frame_botones, text="Ionización del átomo", command=self.ionizacion_atomo).grid(row=4, pady=5)
        Button(frame_botones, text="Determinar electronegatividad", command=self.determinar_electronegatividad).grid(row=5, pady=5)
        Button(frame_botones, text="Formar un enlace covalente", command=self.formar_enlace_covalente).grid(row=6, pady=5)
        Button(frame_botones, text="Formar un enlace iónico", command=self.formar_enlace_ionico).grid(row=7, pady=5)
        Button(frame_botones, text="Realizar una reacción de intercambio", command=self.reaccion_intercambio).grid(row=8, pady=5)
        Button(frame_botones, text="Mostrar tabla Periódica", command=self.mostrar_tabla_periodica).grid(row=9, pady=5)
        Button(frame_botones, text="Volver", command=ventana_botones.destroy, bg="red").grid(row=10, pady=5)

    def mostrar_atomo(self):
        print("Mostrar Átomo: Aquí puedes agregar la lógica para mostrar un átomo.")

    def calcular_numero_masico(self):
        print("Calcular Número Másico: Aquí puedes agregar la lógica para calcular el número másico.")

    def ingresar_elemento(self):
        print("Ingresar Elemento: Aquí puedes agregar la lógica para ingresar un elemento.")

    def determinar_configuracion(self):
        capas = [2, 8, 18, 32]  # Capas electrónicas
        electrones = 18  # Ejemplo de electrones
        configuracion = []
        
        for capa in capas:
            if electrones > 0:
                if electrones >= capa:
                    configuracion.append(capa)
                    electrones -= capa
                else:
                    configuracion.append(electrones)
                    electrones = 0

        messagebox.showinfo("Configuración Electrónica", f"Configuración: {configuracion}")

    def ionizacion_atomo(self):
        electrones = rd.randint(1, 10)  # Número aleatorio de electrones
        accion = "remover" if rd.choice([True, False]) else "agregar"
        if accion == "agregar":
            electrones += 1
            messagebox.showinfo("Ionización", f"Se ha agregado un electrón. Nuevos electrones: {electrones}")
        else:
            electrones = max(0, electrones - 1)  # Asegurarse de que no sea negativo
            messagebox.showinfo("Ionización", f"Se ha removido un electrón. Nuevos electrones: {electrones}")

    def determinar_electronegatividad(self):
        electronegatividad = rd.uniform(0.7, 4.0)  # Valor aleatorio de electronegatividad
        messagebox.showinfo("Electronegatividad", f"La electronegatividad del átomo es: {electronegatividad:.2f}")

    def formar_enlace_covalente(self):
        atomos = ["H", "O", "C", "N"]
        atomos_seleccionados = rd.sample(atomos, 2)  # Seleccionar dos átomos aleatorios
        messagebox.showinfo("Enlace Covalente", f"Se han unido {atamos_seleccionados[0]} y {atamos_seleccionados[1]} para formar un enlace covalente.")

    def formar_enlace_ionico(self):
        atomos = ["Na", "Cl", "Mg", "O"]
        atomo1, atomo2 = rd.sample(atomos, 2)  # Seleccionar dos átomos aleatorios
        messagebox.showinfo("Enlace Iónico", f"{atomo1} ha transferido un electrón a {atomo2}. Se ha formado un enlace iónico.")

    def reaccion_intercambio(self):
        messagebox.showinfo("Reacción de Intercambio", "Los átomos han intercambiado elementos en la reacción química.")

    def mostrar_tabla_periodica(self):
        messagebox.showinfo("Tabla Periódica", "Aquí podrías mostrar la tabla periódica.")
    
class Ejercicio2:    
    def __init__(self, ventana):
        ventana.title("Interfaces gráficas con Tkinter POO")
        ventana.geometry("900x600")

        # Creo etiquetas
        etiqueta = tk.Label(ventana, text="Bienvenido a la pagina oficial")
        etiqueta.grid(row=0, pady=10)

        etiqueta2 = tk.Label(ventana, text="De la Divina Misericordia")
        etiqueta2.grid(row=1, pady=10)

        # Cargar la imagen
        imagen = PhotoImage(file="fotillos/divinaposta.png")  # Cambia por la ruta de tu imagen
        etiqueta_imagen = tk.Label(ventana, image=imagen)
        etiqueta_imagen.config(width=300, height=316)
        etiqueta_imagen.grid(row=2, pady=10)

        # Mantener una referencia a la imagen
        self.imagen = imagen

        # Botón para abrir la ventana con todos los botones
        boton_abrir_ventana_botones = Button(ventana, text="Abrir Ventana de Botones", command=self.abrir_ventana_botones)
        boton_abrir_ventana_botones.grid(row=3, pady=10)

    def abrir_ventana_botones(self):
        # Crear una nueva ventana
        ventana_botones = Toplevel()
        ventana_botones.title("Ventana de Botones")
        ventana_botones.geometry("600x400")

        # Crear un frame para los botones
        frame_botones = Frame(ventana_botones)
        frame_botones.pack(pady=10)

        # Crear botones en la nueva ventana
        Button(frame_botones, text="Mostrar Átomo", command=self.mostrar_atomo).grid(row=0, pady=5)
        Button(frame_botones, text="Calcular Número Másico", command=self.calcular_numero_masico).grid(row=1, pady=5)
        Button(frame_botones, text="Ingresar Elemento", command=self.ingresar_elemento).grid(row=2, pady=5)
        Button(frame_botones, text="Determinar configuración electrónica", command=self.determinar_configuracion).grid(row=3, pady=5)
        Button(frame_botones, text="Ionización del átomo", command=self.ionizacion_atomo).grid(row=4, pady=5)
        Button(frame_botones, text="Determinar electronegatividad", command=self.determinar_electronegatividad).grid(row=5, pady=5)
        Button(frame_botones, text="Formar un enlace covalente", command=self.formar_enlace_covalente).grid(row=6, pady=5)
        Button(frame_botones, text="Formar un enlace iónico", command=self.formar_enlace_ionico).grid(row=7, pady=5)
        Button(frame_botones, text="Realizar una reacción de intercambio", command=self.reaccion_intercambio).grid(row=8, pady=5)
        Button(frame_botones, text="Mostrar tabla Periódica", command=self.mostrar_tabla_periodica).grid(row=9, pady=5)
        Button(frame_botones, text="Volver", command=ventana_botones.destroy, bg="red").grid(row=10, pady=5)

    def mostrar_atomo(self):
        print("Mostrar Átomo: Aquí puedes agregar la lógica para mostrar un átomo.")

    def calcular_numero_masico(self):
        print("Calcular Número Másico: Aquí puedes agregar la lógica para calcular el número másico.")

    def ingresar_elemento(self):
        print("Ingresar Elemento: Aquí puedes agregar la lógica para ingresar un elemento.")

    def determinar_configuracion(self):
        capas = [2, 8, 18, 32]  # Capas electrónicas
        electrones = 18  # Ejemplo de electrones
        configuracion = []
        
        for capa in capas:
            if electrones > 0:
                if electrones >= capa:
                    configuracion.append(capa)
                    electrones -= capa
                else:
                    configuracion.append(electrones)
                    electrones = 0

        messagebox.showinfo("Configuración Electrónica", f"Configuración: {configuracion}")

    def ionizacion_atomo(self):
        electrones = rd.randint(1, 10)  # Número aleatorio de electrones
        accion = "remover" if rd.choice([True, False]) else "agregar"
        if accion == "agregar":
            electrones += 1
            messagebox.showinfo("Ionización", f"Se ha agregado un electrón. Nuevos electrones: {electrones}")
        else:
            electrones = max(0, electrones - 1)  # Asegurarse de que no sea negativo
            messagebox.showinfo("Ionización", f"Se ha removido un electrón. Nuevos electrones: {electrones}")

    def determinar_electronegatividad(self):
        electronegatividad = rd.uniform(0.7, 4.0)  # Valor aleatorio de electronegatividad
        messagebox.showinfo("Electronegatividad", f"La electronegatividad del átomo es: {electronegatividad:.2f}")

    def formar_enlace_covalente(self):
        atomos = ["H", "O", "C", "N"]
        atomos_seleccionados = rd.sample(atomos, 2)  # Seleccionar dos átomos aleatorios
        messagebox.showinfo("Enlace Covalente", f"Se han unido {atamos_seleccionados[0]} y {atamos_seleccionados[1]} para formar un enlace covalente.")

    def formar_enlace_ionico(self):
        atomos = ["Na", "Cl", "Mg", "O"]
        atomo1, atomo2 = rd.sample(atomos, 2)  # Seleccionar dos átomos aleatorios
        messagebox.showinfo("Enlace Iónico", f"{atomo1} ha transferido un electrón a {atomo2}. Se ha formado un enlace iónico.")

    def reaccion_intercambio(self):
        messagebox.showinfo("Reacción de Intercambio", "Los átomos han intercambiado elementos en la reacción química.")

    def mostrar_tabla_periodica(self):
        messagebox.showinfo("Tabla Periódica", "Aquí podrías mostrar la tabla periódica.")


ventana_quimica = tk.Tk()
ventana_quimica.title("App educativa de Química")
ventana_quimica.geometry("1000x800")
pagina = Aplicacion(ventana_quimica)
pagina = Ejercicio2(ventana_quimica)

# Ejecutar la aplicación
ventana_quimica.mainloop()
