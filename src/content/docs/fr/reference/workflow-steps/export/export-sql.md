---
title: Étape Export to SQL
description: Exportez des données vers des bases de données SQL externes depuis une étape de workflow PlaidCloud pour charger les résultats dans des systèmes de base de données en aval.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Description



Écrit une table de projet PlaidCloud dans un compte de documents sous la forme d'un fichier SQL contenant des instructions CREATE TABLE et INSERT. Utile lorsque vous devez transmettre des données à un système qui ingère des scripts SQL plutôt que du CSV ou du Parquet.

Pour charger directement dans une base de données distante, utilisez plutôt l'étape d'exportation de base de données appropriée ou [Agent Remote Import](/fr/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) : elles sont plus rapides et ne nécessitent pas de fichier intermédiaire.

## Aperçu

**Aperçu** affiche jusqu'à 100 lignes de la requête que l'étape lit dans la table source, sans l'exécuter. Cliquez sur **Aperçu** dans l'onglet **Source**. S'il y a davantage de lignes, l'aperçu indique qu'il affiche les premières lignes et qu'il faut exécuter l'étape pour toutes les lire. L'aperçu renseigne les variables de la même manière qu'une exécution, mais ne prend pas en charge les formats de variables comme `{x:>9}`.

L'aperçu ne fait que lire des données. Si la requête utilise une fonction que l'aperçu ne peut pas vérifier comme étant en lecture seule, il affiche *Preview only supports standard SQL functions. Run the step to see results.* Exécutez l'étape pour voir le résultat. L'aperçu n'est pas disponible sur un projet verrouillé.

## Paramètres supplémentaires

Dans **Ordre des lignes**, **Trier les lignes par** (`sort_columns`) trie les lignes écrites selon ces colonnes source, première clé en premier, chacune avec un réglage **Colonne**, **Croissant** et **Valeurs nulles**. Une colonne clé n'a pas besoin d'être écrite. **Valeurs nulles** place par défaut les valeurs en premier en tri croissant et en dernier en tri décroissant. Ce paramètre n'est pas utilisé avec **Résumer** ni **Distinct**.

## Exemples


Aucun exemple pour le moment...
