---
title: Étape Export to SQL
description: Exportez des données vers des bases de données SQL externes depuis une étape de workflow PlaidCloud pour charger les résultats dans des systèmes de base de données en aval.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Description



Écrit une table de projet PlaidCloud dans un compte de documents sous forme de fichier SQL contenant des instructions CREATE TABLE et INSERT. Utile lorsque vous devez transmettre des données à un système qui ingère des scripts SQL plutôt que du CSV ou du Parquet.

Pour charger directement dans une base de données distante, utilisez plutôt l'étape d'exportation de base de données appropriée ou [Agent Remote Import](/fr/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) : elles sont plus rapides et ne nécessitent pas de fichier intermédiaire.

## Paramètres supplémentaires

Dans **Ordre des lignes**, **Trier les lignes par** (`sort_columns`) ordonne les lignes écrites selon ces colonnes source, la première clé en premier, chacune avec un paramètre **Colonne**, **Croissant** et **Valeurs nulles**. Une colonne de clé n'a pas besoin d'être écrite. **Valeurs nulles** vaut par défaut « en premier » en ordre croissant et « en dernier » en ordre décroissant. Il n'est pas utilisé avec **Résumer** ou **Distinct**.

## Exemples


Aucun exemple pour le moment...
