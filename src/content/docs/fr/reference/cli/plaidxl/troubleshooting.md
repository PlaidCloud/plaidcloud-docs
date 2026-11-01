---
title: Dépannage de PlaidXL
description: Solutions aux problèmes courants de PlaidXL — complément absent du ruban, fenêtre de connexion qui ne s'ouvre pas, espaces de travail ou projets manquants, tables affichées en rouge, récupérations lentes et erreurs dans les formules PlaidXL.
sidebar:
  label: Dépannage
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## L'onglet PlaidCloud n'est pas dans le ruban

- Fermez toutes les fenêtres Excel, puis rouvrez Excel. Un complément nouvellement installé n'apparaît souvent qu'après un redémarrage.
- Ouvrez **Insert → My Add-ins** et sélectionnez **PlaidCloud**.
- Vérifiez que vous utilisez Excel pour ordinateur avec Microsoft 365, ou Excel 2021 ou version ultérieure. Consultez [Installer PlaidXL](/fr/reference/cli/plaidxl/install/).
- Si votre organisation gère les compléments, demandez à votre administrateur Microsoft 365 si le complément **PlaidCloud** est déployé pour vous.

## La fenêtre de connexion ne s'ouvre pas

Lorsque vous cliquez sur **Sign In**, Excel demande s'il faut afficher une fenêtre contextuelle. Autorisez-la. Si vous avez fermé l'invite, cliquez de nouveau sur **Sign In**.

Si la fenêtre contextuelle s'ouvre mais que vous ne parvenez pas à terminer la connexion, essayez de vous connecter à PlaidCloud dans votre navigateur avec la même adresse e-mail. Un problème à cet endroit — un mot de passe expiré ou un appareil à deux facteurs que vous n'avez plus — doit d'abord être corrigé dans PlaidCloud. Consultez [Authentification des membres](/fr/administration/access/member-authentication/).

## Un espace de travail n'est pas listé

