---
title: Gérer les variables de workflow
description: Gérez les variables de workflow dans PlaidCloud pour stocker et transmettre des valeurs dynamiques entre les étapes et obtenir une logique de traitement des données flexible.
sidebar:
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/manage-workflow-variables.md
---

PlaidCloud permet de définir des variables à la fois à la portée du projet et à celle du workflow. Cela permet de définir des variables à l'échelle du projet ou de transmettre facilement des informations d'un workflow à l'autre. Les variables et leurs valeurs s'affichent en cliquant sur l'icône des variables dans la hiérarchie **Workflows**.



Depuis la table des variables, vous pouvez consulter les variables et leurs valeurs actuelles, et modifier ces valeurs. Vous pouvez aussi ajouter de nouvelles variables ou supprimer des variables existantes.

## Variables intégrées

Les paramètres et expressions des étapes peuvent utiliser ces variables intégrées sans les définir :

| Variable | Valeur |
|---|---|
| `{project}`, `{model}`, `{cloud}` | Les noms du projet, du modèle et de l'espace de travail. |
| `{date}` | L'heure UTC actuelle de l'exécution, en format long, par exemple `Wednesday, 11 November 2026 10:30PM UTC +0`. |
| `{date_iso}` | Le même instant au format ISO 8601, par exemple `2026-11-12T22:49:56+00:00`. |

Utilisez `{date_iso}` lorsqu'une expression doit lire une partie de la date. Ses 7 premiers caractères donnent le mois (`2026-11`) et ses 10 premiers le jour (`2026-11-12`). `{date_iso}` fonctionne partout où `{date}` fonctionne, y compris dans les modèles d'e-mail de notification et dans les étapes Prévision, Parity et Solveur.
