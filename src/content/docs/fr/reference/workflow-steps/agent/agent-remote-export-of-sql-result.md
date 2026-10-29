---
title: Agent Remote Export of SQL Result
description: Exportez des résultats de requêtes SQL à distance via un agent PlaidLink dans les workflows PlaidCloud pour une extraction de données sécurisée derrière un pare-feu.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-export-of-sql-result.md
---

## Description



Exécute du SQL sur une base de données distante via un agent PlaidLink et ramène le jeu de résultats dans PlaidCloud sous forme de table de projet. À utiliser lorsque la base de données source ne peut pas être atteinte directement depuis PlaidCloud (pare-feu, VPN uniquement, sur site) mais que vous voulez tout de même en extraire des données.

L'agent exécute la requête sur site et transmet le résultat en flux continu à PlaidCloud ; les identifiants comme les données restent donc sur votre réseau jusqu'à ce que le résultat soit nécessaire.


## Exemples

Pas encore d'exemples...
