# TP Git - Student List Manager
## Informations du Binôme

- Binôme A : Yousra AMEUR
- Binôme B : Aya AIT EL CADI

### Objectif

Réaliser un mini-projet collaboratif de gestion de liste d'élèves en binôme (A et B),
en mettant en pratique les commandes Git vues en cours.

### Exemples de code complets

- [Exemple en Python](/code_exemple/python/)
- [Exemple en Java](/code_exemple/java/src/)

Cela donne par exemple:

```bash
python .\main.py
Student List Manager
Type 'help' to show commands.
> help
Available commands:
  list
  add <id> <name>
  remove <id>
  export <format> <file_path>  (formats: csv, json)
  help
  quit
> add 1 Arnaud
Student 'Arnaud' added.
> add 2 john
Student 'john' added.
> add 3 Laura
Student 'Laura' added.
> list
Students:
- 1: Arnaud
- 2: john
- 3: Laura
> remove 2
Student with id '2' removed.
> list
Students:
- 1: Arnaud
- 3: Laura
> quit
Bye.
```

### Contrainte

- Durée totale: 3h
- Travail en binôme
- Le langage est libre.
- Le focus est Git.

### Structure imposée pour le projet

```text
README.md
.gitignore
src/
  Main.java          (ou main.py, main.js, etc.)
  Student.java       (ou student.py, etc.)
  StudentService.java (ou student_service.py, etc.)
```

### Règles de collaboration

- Une seule personne intègre dans `main` à la fois.
- Avant chaque intégration dans `main`, faire un `pull` de `main`.
- Noms de branches imposés (ci-dessous).
- Commits atomiques avec messages explicites.

## Phases du TP

### Phase 1 - Initialisation (20 min)

- binomeA: créer un dépôt GitHub
- binomeA: ajouter binomeB au projet (Settings > Collaborators)
- binomeA et binomeB: cloner le dépôt sur vos PC
- binomeA: créer `README.md` et `.gitignore`
- binomeA: premier commit sur `main`, puis push
- binomeB: récupérer les modifications de `main`

### Phase 2 - Base commune (25 min)

- binomeB: créer la branche `feature/interfaces`
- binomeB: dans `Student`, ajouter la structure de donnée (`id`, `nom`)
- binomeB: commit
- binomeB: dans `StudentService`, ajouter les **signatures de fonctions sans implémentation**:
  - `printList`
  - `addStudent`
  - `removeStudent`
- binomeB: commit puis push

### Phase 3 - Intégration base commune (20 min)

- binomeA: récupérer la branche `feature/interfaces`
- binomeA: rebase sur `main` si nécessaire
- binomeA: merger `feature/interfaces` dans `main`
- binomeA: supprimer la branche fusionnée (locale et distante)
- binomeB: se replacer sur `main` et récupérer les modifications

### Phase 4 - Développement parallèle sans conflit (35 min)

- **binomeA**: créer `feature/student-service` depuis `main`, **implémenter les fonctions** de `StudentService`, commits puis push
- **binomeB**: créer `feature/main-cli` depuis `main`, **implémenter l'interface CLI** dans `Main` avec les commandes `list`, `add`, `remove`, commits puis push

### Phase 5 - Intégration croisée (15 min)

Intégration séquentielle obligatoire:

- **Étape 1 (binomeB)**: intégrer `feature/student-service` dans `main`, push
- **Étape 2 (binomeA)**: faire `pull` de `main`, puis intégrer `feature/main-cli`, push

### Phase 6 - Travail parallèle avec conflit volontaire (35 min)

- binomeA: créer `feature/export-a` depuis `main`
- binomeB: créer `feature/export-b` depuis `main`
- Chaque binome modifie **les mêmes zones**:
  - ajouter une méthode d'export différente dans `StudentService` (au moins 2 formats au total, par exemple `csv` et `json`)
  - utiliser cette méthode dans l'interface CLI (`Main`)
- commits puis push sur vos branches respectives

### Phase 7 - Intégration finale et résolution de conflit (20 min)

- binomeB: intégrer `feature/export-a` dans `main`, push
- binomeA: récupérer `main`, intégrer `feature/export-b` dans `main`
- binomeA: **résoudre le conflit proprement**, commit de résolution, push

### Phase 8 - Livraison (10 min)

- mettre à jour `README.md` (binome, choix techniques, commandes Git utilisées)
- poser le tag `v1.0` sur le dernier commit de `main`
- envoyer l'URL du projet GitHub à `arnaud.mercier@epfedu.fr`
- titre du mail: `[TP_GIT] NOM1 NOM2`

---



## Langage choisi

Python 3

## Choix techniques

- Architecture simple en 3 fichiers : `main.py`, `student.py`, `student_service.py`
- Séparation claire entre la logique métier (StudentService) et l’interface CLI (main)
- Gestion des données en mémoire (liste d’objets Student)
- Export des données en deux formats : CSV et JSON
- Résolution manuelle d’un conflit Git lors de l’intégration finale

## Description du projet

Application en ligne de commande permettant de :
- Ajouter un étudiant
- Supprimer un étudiant
- Afficher la liste des étudiants
- Exporter la liste en format CSV et JSON

## Commandes Git utilisées pendant le TP

- git clone
- git checkout -b
- git add
- git commit
- git push
- git pull
- git fetch
- git merge
- git reset
- git restore
- git tag
- Résolution manuelle de conflit
- gestion de branches (feature/*) et intégration séquentielle dans main

## Version finale

Tag créé : v1.0
