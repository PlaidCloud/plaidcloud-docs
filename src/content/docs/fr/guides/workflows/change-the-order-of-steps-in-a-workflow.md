---
title: Modifier l'ordre des étapes d'un workflow
description: Réorganisez les étapes d'un workflow PlaidCloud par glisser-déposer ou par ordonnancement manuel pour contrôler la séquence de traitement des données.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/change-the-order-of-steps-in-a-workflow.md
---

Il existe deux façons de modifier l'ordre des étapes dans le workflow. La première consiste à utiliser les flèches haut et bas présentes dans la table **Workflows** pour déplacer l'étape vers le haut ou vers le bas. La seconde consiste à utiliser l'option **Step Move**, qui facilite le déplacement d'une étape lorsque des changements importants sont nécessaires. L'option de déplacement d'étape permet de placer l'étape en haut, en bas ou après une étape donnée en une seule opération.

La structure d'un workflow ne peut contenir chaque étape qu'une seule fois. Si un workflow contient déjà, d'une manière ou d'une autre, la même étape en double, sa réorganisation — y compris le déplacement d'une étape par glisser-déposer vers une nouvelle position — est refusée avec une erreur indiquant que le workflow contient un doublon. Supprimez l'étape en double pour réparer le workflow ; la suppression d'étapes n'est pas restreinte, et la réorganisation fonctionne de nouveau normalement une fois le doublon supprimé.
