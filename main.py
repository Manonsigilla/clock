import time


class Horloge:
    def __init__(self):
        self.alarme = None
        self.mode_24h = True
        self.heure_actuelle = None

    def afficher_heure(self, heure_tuple):
        """
        Formate et retourne l'heure sous forme de chaîne de caractères. 
        
        Paramètre:  
            heure_tuple:  tuple (heures, minutes, secondes)
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
            
            heure_formatee = f"{heures_12h:02d}:{minutes:02d}:{secondes:02d} {periode}"
        
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
        print("2. Mode 12 heures (ex: 04:30:00 PM)")
        
        try:
            choix = int(input("Choisissez le mode (1 ou 2) : "))
            if choix == 1:
                self.mode_24h = True
                print("Mode 24 heures sélectionné")
            elif choix == 2:
                self.mode_24h = False
                print("Mode 12 heures sélectionné")
            else:
                print("Choix invalide.  Mode 24 heures par défaut.")
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

    def verifier_alarme(self, heure_actuelle):
        """
        Compare l'heure actuelle avec l'heure de l'alarme. 
        """
        if self.alarme is not None and heure_actuelle == self.alarme:
            print("\n\nDRIIIIIING ! RÉVEIL MAMIE JEANNINE !\n")
            self.alarme = None

    # ========================================================================
    # NOUVELLE FONCTIONNALITÉ : CHRONOMÈTRE
    # ========================================================================
    
    def afficher_chronometre(self, heures, minutes, secondes, millisecondes):
        """
        Formate et retourne le temps du chronomètre sous forme de chaîne.
        
        Paramètres:
            heures: nombre d'heures écoulées
            minutes: nombre de minutes écoulées
            secondes: nombre de secondes écoulées
            millisecondes: nombre de millisecondes (0-999)
        
        Retourne:
            str: temps formaté "HH:MM:SS.mmm"
        """
        return f"{heures:02d}:{minutes:02d}:{secondes:02d}.{millisecondes:03d}"

    def chronometre(self):
        """
        Fonction chronomètre qui compte le temps écoulé.
        
        Fonctionnalités:
        - Démarre à 00:00:00.000
        - Affiche le temps en temps réel avec précision à la milliseconde
        - S'arrête avec Ctrl+C
        - Propose de reprendre, réinitialiser ou quitter
        
        La boucle utilise time.perf_counter() pour une meilleure précision
        que time.sleep() seul.
        """
        print("\n" + "=" * 50)
        print("  CHRONOMÈTRE DE MAMIE JEANNINE")
        print("=" * 50)
        print("\nAppuyez sur Entrée pour démarrer le chronomètre...")
        input()
        
        # Initialisation des compteurs
        heures = 0
        minutes = 0
        secondes = 0
        millisecondes = 0
        
        # Variable pour gérer la pause/reprise
        temps_total_ecoule = 0.0  # Temps total en secondes
        
        print("\nChronomètre démarré ! Appuyez sur Ctrl+C pour mettre en pause")
        print("-" * 50)
        
        try:
            # Enregistrer le temps de départ
            temps_depart = time.perf_counter()
            
            while True:
                # Calculer le temps écoulé depuis le départ
                temps_actuel = time.perf_counter()
                temps_ecoule = temps_total_ecoule + (temps_actuel - temps_depart)
                
                # Convertir le temps écoulé en heures, minutes, secondes, millisecondes
                heures = int(temps_ecoule // 3600)
                reste = temps_ecoule % 3600
                minutes = int(reste // 60)
                reste = reste % 60
                secondes = int(reste)
                millisecondes = int((reste - secondes) * 1000)
                
                # Afficher le chronomètre (écrase la ligne précédente)
                print(f"\r{self.afficher_chronometre(heures, minutes, secondes, millisecondes)}", 
                      end="", flush=True)
                
                # Petite pause pour ne pas surcharger le CPU
                time.sleep(0.01)  # Actualisation tous les 10ms
        
        except KeyboardInterrupt:
            # Sauvegarder le temps total écoulé au moment de l'interruption
            temps_actuel = time.perf_counter()
            temps_total_ecoule += (temps_actuel - temps_depart)
            
            print("\n\nChronomètre mis en pause.")
            print(f"Temps écoulé : {self.afficher_chronometre(heures, minutes, secondes, millisecondes)}")
            
            # Menu après la pause
            while True:
                print("\n--- OPTIONS ---")
                print("1. Reprendre le chronomètre")
                print("2. Réinitialiser le chronomètre")
                print("3. Quitter le chronomètre")
                
                try:
                    choix = input("\nVotre choix (1/2/3) : ")
                    
                    if choix == "1":
                        # Reprendre : relancer avec le temps déjà écoulé
                        print("\nChronomètre repris ! Appuyez sur Ctrl+C pour mettre en pause")
                        print("-" * 50)
                        temps_depart = time.perf_counter()
                        
                        try:
                            while True:
                                temps_actuel = time.perf_counter()
                                temps_ecoule = temps_total_ecoule + (temps_actuel - temps_depart)
                                
                                heures = int(temps_ecoule // 3600)
                                reste = temps_ecoule % 3600
                                minutes = int(reste // 60)
                                reste = reste % 60
                                secondes = int(reste)
                                millisecondes = int((reste - secondes) * 1000)
                                
                                print(f"\r{self.afficher_chronometre(heures, minutes, secondes, millisecondes)}", 
                                      end="", flush=True)
                                
                                time.sleep(0.01)
                        
                        except KeyboardInterrupt:
                            temps_actuel = time.perf_counter()
                            temps_total_ecoule += (temps_actuel - temps_depart)
                            print("\n\nChronomètre mis en pause.")
                            print(f"Temps écoulé : {self.afficher_chronometre(heures, minutes, secondes, millisecondes)}")
                            continue
                    
                    elif choix == "2":
                        # Réinitialiser : relancer depuis zéro
                        print("\nChronomètre réinitialisé !")
                        self.chronometre()
                        return
                    
                    elif choix == "3":
                        # Quitter
                        print(f"\nTemps final : {self.afficher_chronometre(heures, minutes, secondes, millisecondes)}")
                        print("Retour au menu principal...\n")
                        return
                    
                    else:
                        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
                
                except (EOFError, KeyboardInterrupt):
                    print("\n\nRetour au menu principal...\n")
                    return

    # ========================================================================
    # FIN DE LA NOUVELLE FONCTIONNALITÉ CHRONOMÈTRE
    # ========================================================================

    def horloge_principale(self, heure_depart=None):
        """
        Fonction principale de l'horloge.
        Affiche l'heure et l'actualise chaque seconde. 
        
        Paramètre: 
            heure_depart: tuple (heures, minutes, secondes) optionnel
        
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
            secondes = now.tm_sec
        
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
        
        MODIFIÉ : Ajout de l'option chronomètre dans le menu principal
        et boucle permettant de revenir au menu après le chronomètre.
        """
        # Boucle principale qui permet de revenir au menu
        while True:
            print("=" * 50)
            print("  HORLOGE DE MAMIE JEANNINE")
            print("=" * 50)
            
            # ===== NOUVEAU : Menu de sélection du mode =====
            print("\n--- MENU PRINCIPAL ---")
            print("1. Horloge (affichage de l'heure)")
            print("2. Chronomètre (mesure du temps écoulé)")
            print("3. Quitter")
            
            try:
                choix_mode = input("\nChoisissez le mode (1, 2 ou 3) : ")
                
                if choix_mode == "2":
                    # Lancer le mode chronomètre
                    self.chronometre()
                    # Après le chronomètre, la boucle while reprend et réaffiche le menu
                    continue
                elif choix_mode == "3":
                    print("\nÀ bientôt Mamie Jeannine !")
                    return
                elif choix_mode != "1":
                    print("Choix invalide. Lancement du mode horloge par défaut.")
            except (ValueError, EOFError, KeyboardInterrupt):
                print("\nLancement du mode horloge par défaut.")
            # ===== FIN DU NOUVEAU MENU =====
            
            heure_personnalisee = None
            
            # Choisir le mode d'affichage
            self.choisir_mode_affichage()
            
            # Régler l'heure manuellement
            choix_heure = input("\nVoulez-vous régler l'heure manuellement ? (o/n) : ")
            if choix_heure.lower() == "o":
                heure_personnalisee = self.regler_heure()
            
            # Régler une alarme
            choix_alarme = input("\nVoulez-vous régler une alarme ?  (o/n) : ")
            if choix_alarme.lower() == "o":
                self.regler_alarme()
            
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
                        # Retourner au menu principal
                        break
                else: 
                    break


# PROGRAMME PRINCIPAL
if __name__ == "__main__": 
    horloge = Horloge()
    horloge.demarrer()