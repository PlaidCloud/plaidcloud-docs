---
title: Se connecter à PlaidXL
description: Connectez PlaidXL à votre espace de travail PlaidCloud avec votre e-mail et votre méthode de connexion habituelle, y compris l'authentification unique et l'authentification à deux facteurs, puis déconnectez-vous ou changez d'espace de travail.
sidebar:
  label: Connexion
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL vous connecte sous votre propre identité, avec la même connexion que celle que vous utilisez pour PlaidCloud dans un navigateur. Aucune adresse de serveur à saisir et aucun mot de passe stocké dans le classeur.

## Se connecter

1. Ouvrez le volet des tâches : **PlaidCloud → Open PlaidXL**, ou **Compte** dans le groupe **Connecter**.
2. Sous **Enter your email**, saisissez l'adresse e-mail que vous utilisez pour PlaidCloud et cliquez sur **Sign In**. PlaidXL mémorise l'adresse pour la prochaine fois.
3. Si votre e-mail appartient à plusieurs espaces de travail, choisissez-en un dans **Select a workspace** et cliquez sur **Sign In**. PlaidXL mémorise votre choix. Si vous appartenez à un seul espace de travail, PlaidXL le sélectionne pour vous. Si aucun espace de travail n'est lié à l'e-mail, le volet l'indique ; vérifiez l'adresse et réessayez.
4. Excel demande s'il faut autoriser une fenêtre contextuelle. Autorisez-la.
5. Dans la fenêtre contextuelle, connectez-vous comme d'habitude :
   - **PlaidCloud sign-in** — votre e-mail, votre mot de passe et, le cas échéant, le code d'authentification à deux facteurs que vous avez configuré.
   - **Single sign-on** — si vous êtes déjà connecté à votre organisation, cette étape se déroule automatiquement. Sinon, la page de connexion de votre organisation s'ouvre d'abord.
6. Lorsque la fenêtre contextuelle affiche **Authenticated successfully**, fermez-la si elle ne s'est pas fermée d'elle-même.

L'en-tête du volet des tâches affiche maintenant votre espace de travail et le projet lié au classeur, avec votre menu de compte à côté. Poursuivez avec [Travailler avec les tables et les dimensions](/fr/reference/cli/plaidxl/retrieve/).

Pour configurer l'authentification à deux facteurs ou l'authentification unique pour votre compte, consultez [Authentification des membres](/fr/administration/access/member-authentication/).

### Se connecter avec votre compte Office

Si vous êtes connecté à Office avec un compte professionnel Microsoft Entra ID et que PlaidXL n'a aucune connexion enregistrée, il retrouve vos espaces de travail à partir de ce compte, sans que vous ayez à saisir votre e-mail :

- **Un seul espace de travail** — PlaidXL commence à vous y connecter. Autorisez la fenêtre contextuelle si Excel le demande ; avec l'authentification unique, l'étape se déroule automatiquement. Dans Excel sur le web, cliquez d'abord sur **Continue as** suivi de votre compte.
- **Plusieurs espaces de travail** — si le classeur a été utilisé en dernier avec l'un d'eux, PlaidXL vous connecte à celui-ci. Sinon, choisissez-en un dans **Select a workspace**.
- **Aucun espace de travail** — l'écran de saisie de l'e-mail s'ouvre avec votre adresse déjà renseignée.

Si vous vous connectez avec un e-mail différent de celui de votre compte Office, PlaidXL indique lequel. Après avoir cliqué sur **Log out**, PlaidXL attend que vous vous connectiez vous-même.

### Commandes avant la connexion

Vous pouvez cliquer sur n'importe quelle commande PlaidXL du ruban avant de vous être connecté. PlaidXL ouvre le volet des tâches pour vous connecter, ou pour choisir un projet, puis exécute la commande sur la cellule d'où vous êtes parti.

## Rester connecté

PlaidXL vous garde connecté sur cet ordinateur et renouvelle votre connexion en arrière-plan pendant que vous travaillez. Lorsque vous ouvrez le volet des tâches lors d'une session ultérieure, il affiche directement vos projets. Si votre connexion a complètement expiré, PlaidXL vous redemande votre e-mail. Un bref problème réseau pendant le renouvellement de votre connexion ne vous déconnecte pas ; PlaidXL réessaie.

