---
title: Gestion des données tabulaires
description: Gérez les données tabulaires dans PlaidCloud à l'aide de tables, de vues et du moteur Lakehouse haute performance, quel que soit le volume de données.
sidebar:
  label: Vue d'ensemble
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

La couche de données de PlaidCloud repose sur des **tables** (données structurées en lignes et colonnes) et des **vues** (requêtes enregistrées sur des tables). Les deux résident dans un projet et s'appuient sur le moteur Lakehouse, qui passe de petites tables de référence à des jeux de données analytiques de plusieurs milliards de lignes sans modification de configuration.

## Contenu de cette section

- [Tables et vues](/fr/guides/data/tables-views/) : ce que sont les unes et les autres, quand utiliser chacune et comment elles interagissent
- [Explorateur de tables](/fr/guides/data/table-explorer/) : parcourez et inspectez les tables de votre projet
- [Type de données Currency](/fr/guides/data/currency-data-type/) : un type de colonne exact, à demi-largeur, pour les montants monétaires, et quand le choisir plutôt que Numeric
- [Type de données Vector](/fr/guides/data/vector-data-type/) : stockez des embeddings précalculés dans une table de projet, déclarez la largeur attendue et recherchez les lignes les plus proches
- [Instantanés de table](/fr/guides/data/table-snapshots/) : parcourez l'historique des instantanés, affichez les données à la date d'un instantané passé, et rétablissez ou restaurez une table
- [Publication des données](/fr/guides/data/publish/) : mettez les tables d'un projet à disposition des tableaux de bord, des outils de BI et des systèmes en aval, et consultez leurs recommandations de performances
- [Sélectionner le dernier enregistrement d'une grande table d'historique](/fr/guides/data/selecting-latest-record-in-large-history-table/) : un schéma courant, avec une solution attentive aux performances
- [API de géocodage](/fr/guides/data/geocoding-api/) : migrez une intégration de géocodage Google ou Mapbox vers les points de terminaison REST de géocodage de PlaidCloud
- [API de routage par temps de trajet](/fr/guides/data/drive-time-routing-api/) : aperçu sur activation : isochrones de temps de trajet et classement par temps de trajet le plus court via REST

## D'où viennent les données

Les tables sont généralement alimentées par des **workflows**, des pipelines automatisés qui importent les données, les transforment et réécrivent les résultats. Consultez [Workflows](/fr/guides/workflows/) pour savoir comment les créer, et la [référence des étapes de workflow](/fr/reference/workflow-steps/) pour tous les types d'étapes disponibles.

Pour connecter des systèmes externes comme sources de données, consultez [Connexions (guide)](/fr/guides/connections/) et [Connecteurs (référence)](/fr/reference/connectors/).

## Voir aussi

- [Concepts](/fr/get-started/concepts/) : comment les tables s'articulent avec les workflows, les dimensions et le modèle de données au sens large
- [Projets](/fr/guides/projects/) : les projets possèdent les tables ; une table n'existe pas en dehors d'un projet
- [Tableaux de bord](/fr/guides/dashboards/) : exploitent les tables publiées pour la visualisation
