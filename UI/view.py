import flet as ft
from UI.alert import AlertManager


'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def clean(self):
        self.list_view.controls.clear()

    def load_interface(self):
        print(">>> load_interface è stata avviata!")
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---

        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

            # --- Sezione 2: Filtraggio ---
        self.generi=ft.Dropdown(label= "Genere",
                on_select=self.controller.leggi_genere,options=[],
                width=300
                )


            # Sezione 3: Libri
        self.biblioteche = ft.Dropdown(label="Biblioteca",options=[],
                on_select=self.controller.leggi_biblio,
                width=300
                )


        seleziona=ft.Button(content="seleziona", on_click=self.controller.seleziona)

        self.list_view = ft.ListView(expand=True, spacing=10)


            # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

            # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

                # Sezione 1
            self.txt_titolo,
            ft.Divider(),

                # Sezione 2: Filtraggio


            ft.Row(
                    [self.biblioteche,seleziona,self.generi],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ft.Divider(),
                # Nella View deve esserci esattamente questo:

                # Sezione 3: Libri
            self.list_view

            )

        self.page.scroll = "adaptive"
        self.controller.drop_biblio()
        self.controller.drop_genere()
        self.page.update()


    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"


        self.page.update()

        """ Cambia tema scuro/chiaro """

