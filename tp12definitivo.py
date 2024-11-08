
from tkinter import Tk, Label, PhotoImage, Button, messagebox, Frame, Toplevel, Entry, END, Listbox
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

        # Botón para abrir la ventana de átomos
        boton_atomos = Button(ventana, text="Átomos", command=self.abrir_ventana_atomos)
        boton_atomos.grid(row=4, pady=10)

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

    def abrir_ventana_atomos(self):
        # Crear una nueva ventana para los átomos
        ventana_atomos = Toplevel()
        ventana_atomos.title("Ventana de Átomos")
        ventana_atomos.geometry("400x300")

        # Crear un frame para los botones de átomos
        frame_atomos = Frame(ventana_atomos)
        frame_atomos.pack(pady=10)

        # Crear botones para átomos de ejemplo
        Button(frame_atomos, text="Hidrógeno", command=self.info_hidrogeno).grid(row=0, pady=5)
        Button(frame_atomos, text="Carbono", command=self.info_carbono).grid(row=1, pady=5)
        Button(frame_atomos, text="Oxígeno", command=self.info_oxigeno).grid(row=2, pady=5)
        Button(frame_atomos, text="Volver", command=ventana_atomos.destroy, bg="red").grid(row=3, pady=5)

    def info_hidrogeno(self):
        protons, electrons, neutrons, number = 1, 1, 0, 1
        messagebox.showinfo("Hidrógeno", f"Nombre: Hidrógeno\nProtones: {protons}\nElectrones: {electrons}\nNeutrones: {neutrons}\nNúmero de elemento: {number}")

    def info_carbono(self):
        protons, electrons, neutrons, number = 6, 6, 6, 6
        messagebox.showinfo("Carbono", f"Nombre: Carbono\nProtones: {protons}\nElectrones: {electrons}\nNeutrones: {neutrons}\nNúmero de elemento: {number}")

    def info_oxigeno(self):
        protons, electrons, neutrons, number = 8, 8, 8, 8
        messagebox.showinfo("Oxígeno", f"Nombre: Oxígeno\nProtones: {protons}\nElectrones: {electrons}\nNeutrones: {neutrons}\nNúmero de elemento: {number}")

    def mostrar_atomo(self):
        skibidi=[]

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
        atomos_seleccionados = rd.sample(atomos, 2)
        messagebox.showinfo("Enlace Covalente", f"Se han unido {atomos_seleccionados[0]} y {atomos_seleccionados[1]} para formar un enlace covalente.")

    def formar_enlace_ionico(self):
        atomos = ["Na", "Cl", "Mg", "O"]
        atomo1, atomo2 = rd.sample(atomos, 2)  # Seleccionar dos átomos aleatorios
        messagebox.showinfo("Enlace Iónico", f"{atomo1} ha transferido un electrón a {atomo2}. Se ha formado un enlace iónico.")

    def reaccion_intercambio(self):
        messagebox.showinfo("Reacción de Intercambio", "Los átomos han intercambiado elementos en la reacción química.")

    def mostrar_tabla_periodica(self):
        ventana_tabla = Toplevel()
        ventana_tabla.title("Ventana de Tabla Periodica")
        ventana_tabla.geometry("1000x800")

        # Crear un frame y empaquetarlo
        frame_t = Frame(ventana_tabla)
        frame_t.pack(pady=10)

        # Mensaje informativo
        messagebox.showinfo("Tabla Periódica", "Acá vas a ver una imagen de la tabla periódica IUPAC")

        # Cargar la imagen
        imagen2 = PhotoImage(file="fotillos/tablaperiodica.png")
        etiqueta_imagen = tk.Label(frame_t, image=imagen2)
        etiqueta_imagen.config(width=700, height=500)
        etiqueta_imagen.grid(row=2, pady=10)
          # Empaquetar la imagen dentro del frame

        # Mantener una referencia a la imagen para evitar que se descarte
        self.imagen2 = imagen2
        buton = Button(frame_t, text="Volver", command=ventana_tabla.destroy, bg="red")
        buton.grid(row=1, column=0, pady=10)

        # Mantener una referencia al botón

        self.buton=buton

