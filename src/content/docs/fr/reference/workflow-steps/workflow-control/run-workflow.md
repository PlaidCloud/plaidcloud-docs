---
title: Exécuter le workflow
description: Exécutez un workflow existant à partir d'une étape de workflow PlaidCloud pour enchaîner des exécutions de workflows et construire des pipelines de traitement multi-workflows.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-workflow.md
---

## Description

Déclenche un autre workflow dans le cadre de l'exécution du workflow en cours. Utilisez cette étape pour enchaîner des workflows lorsqu'un processus dépend logiquement d'un autre — par exemple, un workflow de « clôture de fin de mois » qui appelle un workflow « chargement des réels », puis un workflow « exécution des allocations », puis un workflow « publication des tableaux de bord ».

Le workflow appelé s'exécute de façon indépendante — il peut se trouver dans le même projet ou dans un autre. Par défaut, le workflow appelant continue sans attendre ; activez l'option **Attendre la fin du traitement** si les étapes suivantes de l'appelant dépendent de la fin du workflow appelé.



## Workflow à exécuter


Sélectionnez d'abord le projet qui contient le workflow à exécuter dans la liste déroulante **Projet**.



Sélectionnez ensuite le workflow à exécuter dans la liste déroulante **Workflow**.



Il existe en outre une option **Attendre la fin du traitement avant de continuer.** Si vous cochez cette case, l'exécution du workflow en cours est différée jusqu'à la fin de l'exécution du workflow appelé. Cette option est désactivée par défaut : le workflow en cours qui contient cette transformation continue alors son traitement en parallèle du workflow appelé.







## Exemples

Pas encore d'exemples…
