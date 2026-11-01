---
title: Installer PlaidXL
description: Ajoutez le complément PlaidXL à Excel sous Windows ou Mac, repérez l'onglet PlaidCloud du ruban et ouvrez le volet des tâches PlaidXL.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

Vous installez PlaidXL une seule fois par ordinateur, et non une fois par classeur. Ensuite, l'onglet **PlaidCloud** figure dans le ruban Excel de chaque classeur que vous ouvrez.

## Avant de commencer

- Utilisez Excel pour Microsoft 365, ou Excel 2021 ou version ultérieure, sous Windows ou Mac.
- Si votre organisation gère les compléments Office de manière centralisée, votre administrateur Microsoft 365 devra peut-être déployer PlaidXL pour vous. Si vous ne pouvez pas installer vous-même des compléments, demandez-lui d'ajouter le complément **PlaidCloud**.

## Installer sous Windows

1. Dans Excel, ouvrez **Insert → Add-ins** (dans certaines versions, **Home → Add-ins**).
2. Saisissez `PlaidCloud` dans la zone de recherche de compléments.
3. Sélectionnez le complément **PlaidCloud** et cliquez sur **Ajouter**.

## Installer sous Mac

1. Dans Excel pour Mac, ouvrez **Insert → Add-ins**. Dans les anciennes versions, le menu est **Insert → Store**.
2. Saisissez `PlaidCloud` dans la zone de recherche de compléments.
3. Sélectionnez le complément **PlaidCloud** et cliquez sur **Ajouter**.

## Ouvrir le volet des tâches

1. Cliquez sur l'onglet **PlaidCloud** du ruban.
2. Dans le groupe **Data**, cliquez sur **Open PlaidXL**.

Le volet des tâches PlaidXL s'ouvre sur le côté droit de la fenêtre et vous invite à vous connecter. Poursuivez avec [Connexion](/fr/reference/cli/plaidxl/connect/).

Le volet des tâches reste connecté d'une session à l'autre§T; en général, vous vous connectez donc une seule fois, puis vous ouvrez simplement le volet des tâches quand vous en avez besoin.

## Si PlaidXL n'apparaît pas

- Fermez toutes les fenêtres Excel, puis rouvrez Excel. Un complément n'apparaît souvent dans le ruban qu'après le redémarrage d'Excel.
- Regardez sous **Insert → My Add-ins** (Windows) ou **Insert → Add-ins → My Add-ins** (Mac) et sélectionnez-y **PlaidCloud**.
- Si votre organisation bloque les compléments provenant du store, demandez à votre administrateur Microsoft 365 de le déployer.

Vous trouverez d'autres solutions sur la page [Dépannage](/fr/reference/cli/plaidxl/troubleshooting/).

## Voir aussi

- [Connexion](/fr/reference/cli/plaidxl/connect/) — connecter le complément à votre espace de travail
- [Le ruban PlaidCloud](/fr/reference/cli/plaidxl/ribbon/) — toutes les commandes de l'onglet **PlaidCloud**
