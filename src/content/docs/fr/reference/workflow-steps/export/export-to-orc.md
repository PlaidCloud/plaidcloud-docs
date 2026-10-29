---
title: Étape Export to ORC
description: Exportez des tables de projet PlaidCloud vers un compte de documents sous forme de fichiers Apache ORC, en format colonnaire, avec le codec de compression de votre choix.
sidebar:
  order: 13.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-orc.md
---

## Description

Écrit des tables de projet dans un compte de documents sous forme de fichiers [Apache ORC](https://orc.apache.org/), un fichier par table. ORC est un format colonnaire lu par Hive, Spark et la plupart des plateformes de données cloud, le schéma étant inclus dans le fichier. Associez-le à [Import ORC](/fr/reference/workflow-steps/import/import-orc/).

Le formulaire de l'étape comporte une page **Paramètres du fichier** pour le fichier cible, le préfixe, la compression et le comportement si le fichier existe, ainsi qu'une page **Paramètres d'enregistrement** qui liste les tables à exporter, chacune avec sa propre sélection de données de table et ses propres filtres de données. Les [workflows KNIME migrés](/fr/guides/workflows/migrate-knime-workflows/) utilisent cette étape pour les écrivains ORC.

## Configuration

* **Fichier cible** (`output_file`) — le compte de documents et le dossier dans lesquels les fichiers sont écrits.
* **Préfixe du fichier cible** (`file_name`) — le préfixe du fichier. Chaque table est écrite sous la forme `<prefix><table name>.orc`.
* **Option de compression** (`compression`) — le codec ORC utilisé dans le fichier : **Snappy**, **zlib**, **gzip** (écrit sous la forme `zlib`), **Zstandard** ou **LZ4**. **Aucun** écrit le fichier sans compression.
* **Paramètres d'enregistrement** (`frames`) — les tables à exporter. Chaque frame porte ses propres paramètres de table ; un paramètre de niveau table placé en haut de l'étape plutôt que dans une frame n'est pas lu.
  * `id` — le libellé de la table dans les avertissements.
  * `source` — la table de projet à exporter. Chaque fichier en tire son nom.
  * `source_columns` et `target_columns` — les colonnes lues et les colonnes écrites, avec les éventuels renommages, types et agrégations par colonne.
  * `source_where` — un filtre sur les lignes sources.
  * `aggregate` et `aggregation_type` — résument les lignes ; `aggregation_type` est le résumé appliqué aux colonnes qui n'en définissent pas un propre.
  * `having` — un filtre sur les lignes résumées.
  * `distinct` — écrit uniquement les lignes distinctes.
  * `use_target_slicer`, `limit_target_start` et `limit_target_end` — écrivent uniquement les lignes comprises entre la position de début et la position de fin du résultat.
  * `sort_columns` — à définir avec un assistant IA ou l'API REST pour trier les lignes écrites selon ces colonnes sources, la première clé en premier, chacune sous la forme `{source, ascending, nulls}`. Une colonne clé n'a pas besoin d'être écrite. `nulls` vaut par défaut `first` en tri croissant et `last` en tri décroissant. Non utilisé avec `aggregate` ou `distinct`.
* **Un fichier qui existe déjà** (`if_exists`), sous **Si le fichier existe** — **L'écraser** (`overwrite`, par défaut) remplace un fichier déjà présent ; **Faire échouer l'étape sans rien écrire** (`fail`) arrête l'étape sans rien écrire lorsqu'un fichier qu'elle écrirait existe déjà.

## Voir aussi

- [Étapes d'exportation](/fr/reference/workflow-steps/export/)
- [Import ORC](/fr/reference/workflow-steps/import/import-orc/)
- [Export to Parquet](/fr/reference/workflow-steps/export/export-to-parquet/)
