---
title: La galerie d'applications
description: Référencez une application Panel comme modèle à partir duquel votre espace de travail peut démarrer, et créez une nouvelle application à partir d'une application référencée.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

La galerie d'applications est l'étagère où votre espace de travail conserve des applications Panel prêtes à l'emploi. Toute personne qui peut consulter le projet d'une application référencée peut en créer sa propre copie et la modifier : une bonne application devient ainsi un point de départ plutôt que quelque chose que chacun reconstruit.

## Créer une application depuis la galerie

1. Dans **Mes applications Panel**, choisissez **Create app**.
2. Sous **Partir de**, choisissez **Depuis la galerie**.
3. Choisissez une application. Sa description s'affiche sous le sélecteur.
4. Nommez votre application, choisissez son **Projet** et choisissez **Créer**.

Vous pouvez aussi ouvrir la galerie séparément : chaque carte y affiche le nom, la description et le projet de l'application, avec **Create app from this…**. La galerie ne répertorie que les applications des projets que vous pouvez consulter.

La nouvelle application est une copie des fichiers de l'application référencée. Votre copie et l'original sont distincts : modifier l'un ne modifie jamais l'autre.

## Référencer votre application

Vous avez besoin de l'autorisation de modification sur le projet de l'application, et l'application doit avoir été créée dans [Panel Studio](/fr/guides/panel-apps/studio/) et affectée à un projet.

1. Ouvrez l'application dans Studio et choisissez **Gallery…**.
2. Saisissez une **Description** à afficher sur la carte de la galerie.
3. Choisissez **List in gallery** et confirmez.

Pour modifier la description, choisissez **Update listing**. Pour retirer l'application, choisissez **Take out of gallery**. Déplacer l'application vers un autre projet la retire également de la galerie.

## Qui peut voir quoi

Toute personne qui peut consulter le projet peut lire le code source de l'application référencée, y compris les modifications que vous publierez ultérieurement. Ne mettez ni mots de passe ni notes privées dans les fichiers d'une application référencée. Choisir de référencer une application vous demande d'abord de le confirmer, et le référencement est consigné dans le journal d'audit.

Les personnes qui créent une application depuis la galerie obtiennent uniquement une copie des fichiers situés dans le dossier propre de l'application. Elles ne voient jamais les détails du dépôt de l'application, ses connexions ni ses paramètres de webhook.

## Étapes suivantes

- [Panel Studio](/fr/guides/panel-apps/studio/) : modifiez et publiez la copie que vous créez.
- [Le kit d'applications Panel](/fr/guides/panel-apps/app-kit/) : les composants dont sont faites la plupart des applications de la galerie.
