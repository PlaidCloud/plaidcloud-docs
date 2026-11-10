---
title: PlaidCloud Git
description: Hébergez, versionnez et collaborez sur des dépôts Git dans PlaidCloud, avec tickets, demandes de fusion, tableaux de projet, versions et wikis, et authentification unique intégrée.
sidebar:
  label: Vue d'ensemble
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

PlaidCloud Git est un service Git privé intégré à votre espace de travail. Chaque espace de travail dispose de son propre serveur Git pour stocker du code, de la configuration, des notebooks et tout autre fichier versionné, ainsi que les tickets, les demandes de fusion et les tableaux de projet que votre équipe utilise pour collaborer dessus.

Vous vous connectez avec votre compte PlaidCloud, il n'y a donc ni nom d'utilisateur ni mot de passe distincts à configurer. Les nouveaux dépôts sont privés par défaut et visibles uniquement des membres auxquels vous accordez l'accès.

## Ouvrir Git

Sélectionnez **Git** dans la liste des applications de votre espace de travail. L'onglet **Git** s'ouvre avec l'hôte de l'espace de travail, votre rôle et une liste **Repositories**. Utilisez **View all in Git** pour accéder à l'interface web de Git, **Manage who can push** (si vous pouvez gérer les groupes) pour ouvrir la gestion des groupes, et le bouton d'actualisation pour recharger la page. Utilisez **← Back to** your workspace in Git pour revenir à PlaidCloud.

