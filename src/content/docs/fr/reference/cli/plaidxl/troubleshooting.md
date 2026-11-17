---
title: Dépannage de PlaidXL
description: "Solutions aux problèmes courants de PlaidXL : complément absent du ruban, fenêtre contextuelle de connexion qui ne s'ouvre pas, espaces de travail ou projets introuvables, tables affichées en rouge, extractions lentes, erreurs dans les formules et les métriques PlaidXL, valeurs saisies qui ne sont pas écrites et enregistrements interrompus."
sidebar:
  label: Dépannage
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## L'onglet PlaidCloud n'apparaît pas sur le ruban

- Fermez toutes les fenêtres Excel, puis rouvrez Excel. Un complément récemment installé n'apparaît souvent qu'après un redémarrage.
- Ouvrez **Insert → My Add-ins** et sélectionnez **PlaidCloud**.
- Vérifiez que vous utilisez Excel de bureau pour Microsoft 365, ou Excel 2021 ou version ultérieure. Consultez [Installer PlaidXL](/fr/reference/cli/plaidxl/install/).
- Si votre organisation gère les compléments, demandez à votre administrateur Microsoft 365 si le complément **PlaidCloud** vous est déployé.

## La fenêtre contextuelle de connexion ne s'ouvre pas

Lorsque vous cliquez sur **Sign In**, Excel demande s'il doit afficher une fenêtre contextuelle. Autorisez-la. Si vous avez fermé l'invite, cliquez de nouveau sur **Sign In**.

Si la fenêtre contextuelle s'ouvre mais que vous ne parvenez pas à terminer la connexion, essayez de vous connecter à PlaidCloud dans votre navigateur avec la même adresse e-mail. Un problème à cet endroit, comme un mot de passe expiré ou un appareil d'authentification à deux facteurs que vous n'avez plus, doit d'abord être résolu dans PlaidCloud. Consultez [Authentification des membres](/fr/administration/access/member-authentication/).

## Un espace de travail n'est pas répertorié

