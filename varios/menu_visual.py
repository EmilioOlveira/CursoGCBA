import customtkinter as ctk
from PIL import Image
import os

# Configuración del estilo general (Tema oscuro/claro y paleta de colores)
ctk.set_appearance_mode("System")  # Toma el modo del sistema operativo (Light/Dark)
ctk.set_default_color_theme("blue")

class AppMenu(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.title("Interfaz con Menú e Íconos")
        self.geometry("700x450")

        # --- CARGAR ÍCONOS ---
        # Usamos PIL para abrir la imagen y CTkImage para que escale bien en pantallas de alta resolución
        ruta_actual = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
        
        icon_home_image = Image.open(os.path.join(ruta_actual, "home_icon.png"))
        icon_settings_image = Image.open(os.path.join(ruta_actual, "settings_icon.png"))

        self.home_icon = ctk.CTkImage(light_image=icon_home_image, dark_image=icon_home_image, size=(20, 20))
        self.settings_icon = ctk.CTkImage(light_image=icon_settings_image, dark_image=icon_settings_image, size=(20, 20))

        # --- ESTRUCTURA: MENÚ LATERAL ---
        # Creamos un contenedor (Frame) a la izquierda para el menú
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.pack(side="left", fill="y")

        # Título del menú
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Mi Aplicación", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(padx=20, pady=(20, 40))

        # Botón 1: Inicio (Con ícono)
        self.btn_home = ctk.CTkButton(
            self.sidebar_frame, 
            text=" Inicio",          # Espacio al principio para separar del ícono
            image=self.home_icon,    # Asignamos el ícono creado antes
            compound="left",         # Posiciona el ícono a la izquierda del texto
            anchor="w",              # Alinea el contenido al oeste (izquierda)
            command=self.accion_inicio
        )
        self.btn_home.pack(padx=20, pady=10, fill="x")

        # Botón 2: Configuración (Con ícono)
        self.btn_settings = ctk.CTkButton(
            self.sidebar_frame, 
            text=" Configuración", 
            image=self.settings_icon, 
            compound="left", 
            anchor="w", 
            command=self.accion_config
        )
        self.btn_settings.pack(padx=20, pady=10, fill="x")

        # --- ÁREA DE CONTENIDO PRINCIPAL ---
        # El panel de la derecha donde cambiarán las cosas al tocar el menú
        self.content_frame = ctk.CTkFrame(self, corner_radius=10)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.label_contenido = ctk.CTkLabel(self.content_frame, text="Bienvenido. Seleccioná una opción.", font=("Arial", 16))
        self.label_contenido.pack(expand=True)

    # Métodos que se ejecutan al hacer clic en los botones del menú
    def accion_inicio(self):
        self.label_contenido.configure(text="Estás en la pantalla de Inicio 🏠")

    def accion_config(self):
        self.label_contenido.configure(text="Estás en la pantalla de Configuración ⚙️")

if __name__ == "__main__":
    app = AppMenu()
    app.mainloop()