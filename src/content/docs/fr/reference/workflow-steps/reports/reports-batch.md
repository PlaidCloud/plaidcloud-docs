---
title: Reports Batch
description: Génère des rapports PDF par lot à partir d'une étape de workflow PlaidCloud, afin de produire plusieurs rapports à partir de modèles et de données d'entrée variables.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/reports-batch.md
---

## Description



Génère de nombreux rapports PDF à partir d'un seul modèle RML, pilotés par une table de contrôle. Un rapport est produit pour chaque ligne de la table de contrôle, et les valeurs des colonnes de la ligne servent de paramètres à la génération de ce rapport.

Cas d'usage courants : relevés clients (un PDF par client), états financiers par unité (un PDF par unité opérationnelle), factures (un PDF par commande). Comparez avec [Report Single](/fr/reference/workflow-steps/reports/report-single/) (étape) pour la génération ponctuelle d'un rapport.


## Noms lus par le modèle

Le modèle lit chaque source de l'onglet **Données du rapport**, et chaque colonne cible du mappage **Source de données des valeurs d'enregistrement du lot**, par son nom. Il n'y a pas de section de constantes : chaque ligne du lot fournit au modèle les valeurs de son rapport. Les nouvelles sources se nomment `new_source`, `new_source_2`, etc., et le modèle peut les lire telles quelles.


## Contrôles effectués à l'enregistrement

Le nom de chaque source et de chaque colonne du lot doit être renseigné, unique et lisible par le modèle, selon les mêmes règles que pour [Report Single](/fr/reference/workflow-steps/reports/report-single/) (étape), les colonnes du lot remplaçant les constantes : *Batch column name 'unit id' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*

Si vous enregistrez avec une table source de lot choisie mais un mappage de lot vide, le mappage est rempli à partir de cette table, comme le ferait Populate.


## Table de lot vide

Lorsque la table source du lot ne contient aucune ligne, l'étape se termine avec succès et affiche un avertissement qui nomme la table du lot ; aucun rapport n'est produit.


## Exemples

Aucun exemple pour le moment...