**Select a workspace** répertorie les espaces de travail auxquels votre adresse e-mail appartient. S'il en manque un, vérifiez que vous avez saisi la même adresse e-mail que celle utilisée pour cet espace de travail, puis demandez à un administrateur de l'espace de travail de confirmer que vous en êtes membre. Consultez [Gérer les membres de l'espace de travail](/fr/administration/access/overview/managing-workspace-members/).

Pour passer à un autre espace de travail auquel vous appartenez, ouvrez le menu du compte et choisissez **Switch workspace**.

## Un projet, une table ou une dimension est introuvable

PlaidXL affiche ce que votre compte peut voir dans PlaidCloud. Si un projet est introuvable, demandez à son propriétaire de vous y donner accès. Si une table est introuvable, vérifiez qu'elle existe dans le projet sélectionné et qu'elle a été chargée avec des données : une table qui n'a jamais été alimentée affiche **Unable to get table metadata** lorsque vous la sélectionnez.

Les dossiers des listes de projets, de tables et de dimensions sont repliés au départ. Saisissez une partie du nom dans la zone de filtre en haut de la liste pour trouver un élément situé dans un dossier.

## Une table s'affiche en rouge

La table comporte plus de lignes ou de colonnes que n'en contient une feuille de calcul Excel, ou PlaidCloud ne peut pas en indiquer la taille. Vous pouvez l'extraire, et les lignes qui ne tiennent pas se poursuivent sur d'autres feuilles, mais une table répartie sur plusieurs feuilles ne peut pas être enregistrée. Sélectionnez **Avancé** pour filtrer les lignes et décochez les colonnes dont vous n'avez pas besoin jusqu'à ce que la table tienne. Consultez [Tables affichées en rouge](/fr/reference/cli/plaidxl/retrieve/#tables-affichées-en-rouge).

## Une récupération est lente

Excel est plus lent avec les tables larges. Décochez les cases des colonnes dont vous n'avez pas besoin et filtrez les lignes avec **Avancé**. Extraire uniquement les données que vous utilisez est plus rapide et produit un classeur plus petit.

Les grandes tables s'extraient et s'actualisent beaucoup plus vite dans Excel sur le web et dans les versions récentes d'Excel de bureau. Les versions plus anciennes d'Excel fonctionnent toujours, simplement sans cette accélération.

Si le volet affiche **PlaidXL was updated — reload the pane**, fermez le volet des tâches, rouvrez-le, puis extrayez de nouveau. Après une mise à jour de PlaidXL, le volet adopte la nouvelle version au prochain chargement.

Si une extraction affiche **This PlaidCloud workspace needs an update for PlaidXL**, demandez à votre administrateur de mettre l'espace de travail à jour vers une version récente de PlaidCloud.

## Une formule affiche une erreur

| Ce que vous voyez | Ce qu'il faut vérifier |
|---|---|
| `#SPILL!` | Des cellules dont le résultat a besoin sont occupées. Videz les cellules situées sous la formule ou à côté. |
| `#NAME?` | Excel ne reconnaît pas la fonction. Vérifiez que PlaidXL est installé (l'onglet **PlaidCloud** figure dans le ruban) et vérifiez l'orthographe d'après [la liste des fonctions](/fr/reference/cli/plaidxl/functions/). |
| Une erreur provenant d'une fonction `PLAIDXL` | Vérifiez que vous êtes connecté et que le bon projet est sélectionné, puis vérifiez chaque nom de table, de colonne, de dimension et de nœud par rapport à PlaidCloud : les noms doivent correspondre exactement. |
| `CELL` indique qu'une colonne de filtre est introuvable | Le premier argument de `DIMENSION_REPR` est une colonne de la table, et non une dimension. Utilisez exactement le nom de colonne de la table. Consultez [Valeurs](/fr/reference/cli/plaidxl/functions/#valeurs). |
| `#VALUE!` provenant de `METRIC` ou de `METRIC_BREAKDOWN` | Survolez la cellule pour lire la raison. Consultez [Erreurs de métriques](/fr/reference/cli/plaidxl/functions/#erreurs-de-métrique). |
| `#VALUE!` provenant d'une métrique : **This PlaidCloud workspace can't combine an alternate hierarchy with other members yet. Ask your administrator to update the workspace.** | L'espace de travail doit être mis à jour pour qu'une métrique puisse associer un membre d'une hiérarchie alternative à d'autres membres. Demandez à votre administrateur. Les autres cellules du même recalcul répondent normalement. |
| `#VALUE!` provenant de `CELL` ou de `CELLS` | Survolez la cellule pour lire la raison donnée par PlaidCloud, par exemple une colonne inconnue, un nœud inexistant ou sans membres, ou un problème de calcul de la valeur. Vérifiez les noms par rapport à PlaidCloud. |
| `CELL` renvoie un total inattendu | Un nœud ne se cumule que sur une colonne liée à sa dimension ; sur toute autre colonne, il doit correspondre exactement à une valeur. Vérifiez la colonne et le nœud de chaque filtre. |
| Les valeurs ne changent pas après une modification des données ou du projet | Cliquez sur **Recalculate PlaidXL formulas** dans le menu **Actualiser** du ruban. |
| `MEASURE_TYPE` renvoie une erreur | Utilisez l'une des valeurs `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, en minuscules. |

## Les formules renvoient les données d'un autre projet

Les fonctions PlaidXL lisent le projet lié au classeur. Ouvrez le volet des tâches dans ce classeur, choisissez le projet pour lequel le rapport a été conçu, puis cliquez sur **Recalculate PlaidXL formulas** dans le menu **Actualiser** du ruban. Chaque classeur a son propre projet : en choisir un dans un autre classeur ne modifie pas celui-ci. Consultez [Le projet appartient au classeur](/fr/reference/cli/plaidxl/retrieve/#le-projet-appartient-au-classeur).

## Les tables d'un autre espace de travail sont ignorées

Après un changement d'espace de travail, **Refresh All Tables** indique que des tables ou des dimensions d'un autre espace de travail de ce classeur n'ont pas été actualisées, et elles ne figurent plus sous **On this sheet**. Extrayez de nouveau chaque table dans l'espace de travail actuel pour la lier.

## Une valeur saisie n'est pas écrite

Lorsque vous saisissez une valeur par-dessus une `CELL`, le volet des tâches indique ce qu'il a écrit et répertorie ce qu'il n'a pas écrit, avec la raison. Consultez [Saisir des valeurs dans PlaidCloud](/fr/reference/cli/plaidxl/write-values/).

| Ce que vous voyez | Que faire |
|---|---|
| Seule une cellule contenant une unique `PLAIDXL.CELL` accepte une valeur saisie | Saisissez la valeur par-dessus une cellule dont la formule est une seule `CELL`, éventuellement multipliée, divisée ou négative. |
| Un argument ne peut pas être lu ici | Les arguments de la `CELL` doivent être des cellules ou du texte, et non d'autres calculs. |
| Une méthode de répartition, une forme ou un blocage ne s'applique qu'aux sommes | Les codes tels que `E1200`, `1200 like FY2025` et `H` ne fonctionnent que sur les cellules **somme**. Saisissez un nombre simple dans les autres. |
| Tous les membres sont bloqués | Levez un blocage avec `H`, puis saisissez de nouveau la valeur. |
| L'espace de travail n'accepte pas encore les valeurs saisies dans Excel | Demandez à votre administrateur de mettre à jour l'espace de travail. |

## Un enregistrement est refusé ou interrompu

Un enregistrement écrit immédiatement et s'interrompt rarement. Il le fait dans les cas suivants :

| Ce que vous voyez | Que faire |
|---|---|
| La ligne d'en-tête ne correspond plus aux colonnes extraites | Remettez l'en-tête tel qu'il a été extrait, ou extrayez de nouveau la table. |
| Une valeur ne peut pas être convertie | Rien n'est écrit et les lignes concernées sont listées. Corrigez les valeurs pour qu'elles correspondent au type de données de la colonne. |
| La table se poursuit sur d'autres feuilles | Une table répartie sur plusieurs feuilles ne peut pas être enregistrée. Extrayez-la avec un filtre pour qu'elle tienne sur une seule feuille. |
| La table a été extraite avec un filtre que l'enregistrement ne peut pas respecter | Extrayez-la de nouveau avec un filtre composé de règles **Égal à** et **dans** reliées par **AND**, ou sans filtre. |
| Des lignes sont en dehors de votre accès aux lignes | Rien n'est enregistré. Supprimez ces lignes, puis enregistrez de nouveau. |
| Des colonnes contiennent du texte de plus de 32 767 caractères, la limite d'une cellule Excel | Excel affiche le texte tronqué et l'enregistrer le tronquerait aussi dans PlaidCloud : l'enregistrement est donc désactivé pour cette table. Extrayez la table sans ces colonnes pour pouvoir l'enregistrer. |
| La table n'a été écrite qu'en partie | Excel a refusé une partie de la dernière actualisation. Actualisez la table, puis enregistrez-la. |
| La feuille n'est pas liée à une table | Extrayez d'abord la table dans la feuille. Seules les tables extraites dans la feuille active sont répertoriées sous **On this sheet**. |

Pour annuler un enregistrement, cliquez sur **Défaire** dans le message ou sur **Undo last write** dans le ruban. Chaque enregistrement conserve son propre point de restauration pendant 7 jours : vous pouvez donc annuler n'importe quel enregistrement jusqu'à 7 jours après l'avoir effectué. Consultez [Enregistrer une table dans PlaidCloud](/fr/reference/cli/plaidxl/retrieve/#enregistrer-une-table-dans-plaidcloud).

## Voir aussi

- [Installer PlaidXL](/fr/reference/cli/plaidxl/install/)
- [Se connecter à PlaidXL](/fr/reference/cli/plaidxl/connect/)
- [Obtenir de l'aide](/fr/guides/support/getting-help/) : ouvrez un ticket d'assistance
