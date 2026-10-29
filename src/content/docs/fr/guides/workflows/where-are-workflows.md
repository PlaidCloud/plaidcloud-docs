---
title: Où se trouvent les workflows
description: Accédez à vos workflows PlaidCloud au sein de vos projets et gérez-les grâce à l'interface des workflows et aux outils de navigation du projet.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/where-are-workflows.md
---

Les workflows se trouvent dans les projets. Pour les trouver :

1. Dans le menu supérieur, ouvrez **Projets**.
2. Cliquez sur le projet qui contient les workflows que vous cherchez.
3. Passez à l'onglet **Workflows**.

Vous verrez tous les workflows du projet, organisés selon une hiérarchie de type dossiers.

## Ce que vous voyez pour chaque workflow

- **Statut** : en cours d'exécution, terminé normalement, ou terminé avec un avertissement ou une erreur
- Horodatages **Créé** et **dernière mise à jour**, ainsi que les noms des personnes concernées
- **Organisation en dossiers** : les workflows peuvent être regroupés dans des dossiers imbriqués pour faciliter la gestion dans les grands projets

Double-cliquez sur un workflow pour ouvrir l'**Explorateur de workflow**, où vous pouvez consulter les étapes, exécuter l'ensemble du workflow, exécuter une seule étape ou en choisir une plage.

## Pourquoi un workflow peut ne pas être visible

Les workflows que vous pouvez voir dépendent de deux éléments :

- **Accès au projet** : l'administrateur de votre espace de travail vous donne accès à des projets précis. Si vous vous attendez à voir un projet sans y parvenir, demandez à un propriétaire du projet de vous y ajouter.
- **Rôle d'affichage** : au sein d'un projet, l'un de ces trois rôles vous est attribué :
  - **Architecte** : peut tout voir et tout modifier
  - **Gestionnaire** : peut voir et exécuter les workflows, mais pas les modifier
  - **Explorateur** : visibilité limitée ; certains workflows peuvent être masqués

Si vous vous attendez à voir certains workflows sans y parvenir, votre rôle les filtre peut-être. Un Architecte du projet peut confirmer ce que vous devriez voir.

Votre rôle détermine aussi si vous pouvez modifier une étape. Si vous pouvez ouvrir un workflow mais pas le modifier, le formulaire d'étape s'ouvre en lecture seule : ses champs sont désactivés et son bouton **Enregistrer** est masqué, ce qui vous permet de lire la configuration d'une étape sans pouvoir la modifier. Cela s'applique partout où le formulaire s'ouvre : l'icône d'engrenage et le menu contextuel de la table du workflow, le canevas visuel, la grille **Étapes** du projet et le menu **Nouvelle étape**.

## Modifications non enregistrées dans une fenêtre d'étape

Une fenêtre d'étape signale les modifications non enregistrées par un **•** dans son titre. Fermer la fenêtre avec **Échap**, le **X**, **Annuler** ou le bouton de son onglet affiche la question **Ignorer les modifications non enregistrées ?** afin qu'une modification ne soit pas perdue par accident. Choisissez **Ignorer** pour fermer sans enregistrer, ou revenez en arrière pour continuer à modifier.

## Étapes suivantes

- [Explorateur de workflow](/fr/guides/workflows/workflow-explorer/) : que faire dans un workflow ouvert
- [Créer un workflow](/fr/guides/workflows/create-workflow/) : en démarrer un nouveau
- [Exécuter un workflow](/fr/guides/workflows/run-a-workflow/) : exécuter de bout en bout
