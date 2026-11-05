---
title: PlaidCloud Git
description: Hébergez, versionnez et collaborez sur des dépôts Git dans PlaidCloud — avec tickets, demandes de fusion, tableaux de projet, versions et wikis, et une authentification unique intégrée.
sidebar:
  label: Vue d'ensemble
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git est un service Git privé intégré à votre espace de travail. Chaque espace de travail dispose de son propre serveur Git pour stocker du code, de la configuration, des notebooks et tout autre fichier versionné — ainsi que les tickets, les demandes de fusion et les tableaux de projet que votre équipe utilise pour collaborer dessus.

Vous vous connectez avec votre compte PlaidCloud ; il n'y a donc ni nom d'utilisateur ni mot de passe distinct à configurer. Les nouveaux dépôts sont privés par défaut, visibles uniquement par les membres auxquels vous accordez l'accès.

## Ouvrir Git

Sélectionnez **Git** dans la liste des applications de votre espace de travail. L'onglet **Git** affiche les dépôts de votre espace de travail avec, pour chacun, son nom, sa description, sa branche par défaut et sa dernière date de mise à jour, et une ligne en haut indique ce que vous pouvez faire. Sélectionnez un dépôt pour l'ouvrir, ou **View all in Git** pour accéder à l'interface web de Git. Utilisez **← Back to** votre espace de travail dans Git pour revenir à PlaidCloud.

Pour cloner un dépôt, sélectionnez **Copy clone URL** sur sa ligne. La première fois, une astuce indique ce dont vous avez besoin :

1. Git doit être installé sur votre ordinateur.
2. Créez un jeton d'accès dans Git sous **Paramètres → Applications**, avec l'autorisation **write:repository**. L'astuce renvoie vers cette page.
3. Lorsque Git demande un mot de passe, collez le jeton, et non votre mot de passe PlaidCloud.
4. Exécutez les deux commandes `git config --global user.name` et `user.email` affichées, qui contiennent déjà votre nom et votre adresse e-mail.

Consultez [Dépôts](/fr/guides/git/repositories/) pour la procédure complète. Si vous ne pouvez pas copier d'URL de clonage, vous avez l'accès Lecture ; voir ci-dessous.

## Niveaux d'accès

Toute personne ayant accès à Git peut lire les dépôts partagés de l'espace de travail. Deux niveaux supplémentaires permettent d'envoyer du code.

| Niveau | Ce que vous pouvez faire | Accordé par |
|---|---|---|
| **Lecture** | Consulter et cloner les dépôts partagés. | Par défaut pour chaque membre. |
| **Contributeur** | Tout ce que permet Lecture, et envoyer du code vers le dépôt `apps`, où se trouve le code des applications [Panel](/fr/guides/panel-apps/deploy-from-git/) et [Dash](/fr/guides/dash-apps/deploy-from-git/). | Le groupe de sécurité **Git Contributors**. |
| **Administrateur** | Tout ce que permet Contributeur, et envoyer du code vers tous les dépôts, y compris `udfs`, et créer des organisations. | Le groupe de sécurité **Git Administration**. |

Le dépôt `udfs` est réservé aux administrateurs, car les fonctions définies par l'utilisateur s'exécutent sous l'identité du workflow qui les appelle.

Si vous avez l'accès Lecture, l'onglet **Git** indique jusqu'à trois administrateurs de l'espace de travail auxquels vous pouvez demander de vous ajouter à **Git Contributors**.

## Git depuis les applications et les UDF

La fenêtre d'une application Panel ou Dash comporte une section **Dépôt** qui indique son dépôt, sa branche et l'état de sa construction, avec **Edit in browser** et **Copy clone URL** pour les membres qui peuvent envoyer du code. La barre d'outils d'une UDF basée sur Git comporte **Open**, qui ouvre le dépôt sur sa branche dans Git,, et **Edit in browser** pour les administrateurs.

## Accorder l'accès à Git

Les administrateurs de l'espace de travail accordent l'accès dans **Identité** en ajoutant des membres à un groupe de sécurité, ou en ajoutant l'autorisation à un groupe qui leur est propre.

1. Ajoutez le membre à **Git Contributors** pour lui permettre d'envoyer du code d'application, ou à **Git Administration** pour en faire un administrateur Git.
2. Pour donner à chaque nouveau membre le droit d'envoyer du code d'application, ajoutez **Git Contributors** à vos groupes par défaut. **Git Administration** ne peut pas être un groupe par défaut.
3. Pour vérifier ce qu'un membre peut faire, ouvrez le membre et sélectionnez l'onglet **Git**. Il affiche le nom d'utilisateur Git du membre, son niveau et le groupe qui l'accorde.

Une modification s'applique à la prochaine connexion du membre à Git ou à l'ouverture de l'onglet **Git**. Le personnel du support PlaidCloud dispose automatiquement de l'accès Administrateur.

## Contenu de cette section

- [Dépôts](/fr/guides/git/repositories/) — créez un dépôt, puis clonez, validez et envoyez votre travail
- [Tickets](/fr/guides/git/issues/) — suivez les tâches, les bogues et les idées avec des libellés, des jalons et des responsables
- [Demandes de fusion](/fr/guides/git/pull-requests/) — proposez des modifications sur une branche et faites-les relire avant leur fusion
- [Tableaux de projet](/fr/guides/git/projects/) — organisez les tickets et les demandes de fusion sur un tableau Kanban
- [Versions et balises](/fr/guides/git/releases-and-tags/) — marquez et publiez des instantanés versionnés d'un dépôt
- [Wikis](/fr/guides/git/wikis/) — conservez une documentation détaillée à côté de votre code
- [Paquets](/fr/guides/git/packages/) — publiez et installez des artefacts de build depuis le registre du dépôt
- [Rechercher du code](/fr/guides/git/searching-code/) — trouvez du code, des tickets et des demandes de fusion dans vos dépôts

## Voir aussi

- [Déployer une application Panel depuis PlaidCloud Git](/fr/guides/panel-apps/deploy-from-git/) — diffusez une application HoloViz Panel directement depuis un dépôt, avec une connexion gérée sans identifiants
- [Déployer une application Dash depuis PlaidCloud Git](/fr/guides/dash-apps/deploy-from-git/) — diffusez une application Plotly Dash de la même manière
- [Gestion des accès](/fr/administration/access/) — comment l'appartenance à l'espace de travail et les groupes de sécurité déterminent qui peut voir et modifier les dépôts
