"""
Horloge de Mamie Jeannine
Programme qui affiche l'heure et permet de la régler manuellement.
"""

import time


def afficher_heure(heure_tuple):
    """
    Formate et retourne l'heure sous forme de chaîne de caractères. 
    
    Paramètre: 
        heure_tuple:  tuple (heures, minutes, secondes)
    
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
        
        # Vérification que les valeurs sont dans les plages valides
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

def horloge_principale(heure_depart=None):
    """
    Fonction principale de l'horloge.
    Affiche l'heure et l'actualise chaque seconde. 
    
    Paramètre:
        heure_depart: tuple (heures, minutes, secondes) optionnel
        Si None, utilise l'heure système
    """
    # Initialisation de l'heure
    if heure_depart is not None:
        # Utiliser l'heure fournie par l'utilisateur
        heures = heure_depart[0]
        minutes = heure_depart[1]
        secondes = heure_depart[2]
    else:
        # Utiliser l'heure système
        now = time.localtime()
        heures = now.tm_hour
        minutes = now.tm_min
        secondes = now.tm_sec
    
    print("\nHorloge démarrée !  Appuyez sur Ctrl+C pour arrêter")
    print("-" * 40)
    
    # Boucle principale de l'horloge
    try:
        while True:
            # Créer le tuple de l'heure actuelle
            heure_actuelle = (heures, minutes, secondes)
            
            # Afficher l'heure
            # \r ramène le curseur au début de la ligne
            # end="" empêche le saut de ligne
            # flush=True force l'affichage immédiat
            print(f"\r{afficher_heure(heure_actuelle)}", end="", flush=True)
            
            # Attendre 1 seconde
            time.sleep(1)
            
            # Incrémenter les secondes
            secondes = secondes + 1
            
            # Gestion du passage à la minute suivante
            if secondes >= 60:
                secondes = 0
                minutes = minutes + 1
            
            # Gestion du passage à l'heure suivante
            if minutes >= 60:
                minutes = 0
                heures = heures + 1
            
            # Gestion du passage à minuit (nouveau jour)
            if heures >= 24:
                heures = 0
    
    except KeyboardInterrupt:
        # L'utilisateur a appuyé sur Ctrl+C
        print("\n\nHorloge arrêtée.  À bientôt Mamie Jeannine !")


# PROGRAMME PRINCIPAL
if __name__ == "__main__": 
    print("=" * 50)
    print("   HORLOGE DE MAMIE JEANNINE")
    print("=" * 50)
    
    heure_personnalisee = None
    
    # Option 1 :  Régler l'heure manuellement
    choix_heure = input("\nVoulez-vous régler l'heure manuellement ?  (o/n) : ")
    if choix_heure.lower() == "o":
        heure_personnalisee = regler_heure()
    
    # Lancer l'horloge
    horloge_principale(heure_personnalisee)