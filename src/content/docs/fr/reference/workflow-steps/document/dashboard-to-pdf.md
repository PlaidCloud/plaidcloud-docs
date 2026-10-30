---
title: Étape Convert Dashboard to PDF
description: Générez un PDF d'un tableau de bord PlaidCloud dans un compte de documents, pour chaque ligne d'un jeu de données de filtres, en appliquant les valeurs de la ligne comme filtres du tableau de bord.
sidebar:
  order: 22
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/dashboard-to-pdf.md
---

## Description

Génère des PDF d'un tableau de bord et les écrit dans un compte de documents. Utilisez-la pour planifier un tableau de bord : un dossier de clôture mensuelle, une diffusion à des personnes qui ne se connectent pas, ou un instantané archivé de l'état des chiffres à une date donnée.

L'étape effectue un rendu pour chaque ligne d'un jeu de données de filtres, en appliquant les valeurs de cette ligne comme filtres du tableau de bord. Une seule étape peut ainsi produire un ensemble de PDF par région ou par entité en une seule exécution.

## Configuration

### Tableau de bord

Le tableau de bord à générer.

### Jeu de données des filtres

La table dont les lignes pilotent les rendus : un PDF par ligne.

### Chemin de sortie

Le compte de documents et le dossier dans lesquels les PDF sont écrits.

### Options

- **Génération PDF simultanée** — nombre de rendus exécutés en parallèle. La valeur par défaut est 8 ; réduisez-la si le tableau de bord est assez lourd pour que les rendus parallèles expirent.
- **Délai d'attente du rendu (secondes)** — présent dans la configuration de l'étape, mais **actuellement non appliqué** par l'exécuteur de workflow. Le définir n'a aucun effet pour le moment.

### Filtres du tableau de bord

Les filtres propres au tableau de bord, chacun avec son **ID du filtre de tableau de bord**. Ils sont lus depuis le tableau de bord lorsque vous renseignez le mappage.

### Mappage des colonnes source

Les colonnes du jeu de données de filtres et la façon dont chacune est utilisée. Utilisez **Inspecter la source › Renseigner la table de mappage** pour lire les colonnes et les filtres du tableau de bord ; une colonne nommée comme un filtre du tableau de bord est marquée comme filtre sur celui-ci. Si vous renseignez à nouveau, le **Genre** et la **Colonne de filtre mappée** déjà définis pour une colonne sont conservés.

Définissez le **Genre** de chaque colonne :

- **Filtre de colonne** — la valeur de la colonne définit le filtre du tableau de bord indiqué dans **Colonne de filtre mappée**, qui doit être l'un des filtres du tableau de bord.
- **Nom du fichier** — la colonne fournit le nom de fichier de chaque PDF. Une seule colonne peut être le Nom du fichier. Sans colonne de ce type, l'étape émet un avertissement et génère les noms automatiquement.
- **Aucun filtre** — la colonne n'est pas utilisée.

Au moins une colonne doit être un **Filtre de colonne**.

## Contrôles à l'enregistrement

L'enregistrement de l'étape est refusé, avec le nom de la colonne concernée, dans les cas suivants :

- Aucune colonne n'est un Filtre de colonne avec une Colonne de filtre mappée — *Marquez au moins une colonne source comme Filtre de colonne, avec la Colonne de filtre mappée qu'elle définit.*
- Un Filtre de colonne n'a pas de Colonne de filtre mappée, ou en désigne une qui ne figure pas parmi les filtres du tableau de bord — *La Colonne de filtre mappée 'Region' pour la colonne source 'region' ne fait pas partie des filtres du tableau de bord.*
- Plusieurs colonnes sont le Nom du fichier — *Une seule colonne source peut être le Nom du fichier ; region, entity le sont toutes.*
- Une colonne Filtre de colonne ou Nom du fichier n'a pas de type de données — *La colonne source 'region' n'a pas de type de données ; inspectez de nouveau la source pour l'actualiser.* Certaines étapes enregistrées dans le formulaire d'étape n'ont pas les types de leurs colonnes et échouent à chaque exécution tant qu'elles ne les retrouvent pas. Exécutez **Inspecter la source › Renseigner la table de mappage** pour les restaurer ; vos marquages Filtre de colonne et Nom du fichier sont conservés.

## Voir aussi

- [Étapes Document](/fr/reference/workflow-steps/document/)
- [Tableaux de bord (guide)](/fr/guides/dashboards/)
- [Étapes Report](/fr/reference/workflow-steps/reports/)
