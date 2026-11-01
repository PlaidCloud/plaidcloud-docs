---
title: Dépannage de PlaidXL
description: Solutions aux problèmes courants de PlaidXL — complément absent du ruban, fenêtre contextuelle de connexion qui ne s'ouvre pas, espaces de travail ou projets manquants, tables affichées en rouge, récupérations lentes et erreurs dans les formules PlaidXL.
sidebar:
  label: Dépannage
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## L'onglet PlaidCloud n'est pas dans le ruban

- Fermez toutes les fenêtres Excel et rouvrez Excel. Un complément qui vient d'être installé n'apparaît souvent qu'après un redémarrage.
- Ouvrez **Insertion → Mes compléments** et sélectionnez **PlaidCloud**.
- Vérifiez que vous utilisez Excel de bureau pour Microsoft 365, ou Excel 2021 ou une version ultérieure. Consultez [Installer PlaidXL](/fr/reference/cli/plaidxl/install/).
- Si votre organisation gère les compléments, demandez à votre administrateur Microsoft 365 si le complément **PlaidCloud** vous est déployé.

## La fenêtre contextuelle de connexion ne s'ouvre pas

Lorsque vous cliquez sur **Sign In**, Excel demande s'il doit afficher une fenêtre contextuelle. Autorisez-la. Si vous avez ignoré l'invite, cliquez de nouveau sur **Sign In**.

Si la fenêtre contextuelle s'ouvre mais que vous ne parvenez pas à terminer la connexion, essayez de vous connecter à PlaidCloud dans votre navigateur avec la même adresse e-mail. Un problème à cet endroit — un mot de passe expiré ou un appareil d'authentification à deux facteurs que vous n'avez plus — doit d'abord être corrigé dans PlaidCloud. Consultez [Authentification des membres](/fr/administration/access/member-authentication/).

## Un espace de travail n'est pas listé

