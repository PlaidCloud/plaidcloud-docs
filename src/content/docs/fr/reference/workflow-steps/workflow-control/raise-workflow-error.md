---
title: Déclencher une erreur de workflow
description: Déclenchez une erreur personnalisée dans une étape de workflow PlaidCloud pour activer la gestion des erreurs et interrompre l'exécution lorsque des conditions ne sont pas remplies.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/raise-workflow-error.md
---

## Description

Place le workflow dans un état d'erreur avec un message personnalisé. Utilisez cette étape lorsqu'une étape doit faire échouer le workflow à cause d'une condition sur les données détectée par des étapes précédentes — par exemple « échouer si le nombre de lignes est nul », « échouer si une table de validation des clés contient des valeurs non mappées » ou « échouer si un contrôle de solde ne se réconcilie pas ».

Associez-la à des [conditions d'étape](/fr/guides/workflows/step-conditions/) pour que l'erreur ne se déclenche que lorsqu'un problème existe réellement. Lorsque l'étape s'exécute, elle arrête immédiatement le workflow et écrit l'erreur dans le journal du workflow, ce qui peut à son tour déclencher le workflow de remédiation s'il est configuré.


## Déclencher une erreur de workflow


Principalement destinée à être utilisée avec des conditions d'étape, l'étape peut être configurée pour s'exécuter lorsque les conditions sont remplies et déclencher une erreur dans le workflow.
