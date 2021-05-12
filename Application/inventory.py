import crud


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    isNumber = True
    print_hi('Bienvenue sur notre application')
    print_hi("1 - Lister toutes les postes.")
    print_hi("2 - Chercher un poste en particulier(host).")
    print_hi("3 - Supprimer un  poste(host).")
    print_hi("4 - Creer un  poste.")
    print_hi("5 - Modifier un  poste.")
    while isNumber:
        choice_user = input("Choisissez entre les différentes options: ")
        try:
            choice_user = int(choice_user)
            isNumber = False
        except:
            print("La valeur saisie n'est pas un nombre")
    if choice_user == 1:
        crud.printAllData(crud.get_postes())
    elif choice_user == 2:
        host = input("Veuillez saisir le host d'une poste: ")
        data = crud.get_poste(host)
        crud.printData(data)
    elif choice_user == 3:
        host = input("Veuillez saisir le host d'une poste: ")
        crud.delete_poste(host)
    elif choice_user == 4:
        crud.create_poste()
    elif choice_user == 5:
        host = input("Veuillez saisir le host du poste à modifier: ")
        crud.update_poste(host)
    else:
        print("Choix inconnu...")
