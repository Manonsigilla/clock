import pygame
import math
import time
from datetime import datetime


class HorlogeVintage:
    def __init__(self):
        pygame.init()
        
        # Configuration de la fenêtre
        self.largeur = 900
        self.hauteur = 675
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Horloge de Mamie Jeannine")
        
        # Couleurs bordeaux chaleureuses
        self.BORDEAUX_FONCE = (80, 20, 40)
        self.BORDEAUX_MOYEN = (120, 40, 60)
        self.BORDEAUX_CLAIR = (150, 60, 80)
        self.IVOIRE = (255, 250, 240)
        self.OR_ANTIQUE = (205, 165, 65)
        self.OR_BRILLANT = (255, 200, 50)
        self.NOIR = (25, 20, 20)
        self.ROUGE_VIN = (128, 0, 32)
        self.CREME = (255, 248, 235)
        
        # Zone horloge (partie gauche)
        self.zone_horloge_largeur = 620
        self.centre_x = 310
        self.centre_y = 335
        self.rayon = 180
        
        # Polices
        self.font_titre = pygame.font.Font(None, 42)
        self.font_chiffres = pygame.font.Font(None, 32)
        self.font_digital = pygame.font.Font(None, 48)
        self.font_info = pygame.font.Font(None, 28)
        self.font_bouton = pygame.font.Font(None, 26)
        self.font_petit = pygame.font.Font(None, 22)
        
        # Paramètres de l'horloge
        self.mode_24h = True
        self.alarme = None
        self.alarme_active = False
        self.heure_personnalisee = None
        self.en_pause = False
        self.temps_depart = None
        
        # Boutons sur le côté droit
        btn_x = 650
        btn_largeur = 200
        btn_hauteur = 60
        espacement = 25
        debut_y = 150
        
        self.boutons = {
            'regler': pygame.Rect(btn_x, debut_y, btn_largeur, btn_hauteur),
            'alarme': pygame.Rect(btn_x, debut_y + (btn_hauteur + espacement), btn_largeur, btn_hauteur),
            'mode': pygame.Rect(btn_x, debut_y + 2 * (btn_hauteur + espacement), btn_largeur, btn_hauteur),
            'pause': pygame.Rect(btn_x, debut_y + 3 * (btn_hauteur + espacement), btn_largeur, btn_hauteur)
        }
        
        # Horloge pygame
        self.clock = pygame.time.Clock()

    def afficher_heure(self, heure_tuple):
        """
        Formate et retourne l'heure sous forme de chaîne de caractères.
        En mode 24h:  hh:mm:ss (ex: 16:30:00)
        En mode 12h: hh:mm: ss AM/PM (ex: 04:30:00 PM)
        
        Paramètre:
            heure_tuple:  tuple (heures, minutes, secondes)
        """
        heures, minutes, secondes = heure_tuple
        
        if self.mode_24h:
            # Mode 24 heures classique
            return f"{heures:02d}:{minutes:02d}:{secondes:02d}"
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
            
            return f"{heures_12h:02d}:{minutes:02d}:{secondes:02d} {periode}"

    def convertir_12h_vers_24h(self, heures_12h, periode):
        """
        Convertit une heure en format 12h vers le format 24h.
        
        Paramètres:
            heures_12h: heure en format 12h (1-12)
            periode: "AM" ou "PM"
        
        Retourne:
            int: heure en format 24h (0-23)
        """
        if periode == "AM": 
            if heures_12h == 12:
                return 0  # 12 AM = 00h
            else:
                return heures_12h
        else:   # PM
            if heures_12h == 12:
                return 12  # 12 PM = 12h
            else:
                return heures_12h + 12

    def regler_heure(self, heure_tuple):
        """
        Permet de régler l'heure de l'horloge.
        
        Paramètre:
            heure_tuple: tuple (heures, minutes, secondes)
        """
        heures, minutes, secondes = heure_tuple
        
        if 0 <= heures <= 23 and 0 <= minutes <= 59 and 0 <= secondes <= 59:
            self.heure_personnalisee = heure_tuple
            self.temps_depart = time.time()
            self.en_pause = False
            print(f"Heure reglee sur {self.afficher_heure(heure_tuple)}")
        else:
            print("Erreur: valeurs hors limites!")

    def regler_alarme(self, heure_tuple):
        """
        Permet de régler l'alarme.
        
        Paramètre:
            heure_tuple: tuple (heures, minutes, secondes)
        """
        heures, minutes, secondes = heure_tuple
        
        if 0 <= heures <= 23 and 0 <= minutes <= 59 and 0 <= secondes <= 59:
            self.alarme = heure_tuple
            print(f"Alarme reglee pour {self.afficher_heure(heure_tuple)}")
        else:
            print("Erreur: valeurs hors limites!")

    def verifier_alarme(self, heure_actuelle):
        """
        Vérifie si l'alarme doit sonner.
        """
        if self.alarme is not None and heure_actuelle == self.alarme:
            print("\n" + "=" * 50)
            print("    DRIIIIIING!  REVEIL MAMIE JEANNINE!")
            print("=" * 50 + "\n")
            self.alarme_active = True
            self.alarme = None

    def obtenir_heure(self):
        """Retourne l'heure actuelle sous forme de tuple."""
        if self.heure_personnalisee is not None and not self.en_pause:
            if self.temps_depart is None:
                self.temps_depart = time.time()
            
            temps_ecoule = time.time() - self.temps_depart
            h, m, s = self.heure_personnalisee
            
            total_secondes = h * 3600 + m * 60 + s + int(temps_ecoule)
            
            heures = (total_secondes // 3600) % 24
            minutes = (total_secondes % 3600) // 60
            secondes = total_secondes % 60
            
            return (heures, minutes, secondes)
        elif self.heure_personnalisee is not None and self.en_pause:
            return self.heure_personnalisee
        else:
            now = datetime.now()
            return (now.hour, now.minute, now.second)

    def dessiner_fond(self):
        """Dessine le fond bordeaux."""
        self.ecran.fill(self.BORDEAUX_FONCE)
        
        # Cadre décoratif
        pygame.draw.rect(self.ecran, self.BORDEAUX_CLAIR,
                        (10, 10, self.largeur - 20, self.hauteur - 20),
                        border_radius=20)
        pygame.draw.rect(self.ecran, self.BORDEAUX_FONCE,
                        (25, 25, self.largeur - 50, self.hauteur - 50),
                        border_radius=15)
        pygame.draw.rect(self.ecran, self.OR_ANTIQUE,
                        (20, 20, self.largeur - 40, self.hauteur - 40),
                        3, border_radius=18)

    def dessiner_zone_horloge(self):
        """Dessine les zones de l'horloge."""
        # Zone titre
        pygame.draw.rect(self.ecran, self.BORDEAUX_MOYEN,
                        (45, 45, 560, 70), border_radius=12)
        pygame.draw.rect(self.ecran, self.OR_ANTIQUE,
                        (45, 45, 560, 70), 2, border_radius=12)
        
        # Zone cadran
        pygame.draw.rect(self.ecran, self.IVOIRE,
                        (45, 125, 560, 420), border_radius=15)
        pygame.draw.rect(self.ecran, self.OR_ANTIQUE,
                        (45, 125, 560, 420), 2, border_radius=15)
        
        # Zone heure digitale
        pygame.draw.rect(self.ecran, self.BORDEAUX_MOYEN,
                        (45, 555, 560, 70), border_radius=12)
        pygame.draw.rect(self.ecran, self.OR_ANTIQUE,
                        (45, 555, 560, 70), 2, border_radius=12)

    def dessiner_panneau_lateral(self):
        """Dessine le panneau latéral."""
        pygame.draw.rect(self.ecran, self.BORDEAUX_MOYEN,
                        (620, 45, 240, 580), border_radius=12)
        pygame.draw.rect(self.ecran, self.OR_ANTIQUE,
                        (620, 45, 240, 580), 2, border_radius=12)
        
        # Titre
        titre = self.font_info.render("Commandes", True, self.OR_BRILLANT)
        rect = titre.get_rect(center=(740, 85))
        self.ecran.blit(titre, rect)
        
        # Ligne
        pygame.draw.line(self.ecran, self.OR_ANTIQUE, (650, 115), (830, 115), 2)
        
        # Affichage alarme
        if self.alarme: 
            label = self.font_petit.render("Alarme programmee:", True, self.CREME)
            self.ecran.blit(label, (650, 480))
            
            heure = self.font_info.render(self.afficher_heure(self.alarme), True, self.OR_BRILLANT)
            rect = heure.get_rect(center=(740, 520))
            self.ecran.blit(heure, rect)
        
        # Instructions
        instr1 = self.font_petit.render("Espace: Stopper alarme", True, self.CREME)
        instr2 = self.font_petit.render("Echap: Quitter", True, self.CREME)
        self.ecran.blit(instr1, (650, 560))
        self.ecran.blit(instr2, (650, 585))

    def dessiner_titre(self):
        """Affiche le titre."""
        titre = self.font_titre.render("Horloge de Mamie Jeannine", True, self.OR_BRILLANT)
        rect = titre.get_rect(center=(325, 80))
        self.ecran.blit(titre, rect)

    def dessiner_cadran(self):
        """Dessine le cadran."""
        # Cercle doré extérieur
        pygame.draw.circle(self.ecran, self.OR_ANTIQUE,
                          (self.centre_x, self.centre_y), self.rayon + 15, 10)
        pygame.draw.circle(self.ecran, self.OR_BRILLANT,
                          (self.centre_x, self.centre_y), self.rayon + 6, 2)
        
        # Fond ivoire
        pygame.draw.circle(self.ecran, self.IVOIRE,
                          (self.centre_x, self.centre_y), self.rayon)
        
        # Cercle intérieur
        pygame.draw.circle(self.ecran, self.OR_ANTIQUE,
                          (self.centre_x, self.centre_y), self.rayon - 8, 2)
        
        # Chiffres romains
        chiffres = ['XII', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI']
        
        for i, chiffre in enumerate(chiffres):
            angle = math.radians(i * 30 - 90)
            x = self.centre_x + (self.rayon - 35) * math.cos(angle)
            y = self.centre_y + (self.rayon - 35) * math.sin(angle)
            
            texte = self.font_chiffres.render(chiffre, True, self.BORDEAUX_FONCE)
            rect = texte.get_rect(center=(x, y))
            self.ecran.blit(texte, rect)
        
        # Graduations
        for i in range(60):
            angle = math.radians(i * 6 - 90)
            
            if i % 5 == 0:
                debut, fin, ep = self.rayon - 20, self.rayon - 10, 3
            else:
                debut, fin, ep = self.rayon - 15, self.rayon - 10, 1
            
            x1 = self.centre_x + debut * math.cos(angle)
            y1 = self.centre_y + debut * math.sin(angle)
            x2 = self.centre_x + fin * math.cos(angle)
            y2 = self.centre_y + fin * math.sin(angle)
            
            pygame.draw.line(self.ecran, self.BORDEAUX_FONCE, (x1, y1), (x2, y2), ep)

    def dessiner_aiguilles(self, heures, minutes, secondes):
        """Dessine les aiguilles."""
        angle_h = (heures % 12) * 30 + minutes * 0.5
        angle_m = minutes * 6 + secondes * 0.1
        angle_s = secondes * 6
        
        # Fonction pour dessiner une aiguille
        def aiguille(angle, longueur, epaisseur, couleur):
            rad = math.radians(angle - 90)
            x_fin = self.centre_x + longueur * math.cos(rad)
            y_fin = self.centre_y + longueur * math.sin(rad)
            x_queue = self.centre_x - (longueur * 0.1) * math.cos(rad)
            y_queue = self.centre_y - (longueur * 0.1) * math.sin(rad)
            pygame.draw.line(self.ecran, couleur, (x_queue, y_queue), (x_fin, y_fin), epaisseur)
        
        aiguille(angle_h, self.rayon * 0.5, 7, self.NOIR)
        aiguille(angle_m, self.rayon * 0.7, 4, self.NOIR)
        aiguille(angle_s, self.rayon * 0.8, 2, self.ROUGE_VIN)
        
        # Centre
        pygame.draw.circle(self.ecran, self.OR_ANTIQUE, (self.centre_x, self.centre_y), 10)
        pygame.draw.circle(self.ecran, self.OR_BRILLANT, (self.centre_x, self.centre_y), 6)

    def dessiner_affichage_digital(self, heure_tuple):
        """Affiche l'heure digitale avec le format approprié (24h ou 12h AM/PM)."""
        heure_str = self.afficher_heure(heure_tuple)
        texte = self.font_digital.render(heure_str, True, self.OR_BRILLANT)
        rect = texte.get_rect(center=(325, 590))
        self.ecran.blit(texte, rect)

    def dessiner_boutons(self, souris_pos):
        """Dessine les boutons avec effet hover."""
        textes = {
            'regler': "Regler l'heure",
            'alarme': "Regler alarme",
            'mode': f"Mode {'24H' if self.mode_24h else '12H AM/PM'}",
            'pause': "Reprendre" if self.en_pause else "Pause"
        }
        
        for nom, rect in self.boutons.items():
            # Effet hover
            if rect.collidepoint(souris_pos):
                couleur_fond = self.BORDEAUX_CLAIR
                couleur_texte = self.OR_BRILLANT
            else:
                couleur_fond = self.BORDEAUX_MOYEN
                couleur_texte = self.CREME
            
            # Ombre
            pygame.draw.rect(self.ecran, self.BORDEAUX_FONCE,
                           (rect.x + 3, rect.y + 3, rect.width, rect.height),
                           border_radius=10)
            # Fond
            pygame.draw.rect(self.ecran, couleur_fond, rect, border_radius=10)
            # Bordure
            pygame.draw.rect(self.ecran, self.OR_ANTIQUE, rect, 2, border_radius=10)
            
            # Texte
            texte = self.font_bouton.render(textes[nom], True, couleur_texte)
            texte_rect = texte.get_rect(center=rect.center)
            self.ecran.blit(texte, texte_rect)

    def dessiner_alarme_active(self):
        """Animation alarme."""
        if self.alarme_active:
            if pygame.time.get_ticks() % 600 < 300:
                pygame.draw.rect(self.ecran, self.ROUGE_VIN,
                               (50, 500, 550, 45), border_radius=8)
                texte = self.font_info.render("DRIIIING!  REVEIL MAMIE JEANNINE!", True, self.CREME)
                rect = texte.get_rect(center=(325, 522))
                self.ecran.blit(texte, rect)

    def dialogue_saisie_heure(self, titre):
        """
        Dialogue pour saisir une heure.
        S'adapte au mode actuel (24H ou 12H AM/PM).
        """
        saisie = ""
        etape = 0
        valeurs = [0, 0, 0]  # [heures, minutes, secondes]
        periode = "AM"  # Pour le mode 12H
        
        if self.mode_24h:
            labels = ["Heures (0-23):", "Minutes (0-59):", "Secondes (0-59):"]
            nb_etapes = 3
        else:
            labels = ["Heures (1-12):", "Minutes (0-59):", "Secondes (0-59):", "AM ou PM:"]
            nb_etapes = 4
            valeurs[0] = 12  # Valeur par défaut en mode 12H
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return None
                    
                    # Étape AM/PM (mode 12H uniquement)
                    if not self.mode_24h and etape == 3:
                        if event.key == pygame.K_a:
                            periode = "AM"
                        elif event.key == pygame.K_p:
                            periode = "PM"
                        elif event.key == pygame.K_RETURN:
                            # Convertir en format 24H pour le stockage interne
                            heures_24h = self.convertir_12h_vers_24h(valeurs[0], periode)
                            return (heures_24h, valeurs[1], valeurs[2])
                    
                    # Étapes numériques
                    elif event.key == pygame.K_RETURN:
                        try:
                            valeur = int(saisie) if saisie else (valeurs[0] if etape == 0 and not self.mode_24h else 0)
                            
                            # Validation selon l'étape et le mode
                            if etape == 0:  # Heures
                                if self.mode_24h:
                                    valide = 0 <= valeur <= 23
                                else:
                                    valide = 1 <= valeur <= 12
                            else:  # Minutes ou secondes
                                valide = 0 <= valeur <= 59
                            
                            if valide:
                                valeurs[etape] = valeur
                                etape += 1
                                saisie = ""
                                
                                # En mode 24H, on termine après les secondes
                                if self.mode_24h and etape >= 3:
                                    return tuple(valeurs)
                            else:
                                saisie = ""
                        except ValueError: 
                            saisie = ""
                    
                    elif event.key == pygame.K_BACKSPACE:
                        saisie = saisie[:-1]
                    
                    elif event.unicode.isdigit() and len(saisie) < 2 and etape < 3:
                        saisie += event.unicode
            
            # Dessiner le dialogue
            cx, cy = self.largeur // 2, self.hauteur // 2
            
            # Fond semi-transparent
            overlay = pygame.Surface((self.largeur, self.hauteur), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            self.ecran.blit(overlay, (0, 0))
            
            # Boîte de dialogue (plus grande pour le mode 12H)
            hauteur_dialog = 300 if not self.mode_24h else 260
            pygame.draw.rect(self.ecran, self.BORDEAUX_FONCE,
                           (cx - 180, cy - 150, 360, hauteur_dialog), border_radius=15)
            pygame.draw.rect(self.ecran, self.IVOIRE,
                           (cx - 170, cy - 140, 340, hauteur_dialog - 20), border_radius=12)
            pygame.draw.rect(self.ecran, self.OR_ANTIQUE,
                           (cx - 180, cy - 150, 360, hauteur_dialog), 3, border_radius=15)
            
            # Titre du dialogue
            mode_txt = "(Format 24H)" if self.mode_24h else "(Format 12H AM/PM)"
            t = self.font_info.render(titre, True, self.BORDEAUX_FONCE)
            self.ecran.blit(t, t.get_rect(center=(cx, cy - 115)))
            m = self.font_petit.render(mode_txt, True, self.BORDEAUX_MOYEN)
            self.ecran.blit(m, m.get_rect(center=(cx, cy - 90)))
            
            # Aperçu de l'heure
            if self.mode_24h:
                preview = f"{valeurs[0]:02d}:{valeurs[1]:02d}:{valeurs[2]: 02d}"
            else: 
                preview = f"{valeurs[0]:02d}:{valeurs[1]:02d}:{valeurs[2]:02d} {periode}"
            
            p = self.font_digital.render(preview, True, self.BORDEAUX_MOYEN)
            self.ecran.blit(p, p.get_rect(center=(cx, cy - 50)))
            
            # Label de l'étape actuelle
            if etape < len(labels):
                l = self.font_petit.render(labels[etape], True, self.BORDEAUX_FONCE)
                self.ecran.blit(l, l.get_rect(center=(cx, cy + 5)))
            
            # Zone de saisie ou boutons AM/PM
            if not self.mode_24h and etape == 3:
                # Boutons AM/PM
                am_rect = pygame.Rect(cx - 80, cy + 30, 70, 45)
                pm_rect = pygame.Rect(cx + 10, cy + 30, 70, 45)
                
                # Couleurs selon la sélection
                am_couleur = self.OR_BRILLANT if periode == "AM" else self.BORDEAUX_MOYEN
                pm_couleur = self.OR_BRILLANT if periode == "PM" else self.BORDEAUX_MOYEN
                am_texte_couleur = self.BORDEAUX_FONCE if periode == "AM" else self.CREME
                pm_texte_couleur = self.BORDEAUX_FONCE if periode == "PM" else self.CREME
                
                pygame.draw.rect(self.ecran, am_couleur, am_rect, border_radius=8)
                pygame.draw.rect(self.ecran, self.OR_ANTIQUE, am_rect, 2, border_radius=8)
                am_txt = self.font_bouton.render("AM", True, am_texte_couleur)
                self.ecran.blit(am_txt, am_txt.get_rect(center=am_rect.center))
                
                pygame.draw.rect(self.ecran, pm_couleur, pm_rect, border_radius=8)
                pygame.draw.rect(self.ecran, self.OR_ANTIQUE, pm_rect, 2, border_radius=8)
                pm_txt = self.font_bouton.render("PM", True, pm_texte_couleur)
                self.ecran.blit(pm_txt, pm_txt.get_rect(center=pm_rect.center))
                
                # Instructions
                instr = self.font_petit.render("A: AM | P: PM | Entree: valider", True, self.BORDEAUX_CLAIR)
                self.ecran.blit(instr, instr.get_rect(center=(cx, cy + 100)))
            else:
                # Zone de saisie numérique
                pygame.draw.rect(self.ecran, self.BORDEAUX_MOYEN,
                               (cx - 50, cy + 30, 100, 45), border_radius=8)
                s = self.font_digital.render(saisie + "_", True, self.CREME)
                self.ecran.blit(s, s.get_rect(center=(cx, cy + 52)))
                
                # Instructions
                instr = self.font_petit.render("Entree: valider | Echap: annuler", True, self.BORDEAUX_CLAIR)
                self.ecran.blit(instr, instr.get_rect(center=(cx, cy + 100)))
            
            pygame.display.flip()
            self.clock.tick(30)

    def gerer_clic(self, pos):
        """Gère les clics sur les boutons."""
        for nom, rect in self.boutons.items():
            if rect.collidepoint(pos):
                print(f"Bouton clique: {nom}")
                
                if nom == 'regler':
                    nouvelle_heure = self.dialogue_saisie_heure("Regler l'heure")
                    if nouvelle_heure: 
                        self.regler_heure(nouvelle_heure)
                
                elif nom == 'alarme':
                    if self.alarme_active:
                        self.alarme_active = False
                    else:
                        nouvelle_alarme = self.dialogue_saisie_heure("Regler l'alarme")
                        if nouvelle_alarme:
                            self.regler_alarme(nouvelle_alarme)
                
                elif nom == 'mode': 
                    self.mode_24h = not self.mode_24h
                    mode_str = "24H" if self.mode_24h else "12H AM/PM"
                    print(f"Mode change: {mode_str}")
                
                elif nom == 'pause':
                    if not self.en_pause:
                        self.heure_personnalisee = self.obtenir_heure()
                        self.temps_depart = None
                        self.en_pause = True
                        print("Horloge en pause")
                    else: 
                        self.temps_depart = time.time()
                        self.en_pause = False
                        print("Horloge reprise")
                
                return True
        return False

    def demarrer(self):
        """Boucle principale."""
        en_cours = True
        
        print("=" * 50)
        print("   HORLOGE DE MAMIE JEANNINE")
        print("=" * 50)
        print("L'heure s'actualise toutes les secondes.\n")
        
        while en_cours:
            souris_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clic gauche
                        self.gerer_clic(event.pos)
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        en_cours = False
                    elif event.key == pygame.K_SPACE:
                        self.alarme_active = False
            
            # Obtenir l'heure
            heure_actuelle = self.obtenir_heure()
            heures, minutes, secondes = heure_actuelle
            
            # Console
            print(f"\r{self.afficher_heure(heure_actuelle)}", end="", flush=True)
            
            # Vérifier alarme
            self.verifier_alarme(heure_actuelle)
            
            # Dessiner
            self.dessiner_fond()
            self.dessiner_zone_horloge()
            self.dessiner_panneau_lateral()
            self.dessiner_titre()
            self.dessiner_cadran()
            self.dessiner_aiguilles(heures, minutes, secondes)
            self.dessiner_affichage_digital(heure_actuelle)
            self.dessiner_boutons(souris_pos)
            self.dessiner_alarme_active()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        print("\n\nA bientot Mamie Jeannine!")
        pygame.quit()


# PROGRAMME PRINCIPAL
if __name__ == "__main__":
    horloge = HorlogeVintage()
    horloge.demarrer()