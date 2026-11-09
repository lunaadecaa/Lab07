
from database.DB_connect import DBConnect
from model.libro_DTO import Libro
"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass


    def get_genere(self):
        result=[]
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor()
        query="SELECT DISTINCT `genere` FROM libro"
        if cnx is None:
            cursor.close()
            cnx.close()
            return result
        try:
            cursor.execute(query)
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()
            return result
        except:
            print("Errore nel prendere i dati")
            cursor.close()
            cnx.close()
            return None

    def get_libri(self,genere,biblio):
        cnx = DBConnect.get_connection()

        cursore = cnx.cursor()#non uso dictionary perche ho indici come chciavi


        query = "SELECT `id`, `titolo` ,`autore`, `genere`, `anno_pubblicazione`, `id_biblioteca` FROM libro WHERE id_biblioteca = COALESCE(%s, id_biblioteca) AND genere = COALESCE(%s, genere)"

        cursore.execute(query, (biblio, genere))

        libri_filtrati = []
        for x in cursore:
            libro = Libro(x[0], x[1], x[2], x[3], x[4], x[5])
            libri_filtrati.append(libro)

        cursore.close()
        cnx.close()

        return libri_filtrati
