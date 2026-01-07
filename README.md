# 🕰️ Horloge de Mamie Jeannine

Une horloge numérique interactive développée en Python, offrant des fonctionnalités de personnalisation et d'alarme.

## 📋 Description

**Horloge de Mamie Jeannine** est une application console qui simule une horloge numérique avec plusieurs fonctionnalités pratiques :

- ⏰ Affichage de l'heure en temps réel
- 🔄 Choix du format d'affichage (24 heures ou 12 heures AM/PM)
- ⚙️ Réglage manuel de l'heure de départ
- 🔔 Configuration d'une alarme personnalisée
- ⏸️ Possibilité de mettre en pause et reprendre l'horloge

## 🚀 Fonctionnalités

| Fonctionnalité | Description |
|----------------|-------------|
| **Mode 24h/12h** | Basculez entre l'affichage 24 heures (ex: 16:30:00) et 12 heures (ex: 04:30:00 PM) |
| **Réglage de l'heure** | Définissez une heure de départ personnalisée |
| **Alarme** | Programmez une alarme qui se déclenche à l'heure souhaitée |
| **Pause/Reprise** | Utilisez `Ctrl+C` pour mettre en pause et choisir de reprendre |

## 🛠️ Technologies Utilisées

- **Python 3** - Langage de programmation principal
- **Module `time`** - Gestion du temps et des délais

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

1. Au lancement, choisissez votre mode d'affichage (24h ou 12h)
2. Optionnellement, réglez l'heure manuellement
3. Optionnellement, configurez une alarme
4. L'horloge démarre et affiche l'heure en temps réel
5. Appuyez sur `Ctrl+C` pour mettre en pause
6. Choisissez de reprendre ou de quitter l'application

### Exemple d'exécution

```
==================================================
   HORLOGE DE MAMIE JEANNINE
==================================================

--- MODE D'AFFICHAGE ---
1. Mode 24 heures (ex: 16:30:00)
2. Mode 12 heures (ex:  04:30:00 PM)
Choisissez le mode (1 ou 2) : 1
✓ Mode 24 heures sélectionné

Voulez-vous régler l'heure manuellement ? (o/n) : n
Voulez-vous régler une alarme ?  (o/n) : o

--- RÉGLAGE DE L'ALARME ---
Entrez les heures (0-23) : 14
Entrez les minutes (0-59) : 30
Entrez les secondes (0-59) : 0
Alarme réglée pour 14:30:00

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