class VentanaReaccionIntercambio:
    def __init__(self, ventana):
        # Crear una nueva ventana para la reacción de intercambio
        self.ventana_intercambio = Toplevel(ventana)
        self.ventana_intercambio.title("Reacción de Intercambio")
        self.ventana_intercambio.geometry("700x700")
        
        # Etiqueta para el título de la reacción
        Label(self.ventana_intercambio, text="Reacción de intercambio").pack(pady=10)
        
        # Crear una lista de átomos
        self.atom_list = [
            "1. Protactinio (Pa)",
            "2. Uranio (U)",
            "3. Neptunio (Np)",
            "4. Plutonio (Pu)",
            "5. Americio (Am)",
            "6. Curio (Cm)",
            "7. Berkelio (Bk)",
            "8. Californio (Cf)",
            "9. Einstenio (Es)"
        ]
        
        # Crear un Listbox para seleccionar los átomos
        self.lista_atomos = Listbox(self.ventana_intercambio, selectmode='multiple')
        for atomo in self.atom_list:
            self.lista_atomos.insert(END, atomo)
        self.lista_atomos.pack(pady=10)
        
        # Botón para realizar la reacción de intercambio
        Button(self.ventana_intercambio, text="Realizar reacción", command=self.realizar_reaccion).pack(pady=10)
        
        # Etiqueta para mostrar el resultado
        self.resultado = Label(self.ventana_intercambio, text="Resultado = ...")
        self.resultado.pack(pady=10)
        
        # Botón rojo para volver (cerrar la ventana)
        Button(self.ventana_intercambio, text="Volver", command=self.ventana_intercambio.destroy, bg="red").pack(pady=10)

    def realizar_reaccion(self):
        # Obtener los índices de los átomos seleccionados
        seleccionados = self.lista_atomos.curselection()
    
        if len(seleccionados) != 2:
            messagebox.showerror("Error", "Debe seleccionar exactamente dos átomos.")
            return
    
        # Identificar los átomos seleccionados
        atomo1 = self.atom_list[seleccionados[0]]
        atomo2 = self.atom_list[seleccionados[1]]
    
        # Realizar la reacción de intercambio específica
        if atomo1 == "1. Protactinio (Pa)" and atomo2 == "2. Uranio (U)":
            resultado_texto = "Resultado = Protactinio y Uranio forman un compuesto binario de actínidos."
        elif atomo1 == "1. Protactinio (Pa)" and atomo2 == "3. Neptunio (Np)":
            resultado_texto = "Resultado = Protactinio y Neptunio se usan en reactores nucleares experimentales."
        elif atomo1 == "2. Uranio (U)" and atomo2 == "4. Plutonio (Pu)":
            resultado_texto = "Resultado = Uranio y Plutonio son combinados en reactores nucleares para generar energía."
        elif atomo1 == "6. Curio (Cm)" and atomo2 == "9. Einstenio (Es)":
            resultado_texto = "Resultado = Curio y Einstenio pueden usarse en experimentos de síntesis de elementos transuránicos."
        elif atomo1 == "3. Neptunio (Np)" and atomo2 == "4. Plutonio (Pu)":
            resultado_texto = "Resultado = Neptunio y Plutonio pueden formar aleaciones útiles en aplicaciones nucleares."
        elif atomo1 == "5. Americio (Am)" and atomo2 == "6. Curio (Cm)":
            resultado_texto = "Resultado = Americio y Curio pueden reaccionar para formar óxidos mixtos."
        elif atomo1 == "7. Berkelio (Bk)" and atomo2 == "8. Californio (Cf)":
            resultado_texto = "Resultado = Berkelio y Californio se combinan en investigación de alta radioactividad."
        elif atomo1 == "9. Einstenio (Es)" and atomo2 == "5. Americio (Am)":
            resultado_texto = "Resultado = Einstenio y Americio pueden producir compuestos radiactivos únicos."
        else:
            resultado_texto = f"Resultado = Intercambio entre {atomo1} y {atomo2} en condiciones experimentales."
        # Mostrar el resultado en la etiqueta
        self.resultado.config(text=resultado_texto)

# Crear la ventana principal
ventana_quimica = tk.Tk()
ventana_quimica.title("App educativa de Química")
ventana_quimica.geometry("1000x800")
pagina = Aplicacion(ventana_quimica)

# Cambia a grid() para abrir la ventana de reacción
Button(ventana_quimica, text="Abrir Reacción de Intercambio", command=lambda: VentanaReaccionIntercambio(ventana_quimica)).grid(row=1, pady=20)

# Ejecutar la aplicación
ventana_quimica.mainloop()

