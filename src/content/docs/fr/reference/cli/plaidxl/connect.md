---
title: Se connecter à PlaidXL
description: Connectez PlaidXL à votre espace de travail PlaidCloud avec votre e-mail et votre méthode de connexion habituelle, y compris l'authentification unique et l'authentification à deux facteurs, puis déconnectez-vous ou changez d'espace de travail.
sidebar:
  label: Connexion
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL vous connecte sous votre propre identité, avec la même méthode de connexion que celle que vous utilisez pour PlaidCloud dans un navigateur. Aucune adresse de serveur n'est à saisir et aucun mot de passe n'est stocké dans le classeur.

## Se connecter

1. Ouvrez le volet des tâches : **PlaidCloud → Show Taskpane**.
2. Sous **Enter your email**, saisissez l'adresse e-mail que vous utilisez pour PlaidCloud, puis cliquez sur **Sign In**.
3. Si votre adresse e-mail appartient à plusieurs espaces de travail, choisissez-en un dans **Select a tenant**, puis cliquez sur **Sign In**. (Dans PlaidXL, un *tenant* correspond à votre espace de travail PlaidCloud.) Si vous appartenez à un seul espace de travail, PlaidXL le sélectionne pour vous.
4. Excel vous demande s'il doit autoriser une fenêtre contextuelle. Autorisez-la.
5. Dans la fenêtre contextuelle, connectez-vous de la manière habituelle :
   - **Connexion PlaidCloud** — votre e-mail, votre mot de passe et, le cas échéant, le code d'authentification à deux facteurs que vous avez configuré.
   - **Authentification unique** — si vous êtes déjà connecté à votre organisation, cette étape se déroule automatiquement. Sinon, la page de connexion de votre organisation s'ouvre d'abord.
6. Lorsque la fenêtre contextuelle affiche **Authenticated successfully**, fermez-la si elle ne s'est pas fermée d'elle-même.

Le volet des tâches affiche maintenant **Connected to** l'ID de votre espace de travail **as** votre nom d'utilisateur, avec la liste de vos projets en dessous. Poursuivez avec [Travailler avec les tables et les dimensions](/fr/reference/cli/plaidxl/retrieve/).

Pour configurer l'authentification à deux facteurs ou l'authentification unique pour votre compte, consultez [Authentification des membres](/fr/administration/access/member-authentication/).

## Rester connecté

PlaidXL vous maintient connecté sur cet ordinateur et renouvelle votre connexion en arrière-plan pendant que vous travaillez. Lorsque vous ouvrez le volet des tâches lors d'une session ultérieure, il affiche directement vos projets. Si votre connexion a complètement expiré, PlaidXL vous redemande votre adresse e-mail.

## Ce que vous pouvez voir

PlaidXL lit les données avec vos permissions. Vous voyez les projets que vous pouvez ouvrir dans PlaidCloud, ainsi que les tables et les dimensions qu'ils contiennent, et rien de plus. Si un projet ou une table est absent, demandez l'accès à un propriétaire du projet. Consultez [Organisations et espaces de travail expliqués](/fr/administration/access/overview/organizations-and-workspaces-explained/) pour comprendre le fonctionnement de l'appartenance à un espace de travail.

## Se déconnecter ou changer d'espace de travail

Cliquez sur **Logout** en haut du volet des tâches. PlaidXL efface votre connexion et revient à l'écran de saisie de l'e-mail.

Pour travailler dans un autre espace de travail, déconnectez-vous, puis reconnectez-vous et choisissez l'autre espace de travail sous **Select a tenant**. PlaidXL fonctionne avec un seul espace de travail à la fois, pour tous les classeurs que vous avez ouverts.

## Thème clair et sombre

Le volet des tâches suit le thème d'Office. Pour le fixer en clair ou en sombre, cliquez sur le bouton en forme de soleil ou de lune en haut à gauche du volet des tâches.

## Voir aussi

- [Installer PlaidXL](/fr/reference/cli/plaidxl/install/) — ajouter le complément et ouvrir le volet des tâches
- [Dépannage](/fr/reference/cli/plaidxl/troubleshooting/) — lorsque la fenêtre contextuelle de connexion ne s'ouvre pas ou qu'un espace de travail est introuvable
- [Afficher et gérer les espaces de travail](/fr/administration/access/overview/viewing-and-managing-workspaces/) — les espaces de travail auxquels vous appartenez
