---
title: Utiliser une application Panel
description: Suivez le statut de génération, ouvrez, régénérez, verrouillez, consultez les journaux et les métriques d'utilisation, modifiez et supprimez les applications HoloViz Panel publiées depuis l'écran Mes applications Panel de PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Chaque application publiée apparaît sur l'écran **Mes applications Panel** avec son **Exécution**, son **Statut**, son **Slug** et ses horodatages. La colonne la plus à gauche ouvre l'application ; les autres icônes de la ligne vous permettent de la verrouiller contre les modifications accidentelles, de la modifier, de la supprimer et — pour les applications serveur — de la régénérer, d'afficher ses journaux et d'afficher ses métriques d'utilisation. L'icône d'ouverture reflète l'exécution de l'application, ce qui permet de distinguer au premier coup d'œil les applications WASM des applications serveur.

## Statut de génération (applications serveur)

La colonne **Statut** d'une application serveur suit sa génération, et la liste s'actualise d'elle-même tant qu'une génération est en cours :

- **Génération en cours…** — PlaidCloud génère votre dépôt dans un conteneur. L'application n'a pas encore d'URL.
- **Prêt** — la génération a réussi. L'URL de l'application est active et l'icône **Ouvrir** apparaît sur sa ligne.
- **Échec** — la génération ne s'est pas terminée. Vérifiez le point d'entrée et la branche, puis modifiez l'application pour la republier.

Les applications WASM n'ont pas d'étape de génération et sont disponibles dès leur publication.

## Régénérer une application serveur

Cliquez sur l'icône **Régénérer** de la ligne d'une application serveur pour la régénérer et la redéployer sans modifier ses paramètres. Le statut de l'application repasse à **Génération en cours…** pendant que PlaidCloud génère à nouveau la même branche et le même point d'entrée, puis revient à **Prêt** lorsque la nouvelle génération est en ligne.

Utilisez **Régénérer** après des modifications de dépendances, des mises à jour de l'image de base ou une génération en échec transitoire. Modifier puis enregistrer une application serveur la régénère aussi, mais une régénération ne nécessite pas d'ouvrir le formulaire de modification.

