---
title: Se connecter à PlaidXL
description: Connectez PlaidXL à votre espace de travail PlaidCloud avec votre adresse e-mail et votre connexion habituelle, y compris l'authentification unique et l'authentification à deux facteurs, puis déconnectez-vous ou changez d'espace de travail.
sidebar:
  label: Connexion
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL vous connecte sous votre propre identité, avec la même connexion que celle que vous utilisez pour PlaidCloud dans un navigateur. Il n'y a aucune adresse de serveur à saisir et aucun mot de passe n'est stocké dans le classeur.

## Se connecter

1. Ouvrez le volet des tâches : **PlaidCloud → Open PlaidXL**, ou **Compte** dans le groupe **Connecter**.
2. Sous **Enter your email**, saisissez l'adresse e-mail que vous utilisez pour PlaidCloud et cliquez sur **Sign In**. PlaidXL mémorise l'adresse pour la prochaine fois.
3. Si votre adresse e-mail appartient à plusieurs espaces de travail, choisissez-en un dans **Select a workspace** et cliquez sur **Sign In**. PlaidXL mémorise votre choix. Si vous appartenez à un seul espace de travail, PlaidXL le sélectionne pour vous. Si aucun espace de travail n'est lié à l'adresse e-mail, le volet l'indique ; vérifiez l'adresse et réessayez.
4. Excel demande s'il faut autoriser une fenêtre contextuelle. Autorisez-la.
5. Dans la fenêtre contextuelle, connectez-vous comme d'habitude :
   - **PlaidCloud sign-in** — votre adresse e-mail, votre mot de passe et, le cas échéant, le code à deux facteurs que vous avez configuré.
   - **Single sign-on** — si vous êtes déjà connecté à votre organisation, cette étape se déroule automatiquement. Sinon, la page de connexion de votre organisation s'ouvre d'abord.
6. Lorsque la fenêtre contextuelle affiche **Authenticated successfully**, fermez-la si elle ne s'est pas fermée d'elle-même.

L'en-tête du volet des tâches affiche maintenant votre espace de travail et le projet lié au classeur, avec votre menu de compte à côté. Poursuivez avec [Travailler avec les tables et les dimensions](/fr/reference/cli/plaidxl/retrieve/).

Pour configurer l'authentification à deux facteurs ou l'authentification unique pour votre compte, consultez [Authentification des membres](/fr/administration/access/member-authentication/).

### Se connecter avec votre compte Office

Si vous êtes connecté à Office avec un compte professionnel Microsoft Entra ID et que PlaidXL n'a aucune connexion enregistrée, il trouve vos espaces de travail à partir de ce compte, ce qui vous évite de saisir votre adresse e-mail :

- **Un seul espace de travail** — PlaidXL commence à vous y connecter. Autorisez la fenêtre contextuelle si Excel le demande ; avec l'authentification unique, la connexion se fait automatiquement. Dans Excel sur le web, cliquez d'abord sur **Continue as** suivi de votre compte.
- **Plusieurs espaces de travail** — si le classeur a été utilisé en dernier avec l'un d'eux, PlaidXL vous connecte à celui-ci. Sinon, choisissez-en un dans **Select a workspace**.
- **Aucun espace de travail** — l'écran de l'adresse e-mail s'ouvre avec votre adresse déjà renseignée.

Si vous vous connectez avec une adresse e-mail différente de celle de votre compte Office, PlaidXL indique laquelle. Après avoir cliqué sur **Log out**, PlaidXL attend que vous vous connectiez vous-même.

### Commandes avant la connexion

Vous pouvez cliquer sur n'importe quelle commande PlaidXL du ruban avant de vous être connecté. PlaidXL ouvre le volet des tâches pour vous connecter ou pour choisir un projet, puis exécute la commande sur la cellule d'où vous êtes parti.

## Rester connecté

PlaidXL vous maintient connecté sur cet ordinateur et renouvelle votre connexion en arrière-plan pendant que vous travaillez. Lorsque vous ouvrez le volet des tâches lors d'une session ultérieure, il affiche directement vos projets. Si votre connexion a complètement expiré, PlaidXL vous redemande votre adresse e-mail. Un bref problème réseau pendant le renouvellement de votre connexion ne vous déconnecte pas ; PlaidXL réessaie.

## Ce que vous pouvez voir

PlaidXL lit les données avec vos autorisations. Vous voyez les projets que vous pouvez ouvrir dans PlaidCloud, ainsi que les tables et les dimensions qu'ils contiennent, et rien de plus. Si un projet ou une table est absent, demandez l'accès à un propriétaire du projet. Consultez [Organisations et espaces de travail expliqués](/fr/administration/access/overview/organizations-and-workspaces-explained/) pour comprendre comment fonctionne l'appartenance à un espace de travail.

## Se déconnecter ou changer d'espace de travail

Cliquez sur le menu de compte (les trois points) en haut à droite du volet des tâches. Il affiche votre nom et votre espace de travail, avec trois commandes :

- **Keyboard shortcuts** répertorie les raccourcis PlaidXL afin que vous puissiez les modifier. Consultez [Raccourcis clavier](/fr/reference/cli/plaidxl/ribbon/#raccourcis-clavier).
- **Switch workspace** vous déconnecte et revient à l'écran de l'adresse e-mail, afin que vous puissiez choisir un autre espace de travail sous **Select a workspace**.
- **Log out** efface votre connexion et revient à l'écran de l'adresse e-mail.

Votre connexion est partagée par tous les classeurs que vous avez ouverts, mais chaque classeur conserve son propre projet. Le projet d'un classeur appartient à un espace de travail ; après un changement d'espace de travail, un classeur lié à un projet de l'ancien espace de travail n'a plus de projet tant que vous n'en choisissez pas un. Consultez [Le projet appartient au classeur](/fr/reference/cli/plaidxl/retrieve/#le-projet-appartient-au-classeur).

## Thème clair et thème sombre

Le volet des tâches suit votre thème Office et change lorsque vous changez de thème.

## Clavier et lecteurs d'écran

Les lignes des listes de projets, de tables et de dimensions prennent le focus du clavier et répondent aux touches **Entrée** et **Espace**. Un lecteur d'écran annonce la ligne sélectionnée, et les états sélectionné et avertissement sont signalés par une icône en plus de la couleur.

## Voir aussi

- [Installer PlaidXL](/fr/reference/cli/plaidxl/install/) — ajoutez le complément et ouvrez le volet des tâches
- [Dépannage](/fr/reference/cli/plaidxl/troubleshooting/) — lorsque la fenêtre contextuelle de connexion ne s'ouvre pas ou qu'un espace de travail est introuvable
- [Afficher et gérer les espaces de travail](/fr/administration/access/overview/viewing-and-managing-workspaces/) — les espaces de travail auxquels vous appartenez