## Ce que vous pouvez voir

PlaidXL lit les données avec vos autorisations. Vous voyez les projets que vous pouvez ouvrir dans PlaidCloud, ainsi que les tables et les dimensions qu'ils contiennent, et rien de plus. Si un projet ou une table est absent, demandez l'accès à un propriétaire du projet. Consultez [Présentation des organisations et des espaces de travail](/fr/administration/access/overview/organizations-and-workspaces-explained/) pour comprendre le fonctionnement de l'appartenance à un espace de travail.

## Se déconnecter ou changer d'espace de travail

Cliquez sur le menu du compte (les trois points) en haut à droite du volet des tâches. Il affiche votre nom et votre espace de travail, avec trois commandes :

- **Keyboard shortcuts** répertorie les raccourcis PlaidXL afin que vous puissiez les modifier. Consultez [Raccourcis clavier](/fr/reference/cli/plaidxl/ribbon/#raccourcis-clavier).
- **Switch workspace** vous déconnecte et revient à l'écran de saisie de l'e-mail, afin que vous puissiez choisir un autre espace de travail sous **Select a workspace**. Connectez-vous au nouvel espace de travail lorsque vous y êtes invité. Revenir à un espace de travail auquel vous vous êtes déjà connecté ne demande aucune nouvelle connexion, et l'annulation de la connexion vous maintient dans l'espace de travail actuel.
- **Log out** efface votre connexion et revient à l'écran de saisie de l'e-mail.

Chaque connexion ne fonctionne que pour l'espace de travail dans lequel elle a été établie. Tout le monde se connecte une fois après ce changement. Lorsque vous êtes déconnecté, **Enregistrer** affiche **Sign in to PlaidCloud to save.** et la récupération d'une dimension affiche **Sign in to PlaidCloud to retrieve a dimension.**

Votre connexion est partagée par tous les classeurs que vous avez ouverts, mais chaque classeur conserve son propre projet. Le projet d'un classeur appartient à un espace de travail : après un changement d'espace de travail, un classeur lié à un projet de l'ancien espace de travail n'a plus de projet tant que vous n'en choisissez pas un. Consultez [Le projet appartient au classeur](/fr/reference/cli/plaidxl/retrieve/#le-projet-appartient-au-classeur).

## Thème clair et sombre

Le volet des tâches reprend l'apparence de l'application web PlaidCloud, avec le bleu de la marque, des onglets et des listes de type rail, et des tables, dimensions, projets et colonnes présentés dans des cartes défilantes délimitées. Il suit votre thème Office et change lorsque vous le changez. Dans un volet étroit, les onglets s'affichent sur deux rangées de trois ; à partir de 560 pixels de large, ils tiennent sur une seule rangée.

## Clavier et lecteurs d'écran

Les lignes des listes de projets, de tables et de dimensions prennent le focus clavier et réagissent aux touches **Enter** et **Space**. Une ligne sélectionnée est annoncée par un lecteur d'écran, les états sélectionné et avertissement s'accompagnent d'une icône en plus d'une couleur, et le contrôle qui a le focus clavier affiche un anneau de focus bien visible.

## Nombres

Tous les nombres affichés dans le volet des tâches, tels que les nombres de lignes et de colonnes, et les messages d'actualisation, de recalcul, d'Explain, de Formulas, de Report et de planification, suivent la langue d'affichage d'Excel. Excel en allemand affiche par exemple 4.812.233. Les valeurs écrites dans les cellules ne changent pas.

## Voir aussi

- [Installer PlaidXL](/fr/reference/cli/plaidxl/install/) — ajouter le complément et ouvrir le volet des tâches
- [Dépannage](/fr/reference/cli/plaidxl/troubleshooting/) — lorsque la fenêtre contextuelle de connexion ne s'ouvre pas ou qu'un espace de travail est introuvable
- [Afficher et gérer les espaces de travail](/fr/administration/access/overview/viewing-and-managing-workspaces/) — les espaces de travail auxquels vous appartenez
