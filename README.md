<div style="display: flex; align-items: center; white-space: nowrap; gap: 10px;">
    <img src="https://image.noelshack.com/fichiers/2024/44/6/1730568505-37bfb2bb-301d-48f8-8d71-3d9b0e636132.jpg" alt="Logo" width="60" vertical-align: middle;/>
    <h1 style="margin: 0; font-size: 24px;">CompanyScraper</h1>
</div>

**CompanyAnalyzer** est un outil permettant d’extraire automatiquement les données essentielles d’une fiche entreprise sur le site web [pappers.fr](https://www.pappers.fr/), en simulant un navigateur avec Selenium. Les informations sont extraites et affichées sous forme de tableau lisible dans le terminal.

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation des dépendances](#installation-des-dépendances)
- [Utilisation](#utilisation)
- [Exemple de sortie](#exemple-de-sortie)
- [Remarques](#remarques)
- [Auteurs](#auteurs)
- [License](#license)

## Fonctionnalités

- **Navigation furtive automatisée** grâce à `selenium-stealth`
- **Extraction intelligente** de données via `BeautifulSoup`
- **Affichage structuré** des résultats sous forme de tableau avec `tabulate`
- **Silencieux** : supprime tous les messages parasites dans le terminal
- **Sécurité intégrée** : gère les erreurs de chargement de page ou d’éléments manquants
- **Aucune API nécessaire** : fonctionne sur des pages web accessibles publiquement

## Prérequis

Assurez-vous d’avoir **Python 3.8 ou supérieur** ainsi que **Google Chrome** et **ChromeDriver** installés sur votre machine.

### Modules requis :

- `selenium`
- `selenium-stealth`
- `beautifulsoup4`
- `tabulate`

## Installation des dépendances

Installez les bibliothèques nécessaires avec :

```bash
pip install selenium selenium-stealth beautifulsoup4 tabulate
```

## Utilisation

1. Lancez le script avec Python :

```bash
python company_scraper.py
```

2. Entrez l’URL de la fiche entreprise lorsque le script vous le demande :

```bash
👉 Entrez l'URL de la fiche entreprise : https://www.pappers.fr/entreprise/google-france-443061841
```

3. Les informations seront affichées sous forme de tableau clair dans le terminal :

## Exemple de sortie

```
[+] Chargement de la page...

--- 📊 Données extraites ---

+-----------------------------+------------------------------------------------------+
| Champ                       | Valeur                                               |
+-----------------------------+------------------------------------------------------+
| Nom                         | EXEMPLE SARL                                         |
| SIREN                       | 123 456 789                                          |
| SIRET (siège)               | 123 456 789 00010                                    |
| Forme juridique             | Société à responsabilité limitée                    |
| Numéro de TVA               | FR123456789                                          |
| Inscription au RCS          | Paris B 123 456 789                                  |
| Inscription au RNE          | Oui                                                  |
| Numéro RCS                  | 123 456 789 RCS Paris                                |
| Capital social              | 10 000 €                                             |
| Statut                      | Active                                               |
| Adresse                     | 10 Rue de l'Entreprise, 75000 Paris                  |
| Activité                    | Conseil en systèmes informatiques                    |
| Effectif                    | 1 à 2 salariés                                       |
| Création                    | 01/01/2020                                           |
| Dirigeant                   | Jean Dupont                                          |
| Activité principale déclarée| Programmation informatique                           |
| Code NAF ou APE             | 6201Z                                                |
| Domaine d’activité          | Informatique                                         |
| Forme d'exercice            | Individuelle                                         |
| Convention collective       | Syntec                                               |
| Clôture d'exercice          | 31/12                                                |
+-----------------------------+------------------------------------------------------+
```

## Remarques

- Les champs affichés peuvent varier selon la page ciblée.
- Le scraping est réalisé de manière furtive, mais reste soumis aux limitations du site (CAPTCHA, accès restreint, etc.).
- Si certaines données ne sont pas trouvées, un message d’erreur lisible est affiché à la place.

## Auteurs

- [OneFileSystem](https://github.com/OneFileSystem)

## License

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](./LICENSE) pour plus d’informations.
