---
title: Apache Doris
description: Configurez une connexion à une base de données Apache Doris dans PlaidCloud pour exécuter des requêtes analytiques en temps réel sur de grands jeux de données.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/doris.md
---

**Apache Doris** est la base de données analytique MPP hautes performances dont StarRocks est issu par fork. Utilisez ce connecteur pour interroger des déploiements Doris depuis des workflows PlaidCloud. La connexion utilise le protocole filaire MySQL avec une authentification standard par nom d'utilisateur et mot de passe.

## Documentation en amont
[Documentation d'Apache Doris](https://doris.apache.org/docs/4.x/gettingStarted/what-is-apache-doris).

La [page d'accueil du projet Apache Doris](https://doris.apache.org/).

## Configuration

Ce connecteur utilise un flux d'authentification propre au fournisseur et se configure directement depuis l'écran **Connexions** de votre espace de travail. Les champs de configuration affichés dépendent des identifiants que l'administrateur de votre tenant a provisionnés pour l'intégration.

Consultez la [documentation de doris](https://doris.apache.org/docs/) en amont pour connaître les dernières précisions sur la configuration.

Si vous avez besoin d'aide pour configurer ce connecteur pour votre tenant, contactez votre équipe commerciale : les identifiants propres au connecteur, les URL d'environnement et tout provisionnement préalable requis doivent généralement être coordonnés avec le support PlaidCloud.
