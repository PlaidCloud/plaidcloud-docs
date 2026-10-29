---
title: Dépannage de PlaidXL
description: "Solutions aux problèmes courants de PlaidXL : complément absent du ruban, fenêtre contextuelle de connexion qui ne s'ouvre pas, espaces de travail ou projets introuvables, tables affichées en rouge, récupérations lentes et erreurs dans les formules PlaidXL."
sidebar:
  label: Dépannage
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## L'onglet PlaidCloud n'apparaît pas dans le ruban

- Fermez toutes les fenêtres Excel, puis rouvrez Excel. Un complément récemment installé n'apparaît souvent qu'après un redémarrage.
- Ouvrez **Insert → My Add-ins** et sélectionnez **PlaidCloud**.
- Vérifiez que vous utilisez Excel pour ordinateur avec Microsoft 365, ou Excel 2021 ou version ultérieure. Consultez [Installer PlaidXL](/fr/reference/cli/plaidxl/install/).
- Si votre organisation gère les compléments, demandez à votre administrateur Microsoft 365 si le complément **PlaidCloud** vous est bien déployé.

## La fenêtre contextuelle de connexion ne s'ouvre pas

Lorsque vous cliquez sur **Sign In**, Excel demande s'il doit afficher une fenêtre contextuelle. Autorisez-la. Si vous avez fermé l'invite, cliquez de nouveau sur **Sign In**.

Si la fenêtre contextuelle s'ouvre mais que vous ne parvenez pas à terminer la connexion, essayez de vous connecter à PlaidCloud dans votre navigateur avec la même adresse e-mail. Un problème à ce niveau (mot de passe expiré ou appareil d'authentification à deux facteurs que vous n'avez plus) doit d'abord être résolu dans PlaidCloud. Consultez [Authentification des membres](/fr/administration/access/member-authentication/).

## Un espace de travail n'est pas listé

**Select a tenant** liste les espaces de travail auxquels votre adresse e-mail appartient. S'il en manque un, vérifiez que vous avez saisi la même adresse e-mail que celle que vous utilisez pour cet espace de travail, puis demandez à un administrateur de l'espace de travail de confirmer que vous en êtes membre. Consultez [Gérer les membres de l'espace de travail](/fr/administration/access/overview/managing-workspace-members/).

Pour passer à un autre espace de travail auquel vous appartenez, cliquez sur **Logout** et reconnectez-vous.

## Un projet, une table ou une dimension est introuvable

PlaidXL affiche ce que votre compte peut voir dans PlaidCloud. Si un projet est introuvable, demandez à son propriétaire de vous donner l'accès. Si une table est introuvable, vérifiez qu'elle existe dans le projet sélectionné et qu'elle a été chargée avec des données : une table dans laquelle rien n'a jamais été écrit affiche **Unable to get table metadata** lorsque vous la sélectionnez.

Les dossiers des listes de projets, de tables et de dimensions sont réduits au départ. Saisissez une partie du nom dans la zone de filtre en haut de la liste pour trouver un élément situé dans un dossier.

## Une table s'affiche en rouge

La table compte plus de lignes ou de colonnes qu'une feuille de calcul Excel ne peut en contenir. Sélectionnez **Avancé** pour filtrer les lignes et décochez les colonnes dont vous n'avez pas besoin, jusqu'à ce qu'elle tienne. Consultez [Tables affichées en rouge](/fr/reference/cli/plaidxl/retrieve/#tables-affichées-en-rouge).

## Une récupération est lente

Excel est le plus lent avec les tables larges. Décochez les colonnes dont vous n'avez pas besoin et filtrez les lignes avec **Avancé**. Ne récupérer que les données avec lesquelles vous travaillez est plus rapide et produit un classeur plus léger.

## Une formule affiche une erreur

| Ce que vous voyez | Ce qu'il faut vérifier |
|---|---|
| `#SPILL!` | Quelque chose occupe les cellules dont le résultat a besoin. Effacez les cellules situées sous la formule ou à côté. |
| `#NAME?` | Excel ne reconnaît pas la fonction. Vérifiez que PlaidXL est installé (l'onglet **PlaidCloud** figure dans le ruban) et contrôlez l'orthographe par rapport à [la liste des fonctions](/fr/reference/cli/plaidxl/functions/). |
| Une erreur provenant d'une fonction `PLAIDXL` | Vérifiez que vous êtes connecté et que le bon projet est sélectionné, puis contrôlez chaque nom de table, de colonne, de dimension et de nœud par rapport à PlaidCloud : les noms doivent correspondre exactement. |
| `CELL` indique qu'une colonne de filtre est introuvable | Le premier argument de `DIMENSION_REPR` est une colonne de la table, et non une dimension. Utilisez exactement le nom de la colonne de la table. Consultez [Valeurs](/fr/reference/cli/plaidxl/functions/#valeurs). |
| `CELL` renvoie 0 ou un total inattendu | Contrôlez le nom du nœud par rapport à la dimension : un nœud qui n'existe pas ne consolide rien et renvoie 0. Un nœud ne se consolide que sur une colonne liée à sa dimension ; sur toute autre colonne, il doit correspondre exactement à une valeur. |
| Les valeurs ne changent pas après une modification des données ou du projet | Forcez un recalcul complet : sous Windows, **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` renvoie une erreur | Utilisez l'une des valeurs `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, en minuscules. |

## Les formules renvoient les données d'un autre projet

Les fonctions PlaidXL lisent le projet sélectionné dans le volet des tâches, et cette sélection est partagée par tous les classeurs que vous avez ouverts. Sélectionnez le projet pour lequel le rapport a été conçu, puis forcez un recalcul complet. **Définir par défaut** enregistre un projet dans le classeur, qui est ainsi sélectionné lorsque vous y ouvrez le volet des tâches. Consultez [Définir un projet par défaut](/fr/reference/cli/plaidxl/retrieve/#définir-un-projet-par-défaut).

## Voir aussi

- [Installer PlaidXL](/fr/reference/cli/plaidxl/install/)
- [Se connecter à PlaidXL](/fr/reference/cli/plaidxl/connect/)
- [Obtenir de l'aide](/fr/guides/support/getting-help/) — ouvrir un ticket d'assistance
