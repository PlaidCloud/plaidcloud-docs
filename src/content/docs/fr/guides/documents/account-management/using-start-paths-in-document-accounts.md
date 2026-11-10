---
title: Utiliser les chemins de départ dans les comptes de documents
description: Configurez les chemins de départ des comptes de documents PlaidCloud pour définir l'emplacement de répertoire par défaut lors de la navigation dans le stockage de fichiers.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/account-management/using-start-paths-in-document-accounts.md
---

Le formulaire de gestion du compte permet de configurer les informations de connexion au stockage ainsi qu'un chemin de départ. Un chemin de départ permet aux utilisateurs du compte de commencer à parcourir l'arborescence à un niveau plus profond. Cette option est particulièrement utile lorsque plusieurs équipes ont besoin d'un stockage de fichiers cloisonné, mais que vous ne souhaitez utiliser qu'un seul compte de service de stockage sous-jacent.



L'option Chemin de départ des comptes Document est utile pour les raisons suivantes :


* Contrôler l'accès aux sous-répertoires pour des équipes et des groupes précis
* N'accorder l'accès qu'à un seul bucket

Par exemple, définir le chemin de départ *teams/team_1/* pour le compte Document `Team 1` *et teams/team_2* pour le compte Document `Team 2` offre des points de départ différents sur un compte partagé. Lorsqu'un membre ouvre le compte Document Team 1, il commence sa navigation dans *team/team_1*. Il ne peut pas remonter dans l'arborescence pour voir ce qui se trouve au-dessus de *teams/team_1*.



L'équipe 2 aurait une restriction similaire et ne pourrait pas naviguer dans l'espace de l'équipe 1.



Il est ainsi possible de limiter certaines équipes aux niveaux inférieurs de l'arborescence tout en donnant à d'autres équipes un accès aux niveaux supérieurs, sans aucune complexité supplémentaire dans le stockage cloud, comme des buckets supplémentaires ou des autorisations spéciales.



## Ajouter et mettre à jour le chemin de départ


1. Accédez à `Document > Manage`
2. Ouvrez le compte à modifier et sélectionnez **Modifier**
3. Saisissez un chemin de départ dans le champ de texte Chemin de départ
4. Sélectionnez le bouton Enregistrer

## Format du chemin de départ


Le chemin commence toujours par le nom du bucket, suivi des sous-répertoires.



```text
<my-bucket>/folder1/folder2/
```
