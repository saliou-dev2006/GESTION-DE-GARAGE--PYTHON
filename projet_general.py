def enregistrement(x, voiture):
    voiture['marque'] = input("donner la marque de la vehicule:")
    voiture['modele'] = input("donner le modele de la vehicule:")
    voiture['couleur'] = input("donner la couleur de la vehicule:")
    voiture['plaque'] = input("donner la plaque du vehicule:")
    voiture['prix'] = int(input("donner le prix du vehicule:"))
    with open('garage.txt', 'a') as f:
        f.write(f"marque:{voiture['marque']} modele:{voiture['modele']} couleur:{voiture['couleur']} plaque:{voiture['plaque']} prix:{voiture['prix']}\n")
    x.append(voiture)


def vendre(x, voiture, a, b, c):
    x.clear()
    try:
        with open('garage.txt', 'r') as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne:
                    continue
                voiture = {}
                parties = ligne.split(' ')
                for partie in parties:
                    if ':' in partie:
                        cle, valeur = partie.split(':', 1)
                        voiture[cle] = valeur
                if 'marque' in voiture:
                    x.append(voiture)
    except FileNotFoundError:
        pass
    marque = input("donner la marque du vehicule que vous souhaitez vendre:")
    couleur = input("donner sa couleur:")
    trouve = False
    for voiture in x:
        if (marque == voiture['marque'] and couleur == voiture['couleur']):
            print(f"MARQUE:{voiture['marque']}")
            print(f"MODELE:{voiture['modele']}")
            print(f"COULEUR:{voiture['couleur']}")
            print(f"PLAQUE:{voiture['plaque']}")
            print(f"PRIX:{voiture['prix']}GNF")
            a['marque'] = voiture['marque']
            a['modele'] = voiture['modele']
            a['couleur'] = voiture['couleur']
            a['plaque'] = voiture['plaque']
            a['prix'] = voiture['prix']
            b += [voiture['prix']]
            c.append(dict(a))
            x.remove(voiture)
            trouve = True
            # sauvegarder la vente dans le fichier des ventes
            with open('rapport_ventes.txt', 'a') as f:
                f.write(f"marque:{a['marque']} modele:{a['modele']} couleur:{a['couleur']} plaque:{a['plaque']} prix:{a['prix']}\n")
            break
    if not trouve:
        print("DESOLE NOUS N'AVONS PAS UNE VOITURE DE")
        print(f"MARQUE:{marque}")
        print(f"COULEUR:{couleur}")
    with open('garage.txt', 'w') as f:
        for voiture in x:
            f.write(f"marque:{voiture['marque']} modele:{voiture['modele']} couleur:{voiture['couleur']} plaque:{voiture['plaque']} prix:{voiture['prix']}\n")


def caractristique(x, voiture):
    x.clear()
    try:
        with open('garage.txt', 'r') as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne:
                    continue
                voiture = {}
                parties = ligne.split(' ')
                for partie in parties:
                    if ':' in partie:
                        cle, valeur = partie.split(':', 1)
                        voiture[cle] = valeur
                if 'marque' in voiture:
                    x.append(voiture)
    except FileNotFoundError:
        pass
    carac = input(" vous voulez les caracteristique de quelle marque de vehicule:")
    for voiture in x:
        if (voiture['marque'] == carac):
            print("_______________________________________________________________________")
            print(f"MARQUE:{voiture['marque']}")
            print(f"MODELE:{voiture['modele']}")
            print(f"COULEUR:{voiture['couleur']}")
            print(f"PLAQUE:{voiture['plaque']}")
            print(f"PRIX:{voiture['prix']}GNF")
            print("_________________________________________________________________________")


def liste_des_voiture_garage(x, voiture):
    x.clear()
    try:
        with open('garage.txt', 'r') as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne:
                    continue
                voiture = {}
                parties = ligne.split(' ')
                for partie in parties:
                    if ':' in partie:
                        cle, valeur = partie.split(':', 1)
                        voiture[cle] = valeur
                if 'marque' in voiture:
                    x.append(voiture)
    except FileNotFoundError:
        pass
    for voiture in x:
        print("_________________________________________________________________________________")
        print(f"MARQUE:{voiture['marque']}")
        print(f"MODELE:{voiture['modele']}")
        print(f"COULEUR:{voiture['couleur']}")
        print(f"PLAQUE:{voiture['plaque']}")
        print(f"PRIX:{voiture['prix']}GNF")
        print("___________________________________________________________________________________")


def raport_des_voiture_vendu(a, b, c):
    c.clear()
    b.clear()
    try:
        with open('rapport_ventes.txt', 'r') as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne:
                    continue
                a = {}
                parties = ligne.split(' ')
                for partie in parties:
                    if ':' in partie:
                        cle, valeur = partie.split(':', 1)
                        a[cle] = valeur
                if 'marque' in a:
                    c.append(dict(a))
                    b += [a['prix']]
    except FileNotFoundError:
        pass
    print('les voiture vendus sont les suivante:')
    for a in c:
        print("_________________________________________________________________________________")
        print(f"MARQUE:{a['marque']}")
        print(f"MODELE:{a['modele']}")
        print(f"COULEUR:{a['couleur']}")
        print(f"PLAQUE:{a['plaque']}")
        print(f"PRIX:{a['prix']}GNF")
        print("___________________________________________________________________________________")
    if b:
        print(f'la somme totale encaisée est: {sum(int(v) for v in b)}GNF')
    else:
        print("aucune vente effectuee")


def menu():
    print("___________________________________________gestion des vitures d'occasions__________________________________________________")
    garase = []
    total = {}
    voiture_vendu = []
    somme = []
    choix = ''
    while (choix != '0'):
        print("1--> pour enregistre une voiture:")
        print("2--> pour vendre une voiture:")
        print("3--> pour afficher les caracteristiques d'une voiture:")
        print("4--> pour afficher la liste totale des voiture du garage:")
        print("5--> pour afficher le tatal des voiture vendu ainsi que la somme encaissée:")
        print("0--> pour quitter le programme:")
        choix = input("Choix--> ")
        vehivule = {}
        if (choix == '1'):
            enregistrement(garase, vehivule)
        elif (choix == '2'):
            vendre(garase, vehivule, total, somme, voiture_vendu)
        elif (choix == '3'):
            caractristique(garase, vehivule)
        elif (choix == '4'):
            liste_des_voiture_garage(garase, vehivule)
        elif (choix == '5'):
            raport_des_voiture_vendu(total, somme, voiture_vendu)


#  MON PROGRAMME PRINCIPALE
menu()