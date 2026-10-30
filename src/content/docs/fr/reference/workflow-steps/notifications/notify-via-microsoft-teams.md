---
title: Notify via Microsoft Teams
description: Envoyez des notifications Microsoft Teams depuis une étape de workflow PlaidCloud pour alerter des canaux ou des utilisateurs des événements et de l'état d'un workflow.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-microsoft-teams.md
---

L'ajout de notifications Microsoft Teams depuis un workflow se déroule en deux parties :


1. Créer une connexion externe Microsoft Teams
2. Ajouter des étapes de notification Microsoft Teams à vos workflows

## Ajouter une étape de notification Microsoft Teams à un workflow


L'ajout d'étapes de notification Microsoft Teams à un workflow se fait comme pour n'importe quelle autre étape. Après avoir ajouté l'étape, ouvrez sa configuration, renseignez le formulaire et enregistrez-le. Vous pouvez alors tester votre notification Microsoft Teams.



## Mise en forme du message Microsoft Teams


Teams offre de nombreuses options de mise en forme, notamment l'ajout d'images et la mention d'utilisateurs. Consultez la documentation [Teams Message Text Formatting](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772) pour plus de détails.



## Créer une connexion externe Microsoft Teams


Il s'agit d'une configuration à effectuer une seule fois, qui permet à PlaidCloud d'envoyer des notifications Microsoft Teams en votre nom. Microsoft Teams permet de créer une application Webhook (un moyen générique d'envoyer une notification sur Internet). Après avoir créé l'application Webhook dans Microsoft Teams, ajoutez les identifiants fournis à PlaidCloud pour pouvoir l'utiliser.



### Création de l'application Webhook Microsoft Teams


Ces étapes doivent être effectuées par un administrateur Microsoft Teams. Suivez les étapes décrites ici : [Creating Incoming Webhook (Microsoft Teams Documentation)](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-incoming-webhook-1).



### Configuration de la connexion externe PlaidCloud


Ces étapes doivent être effectuées par un administrateur de l'espace de travail PlaidCloud disposant des autorisations nécessaires pour créer des connexions de données externes. Suivez ces étapes pour créer la connexion :


1. Accédez à `Analyze > Tools > External Data Connections`
2. Sous la sélection `+ New Connection`, choisissez Microsoft Teams Webhook
3. Renseignez le nom, la description, et collez l'URL du webhook générée lors de la création du webhook ci-dessus. Le nom indiqué ici s'affiche comme choix dans l'étape de workflow ; il doit donc être aussi descriptif que possible. Toute personne détenant l'URL peut publier dans votre canal : le champ **URL du webhook** la masque donc au moment où vous la collez et s'affiche vide lorsque vous rouvrez la connexion ; laissez-le vide pour conserver l'URL enregistrée.
4. Sélectionnez le bouton `+ Create`


## Exemples

Aucun exemple pour le moment...
