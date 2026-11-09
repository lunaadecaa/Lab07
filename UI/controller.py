
import flet as ft
from UI.view import View
from model.model import Model



'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view:View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None



    """def drop_biblio(self):
        d = self._model.get_biblioteche()
        print(f"Biblioteche trovate dal model: {d}")  # <-- AGGIUNGI QUESTO
        b = self._view.biblioteche
        b.options.clear()
        b.options.append(ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro"))
        for x in d:
            b.options.append(ft.DropdownOption(key=str(x.id), text= str(x.nome)))
        self._view.update()

    def drop_genere(self):
        generi = self._model.get_generi()
        print(f"Generi trovati dal model: {generi}")  # <-- AGGIUNGI QUESTO
        gen = self._view.generi
        gen.options.clear()
        gen.options.append(ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro"))
        for g in generi:
            gen.options.append(ft.DropdownOption(key=str(g), text=str(g)))

        self._view.update()
   """

    def drop_biblio(self):
        print(">>> SONO DENTRO drop_biblio")
        try:
            d = self._model.get_biblioteche()
            print(f"Biblioteche lette: {d}")
            b = self._view.biblioteche
            b.options.clear()
            b.options.append(ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro"))
            for x in d:
                b.options.append(ft.dropdown.Option(key=str(x.id), text=str(x.nome)))
            self._view.update()
        except Exception as e:
            print(f"ERRORE in drop_biblio: {e}")

    def drop_genere(self):
        print(">>> SONO DENTRO drop_genere")
        try:
            generi = self._model.get_generi()
            print(f"Generi letti: {generi}")
            gen = self._view.generi
            gen.options.clear()
            gen.options.append(ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro"))
            for g in generi:
                if g is not None:
                    gen.options.append(ft.dropdown.Option(key=str(g), text=str(g)))
            self._view.update()
        except Exception as e:
            print(f"ERRORE in drop_genere: {e}")


    def leggi_biblio(self,e):
        self.biblioteca_selezionata=e.control.value
        return self.biblioteca_selezionata

    def leggi_genere(self,e):
        self.genere_selezionato=e.control.value
        return self.genere_selezionato

    """def seleziona_bnt(self,e):
        print("button clicked")
        genere_scelto = self._view.generi.value
        biblioteca_scelta = self._view.biblioteche.value


        result = self._model.get_libri_filtrati(genere_scelto, biblioteca_scelta)
        self._view.list_view.controls.clear()
        self._view.list_view.controls.append(ft.Text(f"{len(result)}"))
        for libro in result:
            self._view.list_view.controls.append(ft.Text(f"{libro}"))
        self._view.update()

    # AZIONE: MOSTRA LIBRI
    def seleziona(self,e):
        genere_scelto=self._view.generi.value
        biblioteca_scelta=self._view.biblioteca_selezionata.value

        result=self._model.get_libri_filtrati(genere_scelto,biblioteca_scelta)
        return result"""

    def seleziona(self,e):
        print(f"VALORE SELEZIONATO BIBLIOTECA -> {self.biblioteca_selezionata} (tipo: {type(self.biblioteca_selezionata)})")
        print(f"VALORE SELEZIONATO GENERE -> {self.genere_selezionato} (tipo: {type(self.genere_selezionato)})")
        self._view.list_view.controls.clear()

        if self.biblioteca_selezionata == "Nessun filtro":
            self.biblioteca_selezionata = None

        if self.genere_selezionato == "Nessun filtro":
            self.genere_selezionato = None

        libri_filtrati = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        if len(libri_filtrati) == 0:
            self._view.show_alert("Non è stato trovato alcun libro corrispondente ai filtri applicati")

        else:
            listview = self._view.list_view
            for libro in libri_filtrati:
                testo_libro = ft.Text(str(libro))
                listview.controls.append(testo_libro)

        self._view.update()
