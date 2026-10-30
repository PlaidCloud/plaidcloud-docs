---
title: Agent Remote Import Table into SQL Database
description: Importez les données d'une table PlaidCloud dans des bases de données SQL distantes via un agent PlaidLink pour un chargement de données sécurisé derrière un pare-feu.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database.md
---

## Description



Envoie une table de projet PlaidCloud vers une base de données accessible uniquement par un agent PlaidLink. L'agent reçoit les données de PlaidCloud et effectue le chargement localement, ce qui est utile pour garder une base de données opérationnelle sur site synchronisée avec les analyses PlaidCloud.

Usage typique : PlaidCloud produit une prévision ou un résultat d'allocation actualisé, et l'agent le charge dans l'ERP, le data mart ou la base de données de reporting opérationnel sur site.


## Comment les données parviennent à l'agent

Un agent PlaidLink en version 1.2.33 ou ultérieure reçoit les lignes de la table sous la forme d'un seul fichier Parquet. Les nombres, les dates, les horodatages et les valeurs booléennes arrivent avec leur propre type. Les autres colonnes, comme les colonnes d'heure, d'intervalle et JSON, arrivent sous forme de texte. Une valeur de texte vide arrive vide (NULL), comme toujours.

Un agent plus ancien reçoit les lignes sous la forme d'un fichier compressé au format zip, délimité par des tabulations, comme auparavant. [Mettez à niveau l'agent](/fr/reference/cli/plaidlink/upgrade/) pour recevoir du Parquet.

## Exemples

Pas encore d'exemples...