**Select a workspace** liste les espaces de travail auxquels votre adresse e-mail appartient. S'il en manque un, vérifiez que vous avez saisi la même adresse e-mail que celle que vous utilisez pour cet espace de travail, puis demandez à un administrateur de l'espace de travail de confirmer que vous en êtes membre. Consultez [Gérer les membres de l'espace de travail](/fr/administration/access/overview/managing-workspace-members/).

Pour passer à un autre espace de travail auquel vous appartenez, ouvrez le menu du compte et choisissez **Switch workspace**.

## Un projet, une table ou une dimension est manquant

PlaidXL affiche ce que votre compte peut voir dans PlaidCloud. Si un projet est manquant, demandez à son propriétaire de vous donner accès. Si une table est manquante, vérifiez qu'elle existe dans le projet sélectionné et qu'elle a été chargée avec des données — une table qui n'a jamais été écrite affiche **Unable to get table metadata** lorsque vous la sélectionnez.

Les dossiers des listes de projets, de tables et de dimensions sont réduits au départ. Saisissez une partie du nom dans la zone de filtre en haut de la liste pour trouver un élément à l'intérieur d'un dossier.

## Une table s'affiche en rouge

La table a plus de lignes ou de colonnes qu'une feuille de calcul Excel n'en contient. Sélectionnez **Advanced** pour filtrer les lignes, et décochez les colonnes dont vous n'avez pas besoin, jusqu'à ce qu'elle tienne. Consultez [Tables affichées en rouge](/fr/reference/cli/plaidxl/retrieve/#tables-affichées-en-rouge).

## Une récupération est lente

Excel est le plus lent avec les tables larges. Décochez les cases des colonnes dont vous n'avez pas besoin, et filtrez les lignes avec **Advanced**. Ne récupérer que les données avec lesquelles vous travaillez est plus rapide et produit un classeur plus petit.

## Une formule affiche une erreur

| Ce que vous voyez | Ce qu'il faut vérifier |
|---|---|
| `#SPILL!` | Quelque chose se trouve dans les cellules dont le résultat a besoin. Videz les cellules situées sous la formule ou à côté. |
| `#NAME?` | Excel ne reconnaît pas la fonction. Vérifiez que PlaidXL est installé — l'onglet **PlaidCloud** est dans le ruban — et vérifiez l'orthographe en vous aidant de [la liste des fonctions](/fr/reference/cli/plaidxl/functions/). |
| Une erreur d'une fonction `PLAIDXL` | Vérifiez que vous êtes connecté et que le bon projet est sélectionné, puis vérifiez chaque nom de table, de colonne, de dimension et de nœud par rapport à PlaidCloud — les noms doivent correspondre exactement. |
| `CELL` signale qu'une colonne de filtre est introuvable | Le premier argument de `DIMENSION_REPR` est une colonne de la table, et non une dimension. Utilisez exactement le nom de la colonne de la table. Consultez [Valeurs](/fr/reference/cli/plaidxl/functions/#valeurs). |
| `#VALUE!` provenant de `CELL` ou `CELLS` | Survolez la cellule pour lire la raison donnée par PlaidCloud, par exemple une colonne inconnue, un nœud qui n'existe pas ou n'a pas de membres, ou un problème de calcul de la valeur. Vérifiez les noms par rapport à PlaidCloud. |
| `CELL` renvoie un total inattendu | Un nœud ne se consolide que sur une colonne liée à sa dimension ; sur toute autre colonne, il doit correspondre exactement à une valeur. Vérifiez la colonne et le nœud de chaque filtre. |
| Les valeurs ne changent pas après un changement de données ou de projet | Forcez un recalcul complet — sous Windows, **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` renvoie une erreur | Utilisez l'une des valeurs `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, en minuscules. |

## Les formules renvoient les données d'un autre projet

Les fonctions PlaidXL lisent le projet lié au classeur. Ouvrez le volet des tâches dans ce classeur, choisissez le projet pour lequel le rapport a été construit, puis forcez un recalcul complet. Chaque classeur a son propre projet : en choisir un dans un autre classeur ne modifie donc pas celui-ci. Consultez [Le projet appartient au classeur](/fr/reference/cli/plaidxl/retrieve/#le-projet-appartient-au-classeur).

## Les tables d'un autre espace de travail sont ignorées

Après un changement d'espace de travail, le volet des tâches indique combien de tables suivies appartiennent à un autre espace de travail et sont ignorées par **Refresh All Tables**. Récupérez chaque table de nouveau dans l'espace de travail actuel pour la lier.

## Un enregistrement est refusé ou interrompu

| Ce que vous voyez | Que faire |
|---|---|
| Des lignes sont vides à l'intérieur de la table | Une seule ligne vide est ignorée. Deux lignes vides consécutives ou plus, avec des données en dessous, interrompent un enregistrement. Supprimez les lignes vides ou remplissez-les, puis enregistrez de nouveau. |
| La table a changé depuis que vous l'avez récupérée | Quelqu'un d'autre a enregistré la table dans PlaidCloud. Récupérez-la de nouveau et réappliquez vos modifications. (PlaidCloud ne peut le vérifier que pour certains types de tables ; lorsqu'il ne le peut pas, la confirmation avertit que les modifications des autres seront écrasées.) |
| Une valeur ne peut pas être convertie | Rien n'est écrit et les lignes sont listées. Corrigez les valeurs pour qu'elles correspondent au type de données de la colonne. |
| La feuille n'est pas liée à une table | Récupérez d'abord la table dans la feuille. **Save to PlaidCloud…** n'apparaît que pour les tables récupérées dans la feuille active. |

Pour annuler un enregistrement, cliquez sur **Restore previous version** dans le message de confirmation, ou ouvrez la table dans PlaidCloud et choisissez la version précédant l'enregistrement dans le menu **As of**. Le point de restauration est conservé pendant 7 jours. Consultez [Enregistrer une table dans PlaidCloud](/fr/reference/cli/plaidxl/retrieve/#enregistrer-une-table-dans-plaidcloud).

## Voir aussi

- [Installer PlaidXL](/fr/reference/cli/plaidxl/install/)
- [Se connecter à PlaidXL](/fr/reference/cli/plaidxl/connect/)
- [Obtenir de l'aide](/fr/guides/support/getting-help/) — ouvrir un ticket de support
