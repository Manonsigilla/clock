# 🕰️ Horloge de Mamie Jeannine

Une horloge numérique interactive développée en Python, offrant des fonctionnalités de personnalisation, d'alarmes, de chronomètre et de timer. 

## 📋 Description

**Horloge de Mamie Jeannine** est une application console qui simule une horloge numérique avec plusieurs fonctionnalités pratiques :

- ⏰ Affichage de l'heure en temps réel
- 🔄 Choix du format d'affichage (24 heures ou 12 heures AM/PM)
- ⚙️ Réglage manuel de l'heure de départ
- 🔔 Configuration d'alarmes multiples personnalisées
- ⏸️ Possibilité de mettre en pause et reprendre l'horloge
- ⏱️ Chronomètre avec précision à la milliseconde
- ⏳ Timer (minuteur) avec compte à rebours

## 🚀 Fonctionnalités

### Horloge

| Fonctionnalité | Description |
|----------------|-------------|
| **Mode 24h/12h** | Basculez entre l'affichage 24 heures (ex: 16: 30: 00) et 12 heures (ex: 04:30:00 PM) |
| **Réglage de l'heure** | Définissez une heure de départ personnalisée |
| **Alarmes multiples** | Programmez plusieurs alarmes avec des noms personnalisés |
| **Pause/Reprise** | Utilisez `Ctrl+C` pour mettre en pause et choisir de reprendre |

### ⏱️ Chronomètre

| Fonctionnalité | Description |
|----------------|-------------|
| **Précision milliseconde** | Affichage au format HH:MM:SS. mmm |
| **Pause/Reprise** | Mettez en pause avec `Ctrl+C` et reprenez où vous vous êtes arrêté |
| **Réinitialisation** | Remettez le chronomètre à zéro à tout moment |

### ⏳ Timer (Minuteur)

| Fonctionnalité | Description |
|----------------|-------------|
| **Compte à rebours** | Définissez une durée et le timer décompte jusqu'à zéro |
| **Alerte sonore** | Notification visuelle 🔔 quand le temps est écoulé |
| **Pause/Reprise** | Mettez en pause avec `Ctrl+C` et reprenez le décompte |

## 🛠️ Technologies Utilisées

- **Python 3** - Langage de programmation principal
- **Module `time`** - Gestion du temps et des délais
  - `time.perf_counter()` pour une précision élevée (chronomètre/timer)
  - `time.localtime()` pour l'heure système

## 📦 Installation

1. Clonez le repository :
   ```bash
   git clone https://github.com/Manonsigilla/clock. git
   ```

2. Accédez au dossier du projet : 
   ```bash
   cd clock
   ```

3. Lancez l'application : 
   ```bash
   python main.py
   ```

## 💻 Utilisation

### Menu Principal

Au lancement, vous avez accès à 4 modes :

```
--- MENU PRINCIPAL ---
1. Horloge
2. Chronomètre
3. Timer
4. Quitter
```

### Mode Horloge

1. Choisissez votre mode d'affichage (24h ou 12h)
2. Optionnellement, réglez l'heure manuellement
3. Optionnellement, configurez une ou plusieurs alarmes avec des noms personnalisés
4. L'horloge démarre et affiche l'heure en temps réel
5. Appuyez sur `Ctrl+C` pour mettre en pause
6. Choisissez de reprendre ou de revenir au menu principal

### Mode Chronomètre

1. Appuyez sur Entrée pour démarrer
2. Le chronomètre affiche le temps écoulé (HH:MM: SS.mmm)
3. Appuyez sur `Ctrl+C` pour mettre en pause
4. Options :  Reprendre | Réinitialiser | Quitter

### Mode Timer

1. Entrez la durée souhaitée (heures, minutes, secondes)
2. Appuyez sur Entrée pour démarrer le compte à rebours
3. Le timer affiche le temps restant (HH:MM: SS.mmm)
4. 🔔 Alerte quand le temps est écoulé
5. Options en pause :  Reprendre | Réinitialiser | Quitter

### Exemple d'exécution

```
==================================================
   HORLOGE DE MAMIE JEANNINE
==================================================

--- MENU PRINCIPAL ---
1. Horloge
2. Chronomètre
3. Timer
4. Quitter

Choisissez le mode (1, 2, 3 ou 4) :  1

--- MODE D'AFFICHAGE ---
1. Mode 24 heures (ex: 16:30:00)
2. Mode 12 heures (ex:  04:30:00 PM)
Choisissez le mode (1 ou 2) : 1
✓ Mode 24 heures sélectionné

Voulez-vous régler l'heure manuellement ? (o/n) : n
Voulez-vous régler des alarmes ? (o/n) : o

--- RÉGLAGE DES ALARMES ---
(Tapez 'fin' pour terminer l'ajout d'alarmes)

Nom de l'alarme (ou 'fin' pour terminer) : Réveil
--- RÉGLAGE DE L'ALARME - Réveil ---
Entrez les heures (0-23) : 7
Entrez les minutes (0-59) : 30
Entrez les secondes (0-59) : 0
✓ Alarme 'Réveil' réglée pour 07:30:00

Nom de l'alarme (ou 'fin' pour terminer) : fin

Horloge démarrée !  Appuyez sur Ctrl+C pour arrêter
----------------------------------------
14:25:33
```

## 👥 Collaborateurs

| Contributeur | Profil GitHub |
|--------------|---------------|
| **Manonsigilla** | [@Manonsigilla](https://github.com/Manonsigilla) |
| **Louis Varennes** | [@louis-varennes](https://github.com/louis-varennes) |
| **Angie Valencia** | [@angie-valencia](https://github.com/angie-valencia) |

## 📄 Licence

Ce projet est open source et disponible sous licence MIT.

---

<p align="center">
  Fait avec ❤️ par l'équipe Clock
</p>
