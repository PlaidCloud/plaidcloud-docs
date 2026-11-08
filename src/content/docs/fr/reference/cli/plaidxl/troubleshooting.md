---
title: Dépannage de PlaidXL
description: Solutions aux problèmes courants de PlaidXL — complément absent du ruban, fenêtre contextuelle de connexion qui ne s'ouvre pas, espaces de travail ou projets introuvables, tables affichées en rouge, récupérations lentes, erreurs dans les formules et les métriques PlaidXL, valeurs saisies non écrites et enregistrements interrompus.
sidebar:
  label: Dépannage
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## L'onglet PlaidCloud n'apparaît pas sur le ruban

- Fermez toutes les fenêtres Excel et rouvrez Excel. Un complément fraîchement installé n'apparaît souvent qu'après un redémarrage.
- Ouvrez **Insert → My Add-ins** et sélectionnez **PlaidCloud**.
- Vérifiez que vous utilisez Excel de bureau pour Microsoft 365, ou Excel 2021 ou une version ultérieure. Consultez [Installer PlaidXL](/fr/reference/cli/plaidxl/install/).
- Si votre organisation gère les compléments, demandez à votre administrateur Microsoft 365 si le complément **PlaidCloud** vous est déployé.

## La fenêtre contextuelle de connexion ne s'ouvre pas

Lorsque vous cliquez sur **Sign In**, Excel demande s'il faut afficher une fenêtre contextuelle. Autorisez-la. Si vous avez ignoré la demande, cliquez de nouveau sur **Sign In**.

Si la fenêtre contextuelle s'ouvre mais que vous ne parvenez pas à terminer la connexion, essayez de vous connecter à PlaidCloud dans votre navigateur avec la même adresse e-mail. Un problème à cet endroit — un mot de passe expiré ou un appareil à deux facteurs que vous n'avez plus — doit d'abord être résolu dans PlaidCloud. Consultez [Authentification des membres](/fr/administration/access/member-authentication/).

## Un espace de travail n'est pas répertorié

