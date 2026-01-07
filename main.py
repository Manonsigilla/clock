import time


class Horloge:
    def __init__(self):
        self.alarmes = {}  # Dictionnaire pour stocker les alarmes nommées
        self.mode_24h = True
        self.heure_actuelle = None

    def afficher_heure(self, heure_tuple):
        """
        Formate et retourne l'heure sous forme de chaîne de caractères.  
        
        Paramètre:  
            heure_tuple:   tuple (heures, minutes, secondes)
        """
        heures, minutes, secondes = heure_tuple  # Tuple unpacking
        
        if self.mode_24h:
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
            
            heure_formatee = f"{heures_12h:  02d}:{minutes:02d}:{secondes:02d} {periode}"
        
        return heure_formatee

    def demander_heure(self, titre="RÉGLAGE"):
        """
        Demande une heure à l'utilisateur avec validation.
        Fonction utilitaire réutilisable.  
        
        Retourne:  
            tuple (heures, minutes, secondes) ou None si erreur
        """
        print(f"\n--- {titre} ---")
        
        try:
            heures = int(input("Entrez les heures (0-23) : "))
            minutes = int(input("Entrez les minutes (0-59) : "))
            secondes = int(input("Entrez les secondes (0-59) : "))
            
            if 0 <= heures <= 23 and 0 <= minutes <= 59 and 0 <= secondes <= 59:
                return (heures, minutes, secondes)
            else:
                print("Erreur : valeurs hors limites !")
                return None
        except ValueError:
            print("Erreur : veuillez entrer des nombres entiers !")
            return None

    def regler_heure(self):
        """
        Permet à l'utilisateur de régler l'heure de démarrage de l'horloge. 
        
        Retourne:  
            tuple (heures, minutes, secondes) ou None si erreur
        """
        heure_reglee = self.demander_heure("RÉGLAGE DE L'HEURE")
        
        if heure_reglee is not None:
            print(f"Heure réglée sur {self.afficher_heure(heure_reglee)}")
        
        return heure_reglee

    def choisir_mode_affichage(self):
        """
        Permet à l'utilisateur de choisir entre le mode 24h et 12h.
        """
        print("\n--- MODE D'AFFICHAGE ---")
        print("1. Mode 24 heures (ex: 16:30:00)")
        print("2. Mode 12 heures (ex:  04:30:00 PM)")
        
        try:
            choix = int(input("Choisissez le mode (1 ou 2) : "))
            if choix == 1:
                self.mode_24h = True
                print("✓ Mode 24 heures sélectionné")
            elif choix == 2:
                self.mode_24h = False
                print("✓ Mode 12 heures sélectionné")
            else:
                print("Choix invalide.   Mode 24 heures par défaut.")
                self.mode_24h = True
        except ValueError:
            print("Erreur : veuillez entrer 1 ou 2.  Mode 24 heures par défaut.")
            self.mode_24h = True

    def regler_alarme(self):
        """
        Demande à l'utilisateur l'heure de l'alarme et la stocke.
        """
        heure_alarme = self.demander_heure("RÉGLAGE DE L'ALARME")
        
        if heure_alarme is not None:
            self.alarme = heure_alarme
            print(f"Alarme réglée pour {self.afficher_heure(self.alarme)}")

    def regler_multiple_alarmes(self):
        """
        Permet de régler plusieurs alarmes avec un nom pour chaque. 
        """
        print("\n--- RÉGLAGE DES ALARMES ---")
        print("(Tapez 'fin' pour terminer l'ajout d'alarmes)")
        
        while True: 
            nom_alarme = input("\nNom de l'alarme (ou 'fin' pour terminer) : ").strip()
            
            if nom_alarme. lower() == "fin":
                break
            
            if not nom_alarme:
                print("Veuillez entrer un nom valide.")
                continue
            
            if nom_alarme in self.alarmes:
                print(f" L'alarme '{nom_alarme}' existe déjà.")
                continue
            
            heure_alarme = self.demander_heure(f"RÉGLAGE DE L'ALARME - {nom_alarme}")
            
            if heure_alarme is not None:
                self.alarmes[nom_alarme] = heure_alarme
                print(f"✓ Alarme '{nom_alarme}' réglée pour {self.afficher_heure(heure_alarme)}")

    def verifier_alarme(self, heure_actuelle):
        """
        Vérifie toutes les alarmes et les déclenche si l'heure correspond.
        """
        alarmes_declenchees = []
        
        for nom_alarme, heure_alarme in self.alarmes.items():
            if heure_actuelle == heure_alarme:
                alarmes_declenchees.append(nom_alarme)
        
        if alarmes_declenchees:
            alarmes_str = ", ".join(alarmes_declenchees)
            print(f"\n\n DRIIIIIING !   ALARME(S) : {alarmes_str} !\n")
            for nom in alarmes_declenchees: 
                del self.alarmes[nom]

    def horloge_principale(self, heure_depart=None):
        """
        Fonction principale de l'horloge. 
        Affiche l'heure et l'actualise chaque seconde.  
        
        Paramètre:  
            heure_depart:  tuple (heures, minutes, secondes) optionnel
        
        Retourne:  
            tuple (heures, minutes, secondes) - l'heure au moment de l'arrêt
        """
        # Initialisation de l'heure
        if heure_depart is not None:
            heures, minutes, secondes = heure_depart
        else:
            now = time.localtime()
            heures = now.tm_hour
            minutes = now.tm_min
            secondes = now. tm_sec
        
        print("\nHorloge démarrée ! Appuyez sur Ctrl+C pour arrêter")
        print("-" * 40)
        
        # Boucle principale de l'horloge
        try: 
            while True: 
                heure_actuelle = (heures, minutes, secondes)
                
                print(f"\r{self.afficher_heure(heure_actuelle)}", end="", flush=True)
                
                self.verifier_alarme(heure_actuelle)
                
                time.sleep(1)
                
                secondes += 1
                
                if secondes >= 60:
                    secondes = 0
                    minutes += 1
                
                if minutes >= 60:
                    minutes = 0
                    heures += 1
                
                if heures >= 24:
                    heures = 0
        
        except KeyboardInterrupt:
            print("\n\nHorloge mise en pause.")
            return (heures, minutes, secondes)

    def demarrer(self):
        """
        Point d'entrée principal de l'horloge. 
        Gère le menu et la boucle de relance. 
        """
        print("=" * 50)
        print("  HORLOGE DE MAMIE JEANNINE")
        print("=" * 50)
        
        heure_personnalisee = None
        
        # Choisir le mode d'affichage
        self.choisir_mode_affichage()
        
        # Régler l'heure manuellement
        choix_heure = input("\nVoulez-vous régler l'heure manuellement ?  (o/n) : ")
        if choix_heure. lower() == "o":
            heure_personnalisee = self.regler_heure()
        
        # Régler plusieurs alarmes
        choix_alarme = input("\nVoulez-vous régler des alarmes ?  (o/n) : ")
        if choix_alarme.lower() == "o":
            self.regler_multiple_alarmes()
        
        # Boucle permettant de relancer l'horloge après Ctrl+C
        while True:
            # Lancer l'horloge et récupérer l'heure au moment de l'arrêt
            heure_actuelle = self.horloge_principale(heure_personnalisee)
            
            # Si l'horloge a été interrompue (Ctrl+C)
            if heure_actuelle is not None:
                # Afficher l'heure actuelle et proposer de relancer
                choix_relance = input(
                    f"\nHeure actuelle : {self.afficher_heure(heure_actuelle)}"
                    f"\nVoulez-vous relancer l'horloge ? (o/n) : "
                )
                
                if choix_relance.lower() == "o":
                    # Relancer avec l'heure actuelle
                    heure_personnalisee = heure_actuelle
                else:
                    print("\n À bientôt Mamie Jeannine !")
                    break
            else: 
                break


# PROGRAMME PRINCIPAL
if __name__ == "__main__":  
    horloge = Horloge()
    horloge.demarrer()