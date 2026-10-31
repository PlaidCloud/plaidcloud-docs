---
title: Dimension Export
description: "Exportez les données d'une dimension PlaidCloud dans une étape de workflow pour enregistrer des structures hiérarchiques sous forme de fichiers ou les transférer vers d'autres systèmes."
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-export.md
---

## Description

Aplatit une dimension en une table PlaidCloud tabulaire : une ligne par membre, avec des colonnes pour le parent, le niveau, la valeur, les alias et les propriétés. Utilisez cette étape lorsque vous devez interroger la structure de la dimension, la joindre ou l'alimenter vers des systèmes en aval qui ne peuvent pas lire directement le format hiérarchique de PlaidCloud.

Usage courant : exporter la dimension sous forme de table, puis l'écrire dans un système externe (outil de BI, base de données de reporting, remise de fichiers) à l'aide d'une étape d'export classique.

## Exporter toutes les hiérarchies

Choisissez **Toutes les hiérarchies** pour regrouper toutes les hiérarchies dans une seule table. Le résultat gagne une colonne `hierarchy` qui indique la hiérarchie de chaque ligne ; les lignes sont triées avec la hiérarchie principale en premier, suivie des hiérarchies alternatives par ordre alphabétique.
