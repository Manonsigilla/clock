"""
Horloge de Mamie Jeannine
Programme qui affiche l'heure avec alarme
"""

import time

# Variable globale pour stocker l'heure de l'alarme
alarme = None


def afficher_heure(heure_tuple):
    """
    Formate et retourne l'heure sous forme de chaîne de caractères.
    
    Paramètre: 
        heure_tuple: tuple (heures, minutes, secondes)
    
    Retourne:
        Chaîne formatée "hh:mm:ss"
    """
    heures = heure_tuple[0]
    minutes = heure_tuple[1]
    secondes = heure_tuple[2]
    
    heure_formatee = f"{heures:02d}:{minutes:02d}:{secondes:02d}"
    
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