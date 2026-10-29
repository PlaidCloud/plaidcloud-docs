---
title: Notify via Slack
description: Envoyez des notifications Slack depuis une étape de workflow PlaidCloud pour alerter des canaux ou des utilisateurs des événements, des erreurs et de l'état d'un workflow.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-slack.md
---

L'ajout de notifications Slack depuis un workflow se déroule en deux parties :


1. Créer une connexion externe Slack Webhook
2. Ajouter des étapes de notification Slack à vos workflows

## Ajouter une étape de notification Slack à un workflow


L'ajout d'étapes de notification Slack à un workflow se fait comme pour n'importe quelle autre étape. Après avoir ajouté l'étape, ouvrez sa configuration, renseignez le formulaire et enregistrez-le. Vous pouvez alors tester votre notification Slack.



## Joindre un fichier

Choisissez un document dans **Fichier à téléverser** pour l'envoyer au canal, le message lui servant de commentaire. Un webhook ne peut pas transporter de fichier : une pièce jointe passe donc par un jeton de bot sur la connexion Slack :

- Ajoutez un **Jeton de bot** à la connexion. Il s'agit du jeton `xoxb-` d'une application Slack disposant de la portée `files:write`, et l'application doit être invitée dans le canal.
- Saisissez l'**ID du canal** dans l'étape, par exemple `C0123ABCD`, et non un nom de canal. Le téléversement de fichiers de Slack n'accepte que des ID, et l'étape échoue sans cela. Pour trouver un ID, ouvrez les détails du canal dans Slack et faites défiler jusqu'en bas.
- Si le document est introuvable, le message est envoyé par webhook sans lui, et l'étape émet un avertissement indiquant le chemin du document.

## Mise en forme du message Slack


Slack offre de nombreuses options de mise en forme, notamment l'ajout d'images et la mention d'utilisateurs. Consultez la documentation [Slack Text Formatting](https://api.slack.com/reference/surfaces/formatting) pour plus de détails.



## Créer une connexion externe Slack Webhook


Il s'agit d'une configuration à effectuer une seule fois, qui permet à PlaidCloud d'envoyer des notifications Slack en votre nom. Slack permet de créer une application Webhook (un moyen générique d'envoyer une notification sur Internet). Après avoir créé l'application Webhook dans Slack, ajoutez les identifiants fournis à PlaidCloud pour pouvoir l'utiliser.



### Création de l'application Slack Webhook


Ces étapes doivent être effectuées par un administrateur Slack. Suivez ces étapes pour créer une application Slack Webhook :


1. Dans Slack, ouvrez le menu de contrôle de l'espace de travail et sélectionnez `Settings & administration > Manage Apps`
2. Sélectionnez `Custom Integrations` dans la liste des catégories d'applications
3. Sélectionnez `Incoming Webhooks` dans la liste des applications
4. Sélectionnez le bouton `Add to Slack`
5. Sur l'écran suivant, sélectionnez le canal Slack dans lequel vous souhaitez publier les messages, puis poursuivez. Il s'agit du canal par défaut, mais il peut être remplacé dans chaque notification, y compris pour envoyer des messages privés à des personnes précises.
6. Copiez l'URL du webhook affichée. Elle servira plus tard : conservez-la en lieu sûr. Elle ressemble à ceci : `https://hooks.slack.com/services/T04QZ1435/G02TGBFTOP8/K9GZrR2ThdJz1uSiL9YeZxoR`
7. Vous pouvez personnaliser l'apparence, le nom et l'émoji avant d'enregistrer. Ces personnalisations ne sont que des valeurs par défaut et peuvent être remplacées dans chaque étape de notification d'un workflow PlaidCloud.

### Configuration de la connexion externe PlaidCloud


Ces étapes doivent être effectuées par un administrateur de l'espace de travail PlaidCloud disposant des autorisations nécessaires pour créer des connexions de données externes. Suivez ces étapes pour créer la connexion :


1. Accédez à `Analyze > Tools > External Data Connections`
2. Sous la sélection `+ New Connection`, choisissez Slack Webhook
3. Renseignez le nom, la description, et collez l'URL du webhook fournie à l'étape 6 ci-dessus. Le nom indiqué ici s'affiche comme choix dans l'étape de workflow ; il doit donc être aussi descriptif que possible. Toute personne détenant l'URL peut publier dans votre canal : le champ **URL du webhook** la masque donc au moment où vous la collez et s'affiche vide lorsque vous rouvrez la connexion ; laissez-le vide pour conserver l'URL enregistrée.
4. Pour envoyer des pièces jointes, collez également le jeton de bot de l'application Slack dans le champ **Jeton de bot (pour le téléversement de fichiers)**. Une connexion peut contenir l'URL du webhook, le jeton de bot, ou les deux. Le jeton de bot est masqué comme l'URL du webhook et s'affiche vide lorsque vous rouvrez la connexion.
5. Sélectionnez le bouton `+ Create`


## Exemples

Aucun exemple pour le moment...