**Select a workspace** liste les espaces de travail auxquels votre adresse e-mail appartient. S'il en manque un, vérifiez que vous avez saisi la même adresse e-mail que celle que vous utilisez pour cet espace de travail, puis demandez à un administrateur de l'espace de travail de confirmer que vous en êtes membre. Consultez [Gérer les membres de l'espace de travail](/fr/administration/access/overview/managing-workspace-members/).

Pour passer à un autre espace de travail auquel vous appartenez, ouvrez le menu du compte et choisissez **Switch workspace**.

## Un projet, une table ou une dimension est absent

PlaidXL affiche ce que votre compte peut voir dans PlaidCloud. Si un projet est absent, demandez à son propriétaire de vous donner accès. Si une table est absente, vérifiez qu'elle existe dans le projet sélectionné et qu'elle a été chargée avec des données — une table qui n'a jamais été écrite affiche **Unable to get table metadata** lorsque vous la sélectionnez.

Les dossiers des listes de projets, de tables et de dimensions sont réduits au départ. Saisissez une partie du nom dans la zone de filtre en haut de la liste pour trouver un élément situé dans un dossier.

## Une table s'affiche en rouge

La table contient plus de lignes ou de colonnes qu'une feuille de calcul Excel ne peut en contenir. Sélectionnez **Avancé** pour filtrer les lignes et décochez les colonnes dont vous n'avez pas besoin jusqu'à ce qu'elle tienne. Consultez [Tables affichées en rouge](/fr/reference/cli/plaidxl/retrieve/#tables-affichées-en-rouge).

## Une récupération est lente

Excel est plus lent avec les tables larges. Décochez les cases des colonnes dont vous n'avez pas besoin et filtrez les lignes avec **Avancé**. Ne récupérer que les données avec lesquelles vous travaillez est plus rapide et produit un classeur plus léger.

## Une formule affiche une erreur

| Ce que vous voyez | Ce qu'il faut vérifier |
|---|---|
| `#SPILL!` | Quelque chose se trouve dans les cellules dont le résultat a besoin. Videz les cellules situées sous la formule ou à côté d'elle. |
| `#NAME?` | Excel ne reconnaît pas la fonction. Vérifiez que PlaidXL est installé — l'onglet **PlaidCloud** figure dans le ruban — et vérifiez l'orthographe par rapport à [la liste des fonctions](/fr/reference/cli/plaidxl/functions/). |
| Une erreur provenant d'une fonction `PLAIDXL` | Vérifiez que vous êtes connecté et que le bon projet est sélectionné, puis vérifiez chaque nom de table, de colonne, de dimension et de nœud par rapport à PlaidCloud — les noms doivent correspondre exactement. |
| `CELL` signale qu'une colonne de filtre est introuvable | Le premier argument de `DIMENSION_REPR` est une colonne de la table, et non une dimension. Utilisez exactement le nom de colonne de la table. Consultez [Valeurs](/fr/reference/cli/plaidxl/functions/#valeurs). |
| `#VALUE!` provenant de `CELL` ou `CELLS` | Survolez la cellule pour lire la raison fournie par PlaidCloud, par exemple une colonne inconnue, un nœud qui n'existe pas ou qui n'a aucun membre, ou un problème lors du calcul de la valeur. Vérifiez les noms par rapport à PlaidCloud. |
| `CELL` renvoie un total inattendu | Un nœud ne se consolide que sur une colonne liée à sa dimension§T; sur toute autre colonne, il doit correspondre exactement à une valeur. Vérifiez la colonne et le nœud de chaque filtre. |
| Les valeurs ne changent pas après une modification des données ou du projet | Forcez un recalcul complet — sous Windows, **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` renvoie une erreur | Utilisez l'une des valeurs `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, en minuscules. |

## Les formules renvoient les données d'un autre projet

Les fonctions PlaidXL lisent les données du projet associé au classeur. Ouvrez le volet des tâches dans ce classeur, choisissez le projet pour lequel le rapport a été conçu, puis forcez un recalcul complet. Chaque classeur a son propre projet§T; en choisir un dans un autre classeur ne modifie donc pas celui-ci. Consultez [Le projet appartient au classeur](/fr/reference/cli/plaidxl/retrieve/#le-projet-appartient-au-classeur).

## Les tables d'un autre espace de travail sont ignorées

Après un changement d'espace de travail, le volet des tâches indique combien de tables suivies appartiennent à un autre espace de travail et sont ignorées par **Refresh All Tables**. Récupérez de nouveau chaque table dans l'espace de travail actuel pour la lier.

## Un enregistrement est refusé ou interrompu

| Ce que vous voyez | Que faire |
|---|---|
| Des lignes sont vides à l'intérieur de la table | Deux lignes vides consécutives ou plus, avec des données en dessous, interrompent un enregistrement. Supprimez les lignes vides ou remplissez-les, puis enregistrez de nouveau. |
| La table a changé depuis que vous l'avez récupérée | Quelqu'un d'autre a enregistré la table dans PlaidCloud. Récupérez-la de nouveau et réappliquez vos modifications. |
| Une valeur ne peut pas être convertie | Rien n'est écrit et les lignes concernées sont listées. Corrigez les valeurs pour qu'elles correspondent au type de données de la colonne. |
| La feuille n'est pas liée à une table | Récupérez d'abord la table dans la feuille. **Save to PlaidCloud…** n'apparaît que pour les tables récupérées dans la feuille active. |

Pour annuler un enregistrement, cliquez sur **Restore previous version** dans le message de confirmation, ou ouvrez la table dans PlaidCloud et choisissez la version antérieure à l'enregistrement dans le menu **As of**. Le point de restauration est conservé pendant 7 jours. Consultez [Enregistrer une table dans PlaidCloud](/fr/reference/cli/plaidxl/retrieve/#enregistrer-une-table-dans-plaidcloud).

## Voir aussi

- [Installer PlaidXL](/fr/reference/cli/plaidxl/install/)
- [Se connecter à PlaidXL](/fr/reference/cli/plaidxl/connect/)
- [Obtenir de l'aide](/fr/guides/support/getting-help/) — ouvrir un ticket d'assistance
