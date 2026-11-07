---
title: PlaidCloud Git
description: Hébergez, versionnez et partagez des dépôts Git dans PlaidCloud, avec tickets, pull requests, tableaux de projet, versions et wikis, et l'authentification unique intégrée.
sidebar:
  label: Vue d'ensemble
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git est un service Git privé intégré à votre espace de travail. Chaque espace de travail dispose de son propre serveur Git pour stocker le code, la configuration, les notebooks et tous les autres fichiers versionnés, ainsi que les tickets, pull requests et tableaux de projet que votre équipe utilise pour collaborer dessus.

Vous vous connectez avec votre compte PlaidCloud : il n'y a donc ni nom d'utilisateur ni mot de passe distinct à configurer. Les nouveaux dépôts sont privés par défaut, visibles uniquement des membres auxquels vous accordez l'accès.

## Ouvrir Git

Sélectionnez **Git** dans la liste des applications de votre espace de travail. L'onglet **Git** s'ouvre et affiche l'hôte de l'espace de travail, votre rôle et une liste **Dépôts**. Utilisez **View all in Git** pour accéder à l'interface web de Git, **Manage who can push** (si vous pouvez gérer les groupes) pour ouvrir la gestion des groupes, et le bouton d'actualisation pour recharger. Utilisez **← Back to** votre espace de travail dans Git pour revenir à PlaidCloud.

Un indicateur de rôle affiche votre niveau (**Administrateur**, **Contributeur** ou **Lecteur**), avec une ligne précisant ce que cela vous permet de faire. Chaque ligne de dépôt affiche son nom, sa description (lorsqu'il en a une), **Mis à jour** avec la date, un champ de clonage en lecture seule avec un bouton de copie, et **Ouvrir**, qui ouvre le dépôt dans Git. Les dépôts que vous créez en privé se trouvent directement dans Git, pas dans cette liste.

## Cloner un dépôt

Copiez l'adresse de clonage du dépôt depuis sa ligne. La première fois que vous copiez, une carte **Set up Git on your computer** apparaît avec les étapes ci-dessous. Sélectionnez **Ignorer** pour la masquer, et **How to clone** dans l'en-tête pour la faire réapparaître.

1. Git doit être installé sur votre ordinateur.
2. Créez un jeton dans **Paramètres → Applications** avec l'autorisation **write:repository**. La carte renvoie vers cette page.
3. Indiquez à Git qui vous êtes, avec les deux commandes `git config --global user.name` et `user.email` affichées, qui contiennent déjà votre nom et votre adresse e-mail.
4. Clonez le dépôt avec la commande `git clone` affichée. Lorsque Git demande un mot de passe, collez ce jeton, et non votre mot de passe PlaidCloud.

Chaque commande dispose de son propre bouton de copie. Consultez [Dépôts](/fr/guides/git/repositories/) pour la procédure complète. La copie nécessite un accès en écriture et un compte Git activé : si le bouton de copie est désactivé, ouvrez un dépôt une fois pour activer votre compte ou, en tant que **Lecteur**, demandez un accès en écriture comme indiqué ci-dessous.

## Niveaux d'accès

Toute personne ayant accès à Git peut lire les dépôts partagés de l'espace de travail. Deux autres niveaux permettent de pousser du code.

| Rôle | Ce que vous pouvez faire | Accordé par |
|---|---|---|
| **Lecteur** | Consulter et cloner les dépôts partagés. | Par défaut pour chaque membre. |
| **Contributeur** | Tout ce que permet la lecture, et pousser vers le dépôt `apps`, où se trouve le code des applications [Panel](/fr/guides/panel-apps/deploy-from-git/) et [Dash](/fr/guides/dash-apps/deploy-from-git/). | Le groupe de sécurité **Git Contributors**. |
| **Administrateur** | Tout ce que permet le rôle Contributeur, pousser vers tous les dépôts, y compris `udfs`, et créer des organisations. | Le groupe de sécurité **Git Administration**. |

Le dépôt `udfs` est réservé aux administrateurs, car les fonctions définies par l'utilisateur s'exécutent sous l'identité du workflow qui les appelle.

Si vous êtes **Lecteur**, l'onglet **Git** indique jusqu'à trois administrateurs de l'espace de travail à qui vous pouvez demander de vous ajouter à **Git Contributors**.

## Git depuis les applications et les UDF

La fenêtre d'une application Panel ou Dash comporte une section **Dépôt** qui indique son dépôt, sa branche et l'état de sa construction, avec **Edit in browser** et **Copy clone URL** pour les membres qui peuvent pousser. La barre d'outils d'une UDF reposant sur Git comporte **Ouvrir**, qui ouvre le dépôt à sa branche dans Git, et **Edit in browser** pour les administrateurs.

## Accorder l'accès à Git

Les administrateurs de l'espace de travail accordent l'accès dans **Identité** en ajoutant des membres à un groupe de sécurité, ou en ajoutant l'autorisation à un groupe qui vous est propre.

1. Ajoutez le membre à **Git Contributors** pour lui permettre de pousser du code d'application, ou à **Git Administration** pour en faire un administrateur Git.
2. Pour donner à chaque nouveau membre l'accès en écriture au code des applications, ajoutez **Git Contributors** à vos groupes par défaut. **Git Administration** ne peut pas être un groupe par défaut.
3. Pour vérifier ce qu'un membre peut faire, ouvrez le membre et sélectionnez l'onglet **Git**. Il affiche le nom d'utilisateur Git du membre, son niveau et le groupe qui l'accorde.

Une modification s'applique la prochaine fois que le membre se connecte à Git ou ouvre l'onglet **Git**. Désactiver ou retirer un membre bloque son compte Git, y compris ses jetons et ses clés SSH, et le réactiver le débloque. Le personnel du support PlaidCloud dispose automatiquement de l'accès administrateur.

## Contenu de cette section

- [Dépôts](/fr/guides/git/repositories/) : créez un dépôt, puis clonez, validez et poussez votre travail
- [Tickets](/fr/guides/git/issues/) : suivez les tâches, les bogues et les idées avec des libellés, des jalons et des responsables
- [Pull requests](/fr/guides/git/pull-requests/) : proposez des modifications sur une branche et faites-les relire avant la fusion
- [Tableaux de projet](/fr/guides/git/projects/) : organisez les tickets et les pull requests sur un tableau Kanban
- [Versions et tags](/fr/guides/git/releases-and-tags/) : repérez et publiez des instantanés versionnés d'un dépôt
- [Wikis](/fr/guides/git/wikis/) : conservez une documentation détaillée à côté de votre code
- [Paquets](/fr/guides/git/packages/) : publiez et installez des artefacts de build depuis le registre du dépôt
- [Recherche de code](/fr/guides/git/searching-code/) : trouvez du code, des tickets et des pull requests dans vos dépôts

## Voir aussi

- [Déployer une application Panel depuis PlaidCloud Git](/fr/guides/panel-apps/deploy-from-git/) : diffusez une application HoloViz Panel directement depuis un dépôt, avec une connexion gérée sans identifiants
- [Déployer une application Dash depuis PlaidCloud Git](/fr/guides/dash-apps/deploy-from-git/) : diffusez de la même manière une application Plotly Dash
- [Gestion des accès](/fr/administration/access/) : comment l'appartenance à l'espace de travail et les groupes de sécurité déterminent qui peut voir et modifier les dépôts
