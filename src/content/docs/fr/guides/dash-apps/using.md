---
title: Utiliser une application Dash
description: Suivez le statut de génération, ouvrez, régénérez, verrouillez, consultez les journaux, modifiez et supprimez les applications Plotly Dash publiées depuis l'écran Mes applications Panel de PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/using.md
---

Les applications Dash apparaissent dans le même écran **Mes applications Panel** que vos applications Panel WASM et serveur, avec **Dash** indiqué dans la colonne **Exécution** et leur propre icône pour les distinguer facilement. Tout ce qui figure sur cette page reprend [Utiliser une application Panel](/fr/guides/panel-apps/using/) pour une application serveur, à une exception près signalée plus bas : les applications Dash n'ont pas encore de **Métriques d'utilisation**.

## Statut de génération

La colonne **Statut** d'une application Dash suit sa génération, et la liste s'actualise d'elle-même pendant qu'une génération est en cours :

- **Génération en cours…** : PlaidCloud construit votre dépôt dans un conteneur. L'application n'a pas encore d'URL.
- **Prêt** : la génération a réussi. L'URL de l'application est active et l'icône **Ouvrir** apparaît sur sa ligne.
- **Échec** : la génération ne s'est pas terminée. Vérifiez le point d'entrée et la branche, puis modifiez l'application pour la republier.

## Régénérer une application Dash

Cliquez sur l'icône **Régénérer** sur la ligne d'une application Dash pour la régénérer et la redéployer sans modifier ses paramètres. Le statut de l'application repasse à **Génération en cours…** pendant que PlaidCloud construit à nouveau la même branche et le même point d'entrée, puis revient à **Prêt** lorsque la nouvelle génération est en ligne.

Utilisez **Régénérer** après des modifications de dépendances, des mises à jour de l'image de base ou une génération échouée de façon transitoire. Modifier puis enregistrer une application Dash la régénère aussi, mais une régénération n'exige pas d'ouvrir le formulaire de modification.

## Verrouiller une application

Cliquez sur l'icône de **verrou** sur la ligne d'une application pour la protéger contre les modifications accidentelles. Tant qu'une application Dash est verrouillée :

- **Modifier**, **Supprimer** et **Régénérer** refusent de s'exécuter et vous indiquent que l'application est verrouillée.
- **Un envoi vers la branche de l'application ne la régénère pas** : la régénération automatique est ignorée jusqu'au déverrouillage. Envoyez à nouveau (ou utilisez **Régénérer**) après le déverrouillage pour prendre en compte la modification.
- L'ouverture de l'application et l'affichage de ses journaux continuent tous deux de fonctionner : le verrou n'arrête que les modifications, jamais les lecteurs.

Cliquez de nouveau sur l'icône pour déverrouiller. L'icône indique l'état actuel de l'application : fermée lorsqu'elle est verrouillée, ouverte sinon. Le verrou protège contre les accidents ; ce n'est pas un contrôle de sécurité : toute personne pouvant modifier les applications Dash peut aussi les déverrouiller.

## Ouvrir une application Dash

Cliquez sur l'icône **Ouvrir** au début de la ligne d'une application prête pour la lancer dans un nouvel onglet, à l'adresse `https://<your-tenant-host>/serve/<slug>/`. L'icône n'apparaît que lorsque l'application est **Prête**.

Une application Dash retombe à zéro lorsqu'elle est inactive pour économiser des ressources ; la première ouverture après une période d'inactivité doit donc la démarrer. Pendant ce temps, vous voyez un **écran de chargement PlaidCloud** plutôt qu'un onglet vide, et l'application s'affiche d'elle-même dès qu'elle est prête. Si une application ne peut pas démarrer, l'écran de chargement se transforme en un message **« This app didn't start »** accompagné d'un bouton **Réessayer** ; si cela se reproduit, modifiez l'application pour vérifier son point d'entrée et sa branche, puis republiez-la.

> **Un `dcc.Interval` (ou tout autre interrogation permanente) neutralise la mise à l'échelle à zéro tant que son onglet reste ouvert.** La mise à l'échelle à zéro suppose que l'application devienne silencieuse, sans requête en cours, dès que plus personne ne l'utilise activement. Un composant qui émet des requêtes en continu selon un minuteur, tel que `dcc.Interval`, maintient l'application éveillée tant que cet onglet est ouvert, même si la personne qui le regarde s'est absentée. Si vous voulez qu'une application redescende entre deux visites, évitez l'interrogation permanente, ou arrêtez l'intervalle une fois la page restée inactive un certain temps.

## Consulter les journaux

Cliquez sur l'icône **Afficher les journaux** sur la ligne d'une application Dash pour ouvrir son visionneur de journaux, avec les mêmes onglets **Exécution** et **Génération**, filtres, plage de temps et volet de détails que ceux d'une application Panel serveur ; voir [Consulter les journaux](/fr/guides/panel-apps/using/#afficher-les-journaux-applications-serveur) pour le détail complet. Chaque ligne du journal d'exécution est étiquetée avec l'**utilisateur** dont la session l'a produite, comme pour une application Panel serveur.

**Les Métriques d'utilisation ne sont pas disponibles pour les applications Dash dans cette version** : l'icône **Métriques d'utilisation** qui apparaît sur la ligne d'une application Panel serveur n'apparaît pas pour les applications Dash ; il n'y a donc pas encore de ventilation par utilisateurs uniques ou par session à consulter.

## Modifier une application

Cliquez sur l'icône en forme de **crayon** sur la ligne d'une application Dash pour la modifier. Vous pouvez changer le nom, le slug, la branche, le point d'entrée, le CPU, la mémoire, la fenêtre d'inactivité, l'indicateur public, les domaines de diffusion intégrée et le mémo. La **Connexion Git** est figée une fois l'application créée et s'affiche en lecture seule. Il n'y a aucun champ **Conception** à modifier : ce paramètre est propre à Panel. L'enregistrement régénère l'application : son statut repasse à **Génération en cours…** jusqu'à ce que la nouvelle génération soit prête.

## Supprimer une application

Cliquez sur l'icône **moins** sur la ligne d'une application Dash et confirmez. Sa suppression détruit sa génération et son déploiement, et l'URL de l'application cesse immédiatement de fonctionner.
