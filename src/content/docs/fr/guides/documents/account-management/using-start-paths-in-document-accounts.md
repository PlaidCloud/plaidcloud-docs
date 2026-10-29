---
title: Utiliser les chemins de départ dans les comptes de documents
description: Configurez des chemins de départ dans les comptes de documents PlaidCloud pour contrôler le répertoire par défaut à l'ouverture du stockage de fichiers.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/account-management/using-start-paths-in-document-accounts.md
---

Le formulaire de gestion du compte permet de configurer les informations de connexion au stockage ainsi qu'un chemin de départ. Un chemin de départ permet à ceux qui utilisent le compte de commencer à parcourir la structure de répertoires plus bas dans l'arborescence. Cette option est particulièrement utile lorsque plusieurs équipes ont besoin d'un stockage de fichiers séparé, alors que vous ne voulez qu'un seul compte de service de stockage sous-jacent.



L'option Chemin de départ des comptes de documents est utile pour les raisons suivantes :


* Contrôler l'accès aux sous-répertoires pour des équipes et des groupes précis
* N'accorder l'accès qu'à un seul bucket

Par exemple, définir un chemin de départ *teams/team_1/* pour le compte de documents `Team 1` et *teams/team_2* pour le compte de documents `Team 2` offre des points de départ différents sur un compte partagé. Lorsqu'un membre ouvre le compte de documents Team 1, il commence sa navigation dans les fichiers à l'intérieur de *team/team_1*. Il ne pourra pas remonter dans l'arborescence ni voir quoi que ce soit au-dessus de *teams/team_1*.



L'équipe 2 aurait une restriction similaire : elle ne pourrait pas naviguer dans la zone de l'équipe 1.



Cela permet de restreindre des équipes précises aux niveaux inférieurs de l'arborescence tout en donnant à d'autres équipes un accès de niveau supérieur, sans complexité supplémentaire de stockage cloud comme des buckets supplémentaires ou des autorisations spéciales.



## Ajouter et mettre à jour le chemin de départ


1. Accédez à Document > Manage Accounts
2. Sélectionnez le compte que vous souhaitez modifier et passez en mode édition
3. Ajoutez un chemin de départ dans le champ de texte Chemin de départ
4. Cliquez sur le bouton Enregistrer

## Format du chemin de départ


Le chemin commence toujours par le nom du bucket, suivi des sous-répertoires.



```text
<my-bucket>/folder1/folder2/
```
