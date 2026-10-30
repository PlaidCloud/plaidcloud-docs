---
title: Calculate and Export PCM Model
description: Exécutez le calcul d'un modèle PCM et exportez le résultat vers une base de données ou un fichier délimité, via un agent PlaidLink.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/export-pcm-model.md
---

## Description

Calcule un modèle SAP PCM et exporte le résultat en une seule étape, via un [agent PlaidLink](/fr/reference/workflow-steps/agent/) ayant accès à l'installation PCM. Alors que [Calculate PCM Model](/fr/reference/workflow-steps/sap-pcm/calculate-pcm-model/) (étape) ne fait qu'exécuter le calcul, cette étape déplace aussi la sortie.

## Configuration

### Agent à utiliser

L'agent PlaidLink qui accède à l'installation PCM.

### Informations sur le modèle

- **Nom du modèle** : le modèle PCM à calculer.
- **Chemin de la spécification d'exportation** : la spécification d'exportation PCM qui décrit ce qu'il faut exporter.

### Destination de sortie de l'exportation

Choisissez une cible de base de données, une cible de fichier, ou les deux.

**Vers une base de données** : activé par défaut ; l'exportation écrit via la cible de base de données configurée dans la spécification.

**Vers un fichier** : désactivé par défaut. Lorsqu'il est activé :

- **Chemin du fichier** : l'emplacement où l'agent écrit le fichier.
- **Alias** : l'alias consigné dans l'exportation. Par défaut, `DEFAULT ALIAS`.
- **Précision** : le nombre de décimales des valeurs exportées. Par défaut, 0.
- **Délimiteur** : virgule, tabulation, barre verticale, point-virgule, espace, `@`, `~` ou `:`. Par défaut, la tabulation.
- **Ajouter à la fin** : désactivé par défaut, de sorte que chaque exécution remplace le fichier. Activez-le pour cumuler les exécutions.
- **Inclure les règles** : désactivé par défaut. Activez-le pour exporter les règles du modèle avec les valeurs.
- **Unicode** : désactivé par défaut. Activez-le lorsque les données exportées contiennent des caractères hors de l'encodage par défaut.

## Voir aussi

- [Étapes SAP-PCM](/fr/reference/workflow-steps/sap-pcm/)
- [Calculate PCM Model](/fr/reference/workflow-steps/sap-pcm/calculate-pcm-model/) (étape)
- [Run SAP PCM Hyper Loader](/fr/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader/) (étape)