Pour une application [App Runner](/fr/guides/workflows/use-converted-alteryx-apps/#garder-lapplication-à-jour) — le formulaire de saisie généré pour une application Alteryx convertie — **Régénérer** et l'enregistrement d'une modification commencent par actualiser ses fichiers générés vers la version actuelle d'App Runner, puis lancent la génération. PlaidCloud fait de même pour chaque application App Runner non verrouillée lorsque PlaidCloud lui-même est mis à jour ; une application verrouillée nécessite un **Régénérer** après son déverrouillage.

## Verrouiller une application

Cliquez sur l'icône **Verrouiller** de la ligne d'une application pour la protéger des modifications accidentelles. Tant qu'une application est verrouillée :

- **Modifier**, **Supprimer** et **Régénérer** refusent de s'exécuter et vous indiquent que l'application est verrouillée.
- Un **push sur la branche d'une application serveur ne la régénère pas** — la régénération automatique est ignorée jusqu'au déverrouillage de l'application. Aucune génération ne s'exécute pour un push ignoré, si bien que rien de nouveau n'apparaît dans les journaux de génération de l'application ; effectuez un nouveau push (ou utilisez **Régénérer**) après le déverrouillage pour prendre en compte la modification.
- L'ouverture de l'application, la consultation de ses journaux et celle de ses métriques d'utilisation continuent de fonctionner — le verrou n'empêche que les modifications, jamais les personnes qui consultent l'application.

Cliquez à nouveau sur l'icône pour déverrouiller. L'icône indique l'état actuel de l'application : fermée lorsqu'elle est verrouillée, ouverte dans le cas contraire.

Le verrou est une protection contre les accidents — une modification par erreur, une suppression involontaire ou un push Git qui arrive sur une application que vous présentez en démonstration — comme le verrou des workflows et des étapes de workflow. Ce n'est **pas** un contrôle de sécurité : toute personne qui peut modifier des applications Panel peut aussi les déverrouiller.

> Deux cas que le verrou ne couvre pas : une **génération déjà en cours** au moment du verrouillage se termine quand même et est mise en ligne, et les fichiers d'une application **WASM** se trouvent dans son compte de documents ; leur remplacement modifie donc l'application en cours d'exécution sans toucher à l'enregistrement verrouillé.

## Ouvrir une application

Cliquez sur l'icône **Ouvrir** au début de la ligne d'une application prête pour la lancer dans un nouvel onglet. **Ouvrir** est aussi le premier élément du menu **⋯** de la ligne. Consultez [Le menu des actions de ligne](/fr/guides/dashboards/using-dashboards/#le-menu-dactions-de-ligne).

- Une application serveur est servie à l'adresse `https://<your-tenant-host>/serve/<slug>/`.
- L'icône **Ouvrir** n'apparaît que lorsqu'une application serveur a le statut **Prêt**.

Une application serveur est ramenée à zéro lorsqu'elle est inactive afin d'économiser des ressources ; la première ouverture après une période d'inactivité doit donc la redémarrer. Pendant ce temps, vous voyez un **écran de chargement PlaidCloud** au lieu d'un onglet vide : le nom de votre application, sa progression à travers les étapes **Démarrage**, **Préparation** et **Chargement de l'application**, et l'ID de votre espace de travail, dans votre thème clair ou sombre. L'application s'affiche d'elle-même dès qu'elle est prête (généralement en quelques secondes, jusqu'à environ une minute lors d'un démarrage à froid), puis répond normalement jusqu'à sa prochaine période d'inactivité.

> Si une application ne peut pas démarrer, l'écran de chargement se transforme en un message indiquant que l'application n'a pas démarré et à quelle étape elle s'est arrêtée, accompagné d'un bouton **Réessayer**, au lieu de tourner indéfiniment. Si cela se reproduit, modifiez l'application pour vérifier son point d'entrée et sa branche, puis republiez-la, ou contactez votre administrateur PlaidCloud.

### Apparence

Les applications Panel serveur utilisent par défaut le design moderne **FAST** de PlaidCloud, mais le paramètre **Conception** de l'application permet de revenir au style **Par défaut** de Panel lorsque du CSS existant en dépend. Le thème — clair, sombre, ou un commutateur clair/sombre que les personnes qui consultent l'application peuvent basculer — se définit dans le modèle de votre application. Consultez [Définir le thème](/fr/guides/panel-apps/creating/#définir-le-thème-clair-sombre-ou-commutable) dans le guide de création pour les approches possibles. Si les tables ou le style personnalisé de votre application sont conçus pour un fond clair, gardez-la fixée sur le thème clair.

## Afficher les journaux (applications serveur)

Cliquez sur l'icône **Afficher les journaux** de la ligne d'une application serveur pour ouvrir son visualiseur de journaux. (Les applications WASM s'exécutent entièrement dans le navigateur et n'ont pas de journaux serveur ; l'icône n'apparaît donc que sur les lignes des applications serveur.)

Le visualiseur comporte deux onglets :

- **Exécution** (affiché en premier) — la sortie propre à l'application en cours d'exécution : tout ce qu'elle journalise, tout ce qu'elle affiche et toutes les erreurs non interceptées. Ces entrées sont conservées même après que l'application est ramenée à zéro, ce qui vous permet de revoir ce qu'une session précédente a fait.
- **Génération** — la sortie de la génération du conteneur de l'application. Utilisez-le pour comprendre *pourquoi* une génération affiche **Échec** — par exemple, une dépendance qui ne s'installe pas.

Chaque onglet propose des filtres **Info / Avert. / Erreur**, une plage de temps **Journaux depuis** (de la dernière heure jusqu'à 30 jours, ou tout), un bouton **Actualiser** et **Actualisation auto** pour interroger les nouvelles entrées — pratique lorsque vous surveillez une application active ou une génération en cours. Les entrées les plus récentes sont listées en premier.

> Si la sortie de la génération n'a pas pu être capturée, l'onglet Génération affiche une courte note expliquant pourquoi, au lieu de rester vide.

### Lire un message de journal complet

La table des journaux tronque les lignes longues pour que la liste reste lisible. Sélectionnez une ligne de journal pour ouvrir un **volet de détails** à côté de la table, qui affiche le message complet de l'entrée. C'est le moyen le plus simple de lire ce qui est trop long pour la table — un long message d'erreur ou une trace de pile complète — sans qu'il soit coupé.

### Copier des lignes de journal

Vous pouvez sélectionner plusieurs lignes de journal à la fois et cliquer sur **Copier** pour les placer dans votre presse-papiers. C'est pratique pour coller des journaux dans une conversation avec un assistant IA lorsque vous déboguez votre application, ou dans un message à votre équipe ou au support PlaidCloud.

### Qui a déclenché une ligne de journal

Lorsque votre application connecte les personnes qui la consultent, chaque ligne de journal est associée à l'**utilisateur** dont la session l'a produite, ce qui vous permet de savoir quelle personne a rencontré une erreur ou un avertissement donné. Cette association se fait au mieux : certaines lignes du framework et du démarrage s'exécutent avant l'intervention de toute personne et peuvent ne pas afficher d'utilisateur.

## Métriques d'utilisation (applications serveur)

Cliquez sur l'icône **Usage Metrics** de la ligne d'une application serveur — à côté de **Afficher les journaux** — pour voir comment l'application est utilisée. La vue résume :

- **Utilisateurs uniques** — le nombre de personnes distinctes qui ont ouvert l'application.
- **Sessions** — le nombre de fois où elle a été ouverte.
- **Durée moyenne et médiane des sessions** — la durée approximative d'une visite.
- **Dernière utilisation** — le moment de la dernière ouverture de l'application.

Sous le résumé, vous obtenez une répartition **par utilisateur** et **par jour**, pour voir qui utilise l'application et comment l'utilisation évolue dans le temps.

> Les durées sont approximatives. Les applications serveur passent en veille et sont réduites lorsque personne ne les utilise ; la fin exacte d'une session n'est donc pas toujours observée — considérez les durées comme un repère, pas comme une mesure exacte.

## Modifier une application

Cliquez sur l'icône en forme de **crayon** de la ligne d'une application pour la modifier. Le formulaire de modification correspond à l'exécution de l'application.

Pour une application **serveur**, vous pouvez modifier le nom, le slug, la branche, le point d'entrée, le CPU, la mémoire, la conception, le délai d'inactivité, l'indicateur public, les domaines de diffusion intégrée et le mémo. La **Connexion Git** est figée une fois l'application créée et s'affiche en lecture seule. L'enregistrement régénère l'application — son statut repasse à **Génération en cours…** jusqu'à ce que la nouvelle génération soit prête.

## Supprimer une application

Cliquez sur l'icône **moins** de la ligne d'une application et confirmez ; la suppression ou la dépublication d'une application demande toujours une confirmation préalable. La suppression d'une application serveur démantèle sa génération et son déploiement ; la suppression d'une application WASM dépublie le fichier statique. L'URL de l'application cesse de fonctionner immédiatement.

L'outil MCP `panel_deployment_manage` ne propose plus la dépublication. Supprimez plutôt une application depuis cette liste.
