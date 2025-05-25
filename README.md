# Password Generator

Un générateur de mots de passe personnalisable en ligne de commande.

## Fonctionnalités

- Longueur paramétrable du mot de passe
- Inclusion optionnelle de lettres minuscules, majuscules, chiffres et symboles
- Possibilité de fournir une liste personnalisée de symboles

## Installation

Clonez ce dépôt et installez les dépendances (si nécessaire) :

```bash
git clone <URL_DU_REPO>
cd <NOM_DU_REPO>
# Pas de dépendances externes spécifiques requises
```

## Usage

Lancez le script Python avec les options suivantes :
```bash
python main.py [OPTIONS]
```


### Options principales
| Option           | Alias | Description                              | Par défaut              |
|------------------|-------|----------------------------------------|-------------------------|
| `--length`       | `-L`  | Longueur du mot de passe                | 12                      |
| `--lowercase`    |       | Inclure les lettres minuscules (a-z)   | Activé                  |
| `--uppercase`    |       | Inclure les lettres majuscules (A-Z)   | Désactivé               |
| `--numbers`      |       | Inclure les chiffres (0-9)              | Désactivé               |
| `--symbols`      |       | Inclure des symboles spéciaux           | Désactivé               |
| `--symbols-list` |       | Liste personnalisée des symboles       | `!@#$%^&*()-_=+[]{};:,.<>?` |

### Exemple

Générer un mot de passe de 15 caractères avec majuscules, chiffres et symboles personnalisés :

```bash
python main.py --length 15 --uppercase --numbers --symbols --symbols-list "$@!{"
```

## Fonctionnement interne

- Le script garantit qu’au moins un caractère de chaque catégorie activée est présent.

- Les caractères restants sont tirés aléatoirement dans l’ensemble complet des caractères activés.

- Le mot de passe final est mélangé pour maximiser l’aléatoire.

## Licence

Projet open source — libre d’utilisation et de modification.