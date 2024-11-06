# Gestion de Festivals et Artistes

## Description
Ce projet est une application de gestion de festivals et d'artistes. Elle permet d'ajouter des artistes de deux types : Musicien et DJ, et d'organiser des festivals avec des artistes. Le projet utilise une base de données SQLite pour stocker les informations des festivals et des artistes. L'application a une interface graphique simple et intuitive construite avec Tkinter.

## Fonctionnalités
- Ajouter un festival avec son nom et sa date.
- Ajouter des artistes (Musicien ou DJ) avec des informations détaillées (nom, instrument/style musical).
- Lier des artistes à des festivals.
- Visualiser la liste des festivals et des artistes associés dans l'interface.

## Classes Principales

### 1. **Classe Artiste**
La classe **`Artiste`** est la classe parent pour tous les types d'artistes (Musicien, DJ). Elle possède les attributs suivants :
- `nom` : Le nom de l'artiste.
- `type_artiste` : Le type de l'artiste (Musicien ou DJ).
- `info_supplementaire` : Informations supplémentaires comme l'instrument pour un musicien ou le style musical pour un DJ.

Les méthodes de cette classe incluent :
- `ajouter_artiste()` : Ajoute l'artiste à la base de données.

### 2. **Classe Musicien (hérite de Artiste)**
La classe **`Musicien`** est une sous-classe d'**`Artiste`** et représente un musicien. Elle hérite des attributs et des méthodes de la classe **`Artiste`** mais initialise son type en tant que **"Musicien"**.

### 3. **Classe DJ (hérite de Artiste)**
La classe **`DJ`** est une sous-classe d'**`Artiste`** et représente un DJ. Elle hérite des attributs et des méthodes de la classe **`Artiste`** mais initialise son type en tant que **"DJ"**.

### 4. **Classe Festival**
La classe **`Festival`** gère les informations d'un festival :
- `nom` : Le nom du festival.
- `date` : La date du festival.
- `artistes` : La liste des artistes associés à ce festival.

Les méthodes de cette classe incluent :
- `ajouter_artiste()` : Ajoute un artiste à la liste des artistes du festival.
- `ajouter_festival()` : Ajoute le festival à la base de données.

## Relations entre les Classes
- **Artiste** est la classe parente des classes **Musicien** et **DJ**. Ces deux sous-classes héritent des attributs et des méthodes de la classe **Artiste**.
- **Festival** est une classe qui peut contenir plusieurs **Artistes**. Un festival peut avoir plusieurs artistes associés (qu'ils soient musiciens ou DJs).

## Technologies Utilisées
- **Python** : Langage de programmation principal.
- **Tkinter** : Utilisé pour l'interface graphique de l'application.
- **SQLite** : Base de données légère pour stocker les informations des artistes et festivals.
