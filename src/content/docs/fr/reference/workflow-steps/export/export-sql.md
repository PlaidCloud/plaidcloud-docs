---
title: Étape Export to SQL
description: Exportez des données vers des bases de données SQL externes à partir d'une étape de workflow PlaidCloud afin de charger les résultats dans des systèmes de base de données en aval.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Description



Écrit une table de projet PlaidCloud dans un compte de documents sous la forme d'un fichier SQL contenant des instructions CREATE TABLE et INSERT. Utile pour transmettre des données à un système qui ingère des scripts SQL plutôt que des fichiers CSV ou Parquet.

Pour charger les données directement dans une base de données distante, utilisez plutôt l'étape de base de données appropriée pour l'exportation ou l'étape [Agent Remote Import](/fr/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/). Ces étapes sont plus rapides et ne nécessitent pas de fichier intermédiaire.

## Aperçu

**Aperçu** dans l'onglet **Source** affiche jusqu'à 100 lignes de la table source sans exécuter l'étape. Si la table contient davantage de lignes, l'aperçu indique qu'il affiche les premières lignes. Si la table source n'existe pas encore, l'aperçu indique qu'il n'y a rien à afficher. L'aperçu n'est pas disponible sur un projet verrouillé.

## Paramètres supplémentaires

Dans **Ordre des lignes**, **Trier les lignes par** (`sort_columns`) trie les lignes écrites selon ces colonnes sources, la première clé en premier, chacune avec un paramètre **Colonne**, **Croissant** et **Valeurs nulles**. Une colonne de clé n'a pas besoin d'être écrite. Par défaut, **Valeurs nulles** place les valeurs nulles en premier pour un tri croissant et en dernier pour un tri décroissant. Ce paramètre n'est pas utilisé avec **Résumer** ni **Distinct**.

## Exemples


Aucun exemple pour l'instant...
