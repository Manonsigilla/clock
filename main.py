import time

# Variable globale pour stocker l'heure de l'alarme
alarme = None

mode_24h = True


def afficher_heure(heure_tuple):
    """
    Formate et retourne l'heure sous forme de chaîne de caractères.
    
    Paramètre: 
        heure_tuple: tuple (heures, minutes, secondes)
    """
    
    global mode_24h
    
    heures = heure_tuple[0]
    minutes = heure_tuple[1]
    secondes = heure_tuple[2]
    
    if mode_24h:
        # Mode 24 heures classique
        heure_formatee = f"{heures:02d}:{minutes:02d}:{secondes:02d}"
    else:
        # Mode 12 heures avec AM/PM
        if heures == 0:
            heures_12h = 12
            periode = "AM"
        elif heures < 12:
            heures_12h = heures
            periode = "AM"
        elif heures == 12:
            heures_12h = 12
            periode = "PM"
        else:
            heures_12h = heures - 12
            periode = "PM"
        
        heure_formatee = f"{heures_12h:02d}:{minutes:02d}:{secondes:02d} {periode}"
    
    return heure_formatee


def regler_heure():
    """
    Permet à l'utilisateur de régler l'heure de démarrage de l'horloge.
    
    Retourne: 
        tuple (heures, minutes, secondes) ou None si erreur
    """
    print("\n--- RÉGLAGE DE L'HEURE ---")
    
    try:
        heures = int(input("Entrez les heures (0-23) : "))
        minutes = int(input("Entrez les minutes (0-59) : "))
        secondes = int(input("Entrez les secondes (0-59) : "))
        
        if 0 <= heures <= 23 and 0 <= minutes <= 59 and 0 <= secondes <= 59:
            heure_reglee = (heures, minutes, secondes)
            print(f"Heure réglée sur {afficher_heure(heure_reglee)}")
            return heure_reglee
        else: 
            print("Erreur : valeurs hors limites !")
            return None
    except ValueError:
        print("Erreur : veuillez entrer des nombres entiers !")
        return None


def choisir_mode_affichage():
    
    global mode_24h
    
    print("\n--- MODE D'AFFICHAGE ---")
    print("1. Mode 24 heures (ex: 16:30:00)")
    print("2. Mode 12 heures (ex: 04:30:00 PM)")
    
    try:
        choix = int(input("Choisissez le mode (1 ou 2) : "))
        if choix == 1:
            mode_24h = True
            print("✓ Mode 24 heures sélectionné")
        elif choix == 2:
            mode_24h = False
            print("✓ Mode 12 heures sélectionné")
        else:
            print("Choix invalide. Mode 24 heures par défaut.")
            mode_24h = True
    except ValueError:
        print("Erreur : veuillez entrer 1 ou 2. Mode 24 heures par défaut.")
        mode_24h = True


def regler_alarme():
    """
    Demande à l'utilisateur l'heure de l'alarme et la stocke.
    """
    global alarme
    
    print("\n--- RÉGLAGE DE L'ALARME ---")
    
    try:
        heures = int(input("Entrez les heures (0-23) : "))
        minutes = int(input("Entrez les minutes (0-59) : "))
        secondes = int(input("Entrez les secondes (0-59) : "))
        
        if 0 <= heures <= 23 and 0 <= minutes <= 59 and 0 <= secondes <= 59:
            alarme = (heures, minutes, secondes)
            print(f"Alarme réglée pour {afficher_heure(alarme)}")
        else:
            print("Erreur : valeurs hors limites !")
    except ValueError:
        print("Erreur : veuillez entrer des nombres entiers !")


def verifier_alarme(heure_actuelle):
    """
    Compare l'heure actuelle avec l'heure de l'alarme.
    """
    global alarme
    
    if alarme is not None and heure_actuelle == alarme:
        print("\n\nDRIIIIING ! RÉVEIL MAMIE JEANNINE !\n")
        alarme = None


def horloge_principale(heure_depart=None):
    """
    Retourne l'heure actuelle pour permettre la relance
    
    Retourne:
        tuple (heures, minutes, secondes) - l'heure au moment de l'arrêt
    Fonction principale de l'horloge.
    Affiche l'heure et l'actualise chaque seconde.
    """
    # Initialisation de l'heure
    if heure_depart is not None:
        heures = heure_depart[0]
        minutes = heure_depart[1]
        secondes = heure_depart[2]
    else:
        now = time.localtime()
        heures = now.tm_hour
        minutes = now.tm_min
        secondes = now.tm_sec
    
    print("\nHorloge démarrée ! Appuyez sur Ctrl+C pour arrêter")
    print("-" * 40)
    
    # Boucle principale de l'horloge
    try:
        while True:
            heure_actuelle = (heures, minutes, secondes)
            
            print(f"\r{afficher_heure(heure_actuelle)}", end="", flush=True)
            
            verifier_alarme(heure_actuelle)
            
            time.sleep(1)
            
            secondes = secondes + 1
            
            if secondes >= 60:
                secondes = 0
                minutes = minutes + 1
            
            if minutes >= 60:
                minutes = 0
                heures = heures + 1
            
            if heures >= 24:
                heures = 0
    
    except KeyboardInterrupt:
        # Au lieu d'arrêter définitivement, on retourne l'heure
        print("\n\nHorloge mise en pause.")
        return (heures, minutes, secondes)


# PROGRAMME PRINCIPAL
if __name__ == "__main__":
    print("=" * 50)
    print("   HORLOGE DE MAMIE JEANNINE")
    print("=" * 50)
    
    heure_personnalisee = None
    
    choisir_mode_affichage()
    
    # Régler l'heure manuellement
    choix_heure = input("\nVoulez-vous régler l'heure manuellement ? (o/n) : ")
    if choix_heure.lower() == "o":
        heure_personnalisee = regler_heure()
    
    # Régler une alarme
    choix_alarme = input("\nVoulez-vous régler une alarme ? (o/n) : ")
    if choix_alarme.lower() == "o":
        regler_alarme()
    
    # Boucle permettant de relancer l'horloge après Ctrl+C
    while True:
        # Lancer l'horloge et récupérer l'heure au moment de l'arrêt
        heure_actuelle = horloge_principale(heure_personnalisee)
        
        # Si l'horloge a été interrompue (Ctrl+C)
        if heure_actuelle is not None:
            # Afficher l'heure actuelle et proposer de relancer
            choix_relance = input(
                f"\nHeure actuelle : {afficher_heure(heure_actuelle)}"
                f"\nVoulez-vous relancer l'horloge ? (o/n) : "
            )
            
            if choix_relance.lower() == "o":
                # Relancer avec l'heure actuelle (reprend où on s'était arrêté)
                heure_personnalisee = heure_actuelle
            else:
                # Quitter définitivement
                print("\nÀ bientôt Mamie Jeannine !")
                break
        else:
            # L'horloge s'est arrêtée normalement (cas peu probable)
            break