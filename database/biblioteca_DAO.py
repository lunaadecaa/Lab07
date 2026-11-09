

from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):

        pass

    def get_biblioteca(self):
        result=[]
        cnx=DBConnect.get_connection()
        if cnx is None:
            return result

        #faccio dictyionary perche uso nomi come chiavi
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT `id`, `nome`, `indirizzo` FROM biblioteca"

        try:
            cursor.execute(query)
            for row in cursor:

                biblioteca = Biblioteca(
                    id=row["id"],
                    nome=row["nome"],
                    indirizzo=row["indirizzo"]
                )
                result.append(biblioteca)
            cursor.close()
            cnx.close()

            return result
        except Exception as e :
            print(f"ERRORE SQL DETTAGLIATO: {e}")

