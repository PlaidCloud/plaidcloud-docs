---
title: Gestion des données — tabulaires
description: Gérez les données tabulaires dans PlaidCloud à l'aide de tables, de vues et du moteur Lakehouse hautes performances, pour traiter des données à toute échelle.
sidebar:
  label: Vue d'ensemble
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

La couche de données de PlaidCloud repose sur les **tables** (données structurées en lignes et en colonnes) et les **vues** (requêtes enregistrées sur des tables). Les deux résident dans un projet et s'appuient sur le moteur Lakehouse, qui s'adapte aussi bien aux petites tables de référence qu'aux jeux de données analytiques d'un milliard de lignes, sans modification de configuration.

## Contenu de cette section

- [Tables et vues](/fr/guides/data/tables-views/) — ce qu'est chacune, quand utiliser l'une ou l'autre et comment elles interagissent
- [Explorateur de tables](/fr/guides/data/table-explorer/) — parcourez et inspectez les tables de votre projet
- [Type de données Currency](/fr/guides/data/currency-data-type/) — un type de colonne exact, de demi-largeur, pour les montants monétaires, et quand le préférer à Numeric
- [Type de données Vector](/fr/guides/data/vector-data-type/) — stockez des embeddings précalculés dans une table de projet, déclarez la largeur attendue et recherchez les lignes les plus proches
- [Instantanés de table](/fr/guides/data/table-snapshots/) — parcourez l'historique des instantanés, affichez les données telles qu'elles étaient lors d'un instantané passé, et rétablissez ou restaurez une table
- [La fenêtre Lakehouse](/fr/guides/data/lakehouse-window/) — suivez et profilez les requêtes, parcourez les catalogues et les tables avec leurs instantanés, et copiez une requête de voyage dans le temps
- [Publier des données](/fr/guides/data/publish/) — mettez les tables du projet à la disposition des tableaux de bord, des outils de BI et des systèmes en aval, et consultez leurs recommandations de performances
- [Sélectionner le dernier enregistrement dans une grande table d'historique](/fr/guides/data/selecting-latest-record-in-large-history-table/) — un modèle courant, avec une solution attentive aux performances
- [API de géocodage](/fr/guides/data/geocoding-api/) — migrez une intégration de géocodage Google ou Mapbox vers les points de terminaison REST de géocodage de PlaidCloud
- [API de calcul d'itinéraires par temps de trajet](/fr/guides/data/drive-time-routing-api/) — aperçu sur activation : isochrones de temps de trajet et classement par temps de trajet le plus court via REST

## Origine des données

Les tables sont généralement alimentées par des **workflows** — des pipelines automatisés qui importent des données, les transforment et réécrivent les résultats. Consultez [Workflows](/fr/guides/workflows/) pour savoir comment les créer, et la [Référence des étapes de workflow](/fr/reference/workflow-steps/) pour tous les types d'étapes que vous pouvez utiliser.

Pour connecter des systèmes externes comme sources de données, consultez [Connexions (guide)](/fr/guides/connections/) et [Connecteurs (référence)](/fr/reference/connectors/).

## Voir aussi

- [Concepts](/fr/get-started/concepts/) — comment les tables s'articulent avec les workflows, les dimensions et le modèle de données plus large
- [Projets](/fr/guides/projects/) — les projets possèdent les tables ; une table n'existe pas en dehors d'un projet
- [Tableaux de bord](/fr/guides/dashboards/) — consomment les tables publiées pour la visualisation
