---
title: Installer PlaidXL
description: Ajoutez le complément PlaidXL à Excel sous Windows ou Mac, repérez l'onglet PlaidCloud du ruban et ouvrez le volet des tâches PlaidXL.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

Vous installez PlaidXL une seule fois par ordinateur, et non une fois par classeur. Ensuite, l'onglet **PlaidCloud** apparaît dans le ruban Excel de chaque classeur que vous ouvrez.

## Avant de commencer

- Utilisez Excel pour Microsoft 365, ou Excel 2021 ou version ultérieure, sous Windows ou Mac.
- Si votre organisation gère les compléments Office de manière centralisée, votre administrateur Microsoft 365 devra peut-être déployer PlaidXL pour vous. Si vous ne pouvez pas installer de compléments vous-même, demandez-lui d'ajouter le complément **PlaidCloud**.

## Installer sous Windows

1. Dans Excel, ouvrez **Insert → Add-ins** (dans certaines versions, **Home → Add-ins**).
2. Saisissez `PlaidCloud` dans la zone de recherche de compléments.
3. Sélectionnez le complément **PlaidCloud**, puis cliquez sur **Add**.

## Installer sous Mac

1. Dans Excel pour Mac, ouvrez **Insert → Add-ins**. Dans les versions plus anciennes, le menu est **Insert → Store**.
2. Saisissez `PlaidCloud` dans la zone de recherche de compléments.
3. Sélectionnez le complément **PlaidCloud**, puis cliquez sur **Add**.

## Ouvrir le volet des tâches

1. Cliquez sur l'onglet **PlaidCloud** du ruban.
2. Dans le groupe **PlaidXL Controls**, cliquez sur **Show Taskpane**.

Le volet des tâches PlaidXL s'ouvre sur le côté droit de la fenêtre et vous invite à vous connecter. Poursuivez avec [Connexion](/fr/reference/cli/plaidxl/connect/).

Le volet des tâches reste connecté d'une session à l'autre : en général, vous vous connectez une seule fois, puis vous n'avez plus qu'à ouvrir le volet des tâches lorsque vous en avez besoin.

## Si PlaidXL n'apparaît pas

- Fermez toutes les fenêtres Excel, puis rouvrez Excel. Un complément n'apparaît souvent dans le ruban qu'après un redémarrage d'Excel.
- Consultez **Insert → My Add-ins** (Windows) ou **Insert → Add-ins → My Add-ins** (Mac), puis sélectionnez-y **PlaidCloud**.
- Si votre organisation bloque les compléments provenant du store, demandez à votre administrateur Microsoft 365 de le déployer.

D'autres solutions sont disponibles sur la page [Dépannage](/fr/reference/cli/plaidxl/troubleshooting/).

## Voir aussi

- [Connexion](/fr/reference/cli/plaidxl/connect/) — connecter le complément à votre espace de travail
- [Le ruban PlaidCloud](/fr/reference/cli/plaidxl/ribbon/) — toutes les commandes de l'onglet **PlaidCloud**