**Select a workspace** répertorie les espaces de travail auxquels appartient votre adresse e-mail. S'il en manque un, vérifiez que vous avez saisi la même adresse e-mail que celle que vous utilisez pour cet espace de travail, puis demandez à un administrateur de l'espace de travail de confirmer que vous en êtes membre. Consultez [Gérer les membres de l'espace de travail](/fr/administration/access/overview/managing-workspace-members/).

Pour passer à un autre espace de travail auquel vous appartenez, ouvrez le menu de compte et choisissez **Switch workspace**.

## Un projet, une table ou une dimension est introuvable

PlaidXL affiche ce que votre compte peut voir dans PlaidCloud. Si un projet est introuvable, demandez à son propriétaire de vous donner l'accès. Si une table est introuvable, vérifiez qu'elle existe dans le projet sélectionné et qu'elle a été chargée avec des données — une table dans laquelle rien n'a jamais été écrit affiche **Unable to get table metadata** lorsque vous la sélectionnez.

Les dossiers des listes de projets, de tables et de dimensions sont réduits au départ. Saisissez une partie du nom dans la zone de filtre en haut de la liste pour trouver un élément à l'intérieur d'un dossier.

## Une table s'affiche en rouge

La table compte plus de lignes ou de colonnes qu'une feuille de calcul Excel n'en contient, ou PlaidCloud ne peut pas indiquer sa taille. Vous pouvez la récupérer, et les lignes qui ne tiennent pas continuent sur d'autres feuilles, mais une table répartie sur plusieurs feuilles ne peut pas être enregistrée. Sélectionnez **Avancé** pour filtrer les lignes, et décochez les colonnes dont vous n'avez pas besoin, jusqu'à ce qu'elle tienne. Consultez [Tables affichées en rouge](/fr/reference/cli/plaidxl/retrieve/#tables-affichées-en-rouge).

## Une récupération est lente

Excel est le plus lent avec les tables larges. Décochez les colonnes dont vous n'avez pas besoin et filtrez les lignes avec **Avancé**. Ne récupérer que les données avec lesquelles vous travaillez est plus rapide et donne un classeur plus léger.

## Une formule affiche une erreur

| Ce que vous voyez | Ce qu'il faut vérifier |
|---|---|
| `#SPILL!` | Quelque chose se trouve dans les cellules dont le résultat a besoin. Videz les cellules situées sous la formule ou à côté. |
| `#NAME?` | Excel ne reconnaît pas la fonction. Vérifiez que PlaidXL est installé — l'onglet **PlaidCloud** figure sur le ruban — et vérifiez l'orthographe à l'aide de [la liste des fonctions](/fr/reference/cli/plaidxl/functions/). |
| Une erreur provenant d'une fonction `PLAIDXL` | Vérifiez que vous êtes connecté et que le bon projet est sélectionné, puis vérifiez chaque nom de table, de colonne, de dimension et de nœud dans PlaidCloud — les noms doivent correspondre exactement. |
| `CELL` signale qu'une colonne de filtre est introuvable | Le premier argument de `DIMENSION_REPR` est une colonne de la table, pas une dimension. Utilisez exactement le nom de la colonne de la table. Consultez [Valeurs](/fr/reference/cli/plaidxl/functions/#valeurs). |
| `#VALUE!` provenant de `METRIC` ou `METRIC_BREAKDOWN` | Survolez la cellule pour lire la raison. Consultez [Erreurs de métrique](/fr/reference/cli/plaidxl/functions/#erreurs-de-métrique). |
| `#VALUE!` provenant d'une métrique : **This PlaidCloud workspace can't combine an alternate hierarchy with other members yet. Ask your administrator to update the workspace.** | L'espace de travail doit être mis à jour avant qu'une métrique puisse combiner un membre d'une hiérarchie alternative avec d'autres membres. Demandez à votre administrateur. Les autres cellules du même recalcul répondent quand même. |
| `#VALUE!` provenant de `CELL` ou `CELLS` | Survolez la cellule pour lire la raison indiquée par PlaidCloud, par exemple une colonne inconnue, un nœud qui n'existe pas ou n'a pas de membres, ou un problème de calcul de la valeur. Vérifiez les noms dans PlaidCloud. |
| `CELL` renvoie un total inattendu | Un nœud ne se consolide que sur une colonne liée à sa dimension ; sur toute autre colonne, il doit correspondre exactement à une valeur. Vérifiez la colonne et le nœud de chaque filtre. |
| Les valeurs ne changent pas après une modification des données ou du projet | Cliquez sur **Recalculate PlaidXL formulas** dans le menu **Actualiser** du ruban. |
| `MEASURE_TYPE` renvoie une erreur | Utilisez l'une des valeurs `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, en minuscules. |

## Les formules renvoient les données d'un autre projet

Les fonctions PlaidXL lisent depuis le projet lié au classeur. Ouvrez le volet des tâches dans ce classeur, choisissez le projet pour lequel le rapport a été créé, puis cliquez sur **Recalculate PlaidXL formulas** dans le menu **Actualiser** du ruban. Chaque classeur a son propre projet : en choisir un dans un autre classeur ne modifie donc pas celui-ci. Consultez [Le projet appartient au classeur](/fr/reference/cli/plaidxl/retrieve/#le-projet-appartient-au-classeur).

## Les tables d'un autre espace de travail sont ignorées

Après un changement d'espace de travail, **Refresh All Tables** indique que des tables ou des dimensions d'un autre espace de travail de ce classeur n'ont pas été actualisées, et elles ne sont pas répertoriées sous **On this sheet**. Récupérez chaque table de nouveau dans l'espace de travail actuel pour la lier.

## Une valeur saisie n'est pas écrite

Lorsque vous saisissez une valeur par-dessus une formule `CELL`, le volet des tâches indique ce qu'il a écrit et répertorie tout ce qu'il n'a pas écrit, avec la raison. Consultez [Saisir des valeurs dans PlaidCloud](/fr/reference/cli/plaidxl/write-values/).

| Ce que vous voyez | Que faire |
|---|---|
| Seule une cellule contenant exactement un `PLAIDXL.CELL` accepte une valeur saisie | Saisissez la valeur par-dessus une cellule dont la formule est un seul `CELL`, éventuellement multiplié, divisé ou opposé. |
| Un argument ne peut pas être lu ici | Les arguments de `CELL` doivent être des cellules ou du texte, pas d'autres calculs. |
| Une méthode de répartition, une forme ou un blocage ne s'applique qu'aux sommes | Des codes tels que `E1200`, `1200 like FY2025` et `H` ne fonctionnent que sur les cellules **sum**. Saisissez un nombre simple sur les autres. |
| Tous les membres sont bloqués | Levez un blocage avec `H`, puis saisissez de nouveau la valeur. |
| L'espace de travail n'accepte pas encore les valeurs saisies dans Excel | Demandez à votre administrateur de mettre à jour l'espace de travail. |

## Un enregistrement est refusé ou interrompu

Un enregistrement écrit immédiatement et s'interrompt rarement. Il le fait dans les cas suivants :

| Ce que vous voyez | Que faire |
|---|---|
| La ligne d'en-tête ne correspond plus aux colonnes récupérées | Remettez l'en-tête tel qu'il a été récupéré, ou récupérez de nouveau la table. |
| Une valeur ne peut pas être convertie | Rien n'est écrit et les lignes sont répertoriées. Corrigez les valeurs pour qu'elles correspondent au type de données de la colonne. |
| La table continue sur d'autres feuilles | Une table répartie sur plusieurs feuilles ne peut pas être enregistrée. Récupérez-la avec un filtre pour qu'elle tienne sur une seule feuille. |
| La table a été récupérée avec un filtre que l'enregistrement ne peut pas respecter | Récupérez-la de nouveau avec un filtre composé de règles **Égal à** et **in** reliées par **AND**, ou sans filtre. |
| Des lignes sont en dehors de votre accès aux lignes | Rien n'est enregistré. Supprimez ces lignes, puis enregistrez de nouveau. |
| La feuille n'est liée à aucune table | Récupérez d'abord la table dans la feuille. Seules les tables récupérées dans la feuille active sont répertoriées sous **On this sheet**. |

Pour annuler un enregistrement, cliquez sur **Défaire** dans le message ou sur **Undo last write** sur le ruban. Chaque enregistrement conserve son propre point de restauration pendant 7 jours, vous pouvez donc annuler n'importe quel enregistrement jusqu'à 7 jours après l'avoir effectué. Consultez [Enregistrer une table dans PlaidCloud](/fr/reference/cli/plaidxl/retrieve/#enregistrer-une-table-dans-plaidcloud).

## Voir aussi

- [Installer PlaidXL](/fr/reference/cli/plaidxl/install/)
- [Se connecter à PlaidXL](/fr/reference/cli/plaidxl/connect/)
- [Obtenir de l'aide](/fr/guides/support/getting-help/) — ouvrir un ticket d'assistance
