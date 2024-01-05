
def hashing(a):
    counter = 0
    hashing = []
    value = []
    index = 0
    for i in range(len(a)):
        hashing.append(a[counter])
        counter += 1
    counter = 0
    for n in range(len(a)):
        value.append(ord(hashing[counter]))
        counter += 1
    counter = 0
    index = sum(value) / len(a)
    return(int(index))
    
#a function to search a word in the table and return the content
def read(a):
    a = a 


#FunctionToCreateTheArray(NameOfTheArray(string), nb_col(int), nb_row(int),LenghtOfTheRow(int))
#FunctionToAddAnElement(NameOfTheArray(string), NumOfTheCol(int), NumOfTheRow(int),ElementToAdd)


class EmptyCell:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        if self.value is None:
            return "#"
        else:
            return str(self.value)

def CreateArray(n, name, nb_line):
    tableau = {name: []}  # Initialise la liste principale avec un nom donné
    for _ in range(n):
        nouvelle_liste = [EmptyCell() for _ in range(nb_line)]  # Crée une liste avec des objets EmptyCell
        tableau[name].append(nouvelle_liste)  # Ajoute la nouvelle liste à 'tableau'
    return tableau

def ajout(element, indice_liste, indice_objet, tableau_name, tableau):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            if indice_objet < len(tableau[tableau_name][indice_liste]):
                tableau[tableau_name][indice_liste][indice_objet].value = element
                print(f"L'élément '{element}' a été ajouté à la case {indice_objet} de la liste {indice_liste} de '{tableau_name}'.")
            else:
                print(f"L'indice d'objet spécifié est hors de la plage de '{tableau_name}[{indice_liste}]'.")
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")

def del_cells(indice_liste, indice_objet, tableau_name, tableau):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            if indice_objet < len(tableau[tableau_name][indice_liste]):
                tableau[tableau_name][indice_liste][indice_objet].value = None
                print(f"La case {indice_objet} de la liste {indice_liste} de '{tableau_name}' a été vidée.")
            else:
                print(f"L'indice d'objet spécifié est hors de la plage de '{tableau_name}[{indice_liste}]'.")
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")

def del_row(indice_liste, tableau_name, tableau):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            for cellule in tableau[tableau_name][indice_liste]:
                cellule.value = None
            print(f"La liste {indice_liste} de '{tableau_name}' a été vidée.")
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")

def get_row(indice_liste, tableau_name, tableau, exclude_empty=False):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            if exclude_empty:
                return [cellule.value for cellule in tableau[tableau_name][indice_liste] if cellule.value is not None]
            else:
                return [cellule.value for cellule in tableau[tableau_name][indice_liste]]
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
            return []
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")
        return []

def get_coll(tableau_name, n, tableau):
    if tableau_name in tableau:
        return [liste[n].value for liste in tableau[tableau_name] if n < len(liste)]
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")
        return []

def get_cells(tableau_name, indice_liste, indice_objet, tableau):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            if indice_objet < len(tableau[tableau_name][indice_liste]):
                return tableau[tableau_name][indice_liste][indice_objet].value
            else:
                print(f"L'indice d'objet spécifié est hors de la plage de '{tableau_name}[{indice_liste}]'.")
                return None
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
            return None
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")
        return None

# Fonction pour afficher le tableau avec un espacement égal pour tous les éléments
def afficher_tableau(tableau):
    max_length = 0  # Longueur maximale des éléments dans le tableau
    for key, value in tableau.items():
        for liste in value:
            for cellule in liste:
                cellule_length = len(str(cellule))
                if cellule_length > max_length:
                    max_length = cellule_length

    for key, value in tableau.items():
        print(f"{key}:")
        for liste in value:
            for cellule in liste:
                cellule_str = str(cellule)
                espacement = " " * ((max_length - len(cellule_str)) // 2)
                print(f"{espacement}{cellule_str}{espacement}", end=" ")
            print()
        print()
