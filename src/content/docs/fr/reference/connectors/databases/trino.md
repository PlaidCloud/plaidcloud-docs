---
title: Trino
description: Configurez une connexion à un moteur de requêtes distribué Trino dans PlaidCloud pour exécuter des requêtes fédérées sur plusieurs sources de données.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/trino.md
---

**Trino** (anciennement PrestoSQL) est le moteur de requêtes SQL distribué couramment utilisé sur les data lakes. Utilisez ce connecteur pour interroger des déploiements Trino depuis des workflows PlaidCloud. L'authentification utilise HTTP Basic Auth ou JWT ; le catalogue et le schéma que vous ciblez déterminent la source de données sous-jacente interrogée.

## Documentation officielle
[La documentation de Trino](https://trino.io/docs/current/index.html).

## Configuration

Ce connecteur utilise un flux d'authentification propre à l'éditeur et se configure directement depuis l'écran **Connexions** de votre espace de travail. Les champs de configuration affichés dépendent des identifiants que l'administrateur de votre tenant a provisionnés pour l'intégration.

Consultez la [documentation de Trino](https://trino.io/docs/current/) pour connaître les dernières précisions sur la configuration.

Si vous avez besoin d'aide pour configurer ce connecteur pour votre tenant, contactez votre équipe commerciale : les identifiants propres au connecteur, les URL d'environnement et tout provisionnement préalable requis doivent généralement être coordonnés avec le support PlaidCloud.
