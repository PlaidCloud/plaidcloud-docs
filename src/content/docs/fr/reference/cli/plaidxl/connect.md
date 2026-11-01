---
title: Se connecter à PlaidXL
description: Connectez PlaidXL à votre espace de travail PlaidCloud avec votre e-mail et votre méthode de connexion habituelle, y compris l'authentification unique et l'authentification à deux facteurs, puis déconnectez-vous ou changez d'espace de travail.
sidebar:
  label: Connexion
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL vous connecte sous votre propre identité, avec la même connexion que celle que vous utilisez pour PlaidCloud dans un navigateur. Il n'y a pas d'adresse de serveur à saisir, et aucun mot de passe n'est stocké dans le classeur.

## Se connecter

1. Ouvrez le volet des tâches§N: **PlaidCloud → Open PlaidXL**.
2. Sous **Enter your email**, saisissez l'adresse e-mail que vous utilisez pour PlaidCloud et cliquez sur **Sign In**. PlaidXL mémorise l'adresse pour la prochaine fois.
3. Si votre e-mail appartient à plusieurs espaces de travail, choisissez-en un dans **Select a workspace** et cliquez sur **Sign In**. PlaidXL mémorise votre choix. Si vous appartenez à un seul espace de travail, PlaidXL le sélectionne pour vous. Si aucun espace de travail n'est associé à l'e-mail, le volet l'indique§T; vérifiez l'adresse et réessayez.
4. Excel vous demande s'il faut autoriser une fenêtre contextuelle. Autorisez-la.
5. Dans la fenêtre contextuelle, connectez-vous comme d'habitude§N:
   - **Connexion PlaidCloud** — votre e-mail, votre mot de passe et, le cas échéant, le code à deux facteurs que vous avez configuré.
   - **Authentification unique** — si vous êtes déjà connecté à votre organisation, cette étape se déroule automatiquement. Sinon, la page de connexion de votre organisation s'ouvre d'abord.
6. Lorsque la fenêtre contextuelle affiche **Authenticated successfully**, fermez-la si elle ne s'est pas fermée d'elle-même.

L'en-tête du volet des tâches affiche maintenant votre espace de travail et le projet associé au classeur, avec le menu de votre compte à côté. Poursuivez avec [Travailler avec les tables et les dimensions](/fr/reference/cli/plaidxl/retrieve/).

Pour configurer l'authentification à deux facteurs ou l'authentification unique pour votre compte, consultez [Authentification des membres](/fr/administration/access/member-authentication/).

## Rester connecté

PlaidXL vous garde connecté sur cet ordinateur et renouvelle votre connexion en arrière-plan pendant que vous travaillez. Lorsque vous ouvrez le volet des tâches lors d'une session ultérieure, il affiche directement vos projets. Si votre connexion a complètement expiré, PlaidXL vous redemande votre e-mail. Un bref problème réseau pendant le renouvellement de votre connexion ne vous déconnecte pas§T; PlaidXL réessaie.

## Ce que vous pouvez voir

PlaidXL lit les données avec vos autorisations. Vous voyez les projets que vous pouvez ouvrir dans PlaidCloud, ainsi que les tables et les dimensions qu'ils contiennent, et rien de plus. Si un projet ou une table est absent, demandez l'accès à un propriétaire du projet. Consultez [Les organisations et les espaces de travail expliqués](/fr/administration/access/overview/organizations-and-workspaces-explained/) pour comprendre le fonctionnement de l'appartenance à un espace de travail.

## Se déconnecter ou changer d'espace de travail

Cliquez sur le menu du compte (les trois points) en haut à droite du volet des tâches. Il affiche votre nom et votre espace de travail, avec deux commandes§N:

- **Log out** efface votre connexion et revient à l'écran de saisie de l'e-mail.
- **Switch workspace** vous déconnecte et revient à l'écran de saisie de l'e-mail, afin que vous puissiez choisir un autre espace de travail sous **Select a workspace**.

Votre connexion est partagée par tous les classeurs que vous avez ouverts, mais chaque classeur conserve son propre projet. Le projet d'un classeur appartient à un espace de travail§T; après un changement, un classeur lié à un projet de l'ancien espace de travail n'a donc plus de projet tant que vous n'en choisissez pas un. Consultez [Le projet appartient au classeur](/fr/reference/cli/plaidxl/retrieve/#le-projet-appartient-au-classeur).

## Thème clair et thème sombre

Le volet des tâches suit votre thème Office et change lorsque vous le changez.

## Clavier et lecteurs d'écran

Les lignes des listes de projets, de tables et de dimensions prennent le focus du clavier et répondent aux touches **Entrée** et **Espace**. Un lecteur d'écran annonce la ligne sélectionnée, et les états sélectionné et avertissement comportent une icône en plus d'une couleur.

## Voir aussi

- [Installer PlaidXL](/fr/reference/cli/plaidxl/install/) — ajouter le complément et ouvrir le volet des tâches
- [Dépannage](/fr/reference/cli/plaidxl/troubleshooting/) — lorsque la fenêtre de connexion ne s'ouvre pas ou qu'un espace de travail est absent
- [Afficher et gérer les espaces de travail](/fr/administration/access/overview/viewing-and-managing-workspaces/) — les espaces de travail auxquels vous appartenez