Un indicateur de rôle affiche votre niveau : **Administrateur**, **Contributeur** ou **Lecteur**, avec une ligne indiquant ce que cela vous permet de faire. Chaque ligne de dépôt affiche son nom, sa description (lorsqu'il en a une), **Mis à jour** avec la date, un champ de clonage en lecture seule avec un bouton de copie, et **Ouvrir**, qui ouvre le dépôt dans Git. Les dépôts que vous créez en privé se trouvent directement dans Git, pas dans cette liste.

Si Git n'est pas configuré pour votre espace de travail ou est inaccessible, l'onglet **Git** affiche **Git n’est pas disponible** avec le motif, et **Réessayer** relance la vérification.

## Cloner un dépôt

Copiez l'adresse de clonage du dépôt depuis sa ligne. La première fois que vous copiez, une carte **Set up Git on your computer** apparaît avec les étapes ci-dessous. Sélectionnez **Ignorer** pour la masquer, et **How to clone** dans l'en-tête pour la faire réapparaître.

1. Git doit être installé sur votre ordinateur.
2. Créez un jeton dans **Paramètres → Applications** avec l'autorisation **write:repository**. La carte renvoie vers cette page.
3. Indiquez à Git qui vous êtes à l'aide des deux commandes `git config --global user.name` et `user.email` affichées, qui contiennent déjà votre nom et votre adresse e-mail.
4. Clonez le dépôt avec la commande `git clone` affichée. Lorsque Git demande un mot de passe, collez ce jeton, et non votre mot de passe PlaidCloud.

Chaque commande a son propre bouton de copie. Consultez [Dépôts](/fr/guides/git/repositories/) pour la procédure complète. La copie nécessite un accès en écriture (push) et un compte Git activé : si le bouton de copie est désactivé, ouvrez n'importe quel dépôt une fois pour activer votre compte ou, en tant que **Lecteur**, demandez un accès en écriture comme décrit ci-dessous.

## Niveaux d'accès

Toute personne ayant accès à Git peut lire les dépôts partagés de l'espace de travail. Deux niveaux supplémentaires permettent d'effectuer des push.

| Rôle | Ce que vous pouvez faire | Accordé par |
|---|---|---|
| **Lecteur** | Afficher et cloner les dépôts partagés. | Par défaut pour chaque membre. |
| **Contributeur** | Tout ce que permet la lecture, et effectuer des push vers le dépôt `apps`, où se trouve le code des applications [Panel](/fr/guides/panel-apps/deploy-from-git/) et [Dash](/fr/guides/dash-apps/deploy-from-git/). | Le groupe de sécurité **Git Contributors**. |
| **Administrateur** | Tout ce que permet Contributeur, et effectuer des push vers tous les dépôts, y compris `udfs`, et créer des organisations. | Le groupe de sécurité **Git Administration**. |

Le dépôt `udfs` est réservé aux administrateurs, car les fonctions définies par l'utilisateur s'exécutent sous l'identité du workflow qui les appelle.

Si vous êtes **Lecteur**, l'onglet **Git** nomme jusqu'à trois administrateurs de l'espace de travail à qui vous pouvez demander de vous ajouter à **Git Contributors**.

## Git depuis les applications et les UDF

La fenêtre d'une application Panel ou Dash comporte une section **Dépôt** qui affiche son dépôt, sa branche et l'état de la compilation, avec **Edit in browser** et **Copy clone URL** pour les membres qui peuvent effectuer des push. La barre d'outils d'une UDF adossée à Git comporte **Ouvrir**, qui ouvre le dépôt à sa branche dans Git, et **Edit in browser** pour les administrateurs.

## Accorder l'accès à Git

Les administrateurs de l'espace de travail accordent l'accès dans **Identité** en ajoutant des membres à un groupe de sécurité, ou en ajoutant l'autorisation à un groupe qui vous est propre.

1. Ajoutez le membre à **Git Contributors** pour lui permettre d'effectuer des push de code d'application, ou à **Git Administration** pour en faire un administrateur Git.
2. Pour donner à chaque nouveau membre un accès en écriture au code d'application, ajoutez **Git Contributors** à vos groupes par défaut. **Git Administration** ne peut pas être un groupe par défaut.
3. Pour vérifier ce qu'un membre peut faire, ouvrez le membre et sélectionnez l'onglet **Git**. Il affiche le nom d'utilisateur Git du membre, son niveau et le groupe qui l'accorde.

Une modification s'applique la prochaine fois que le membre se connecte à Git ou ouvre l'onglet **Git**. Le compte Git d'un membre suit son appartenance à PlaidCloud. Désactiver ou supprimer un membre bloque son compte Git, y compris ses jetons et ses clés SSH, en une heure environ, et le réactiver le débloque. Rien n'est supprimé : ses dépôts et son historique sont conservés. Se connecter à Git par authentification unique ouvre le compte propre du membre. Le personnel du support PlaidCloud dispose automatiquement d'un accès administrateur.

## Contenu de cette section

- [Dépôts](/fr/guides/git/repositories/) : créez un dépôt, puis clonez, validez et envoyez votre travail
- [Tickets](/fr/guides/git/issues/) : suivez les tâches, les bugs et les idées avec des étiquettes, des jalons et des responsables
- [Demandes de fusion](/fr/guides/git/pull-requests/) : proposez des modifications sur une branche et faites-les relire avant leur fusion
- [Tableaux de projet](/fr/guides/git/projects/) : organisez les tickets et les demandes de fusion sur un tableau Kanban
- [Versions et tags](/fr/guides/git/releases-and-tags/) : marquez et publiez des instantanés versionnés d'un dépôt
- [Wikis](/fr/guides/git/wikis/) : conservez une documentation détaillée à côté de votre code
- [Packages](/fr/guides/git/packages/) : publiez et installez des artefacts de compilation depuis le registre du dépôt
- [Recherche de code](/fr/guides/git/searching-code/) : trouvez du code, des tickets et des demandes de fusion dans tous vos dépôts

## Voir aussi

- [Déployer une application Panel depuis PlaidCloud Git](/fr/guides/panel-apps/deploy-from-git/) : servez une application HoloViz Panel directement depuis un dépôt, avec une connexion gérée sans identifiants
- [Déployer une application Dash depuis PlaidCloud Git](/fr/guides/dash-apps/deploy-from-git/) : servez une application Plotly Dash de la même manière
- [Gestion des accès](/fr/administration/access/) : comment l'appartenance à l'espace de travail et les groupes de sécurité déterminent qui peut voir et modifier les dépôts
