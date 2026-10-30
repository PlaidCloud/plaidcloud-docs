---
title: La galerie d'applications
description: "Ajoutez une application Studio à la galerie ou retirez-la, et créez une application à partir d'une application listée."
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

La galerie d'applications est l'étagère où votre espace de travail range des applications Panel prêtes à l'emploi. Toute personne qui peut consulter le projet d'une application listée peut en créer sa propre copie et la modifier : une bonne application devient ainsi un point de départ plutôt que quelque chose que chacun reconstruit.

## Créer une application depuis la galerie

1. Dans **Mes applications Panel**, choisissez **Nouvelle application Studio**.
2. Sous **Partir de**, choisissez **À partir de la galerie**.
3. Sélectionnez une application sous **Application de la galerie**. Sa description s'affiche sous le sélecteur.
4. Nommez votre application, sélectionnez son **Projet** et choisissez **Créer**.

Vous pouvez aussi choisir **Galerie** dans la barre d'outils **Mes applications Panel** pour parcourir la galerie seule. Chaque carte affiche le nom, la description et le projet de l'application, avec **Créer une application à partir de ceci…**. La galerie ne liste que les applications des projets que vous pouvez consulter.

La nouvelle application est une copie des fichiers de l'application listée. Votre copie et l'original sont distincts : modifier l'une ne modifie jamais l'autre.

## Lister votre application

Vous devez disposer d'un accès en modification au projet de l'application. Seules les applications créées dans [Panel Studio](/fr/guides/panel-apps/studio/) et appartenant à un projet peuvent être listées ; les applications serveur, WASM et Dash ne le peuvent pas.

1. Ouvrez l'application dans Studio et choisissez **Galerie…**. Le bouton n'est disponible que pour une application qui appartient à un projet.
2. Saisissez une **Description** à afficher sur la carte de la galerie.
3. Choisissez **Lister dans la galerie** et confirmez.

Pour modifier la description, choisissez **Mettre à jour la fiche**. Pour retirer l'application de la galerie, ouvrez **Galerie…** et choisissez **Retirer de la galerie**. Déplacer l'application vers un autre projet la retire également de la galerie.

## Qui peut voir quoi

Toute personne qui peut consulter le projet peut lire la source de l'application listée, y compris les modifications que vous publiez ultérieurement. Ne mettez ni mots de passe ni notes privées dans les fichiers d'une application listée. Choisir de lister une application vous demande d'abord de le confirmer, et la mise en liste est consignée dans le journal d'audit.

Les personnes qui créent une application depuis la galerie obtiennent une copie des fichiers du dossier propre à l'application uniquement. Elles ne voient jamais les détails du dépôt de l'application, ses connexions ni ses paramètres de webhook.

## Étapes suivantes

- [Panel Studio](/fr/guides/panel-apps/studio/) — modifiez et publiez la copie que vous créez.
- [Le kit d'applications Panel](/fr/guides/panel-apps/app-kit/) — les composants dont sont faites la plupart des applications de la galerie.
