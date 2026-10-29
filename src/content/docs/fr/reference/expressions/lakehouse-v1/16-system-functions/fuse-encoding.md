---
title: FUSE_ENCODING (Lakehouse v1)
description: FUSE_ENCODING — renvoie les types d'encodage appliqués à une colonne donnée d'une table.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-encoding.md
---

Renvoie les types d'encodage appliqués à une colonne donnée d'une table. Cela vous aide à comprendre comment les données sont compressées et stockées au format natif dans la table.

## Syntaxe SQL

```sql
FUSE_ENCODING('<database_name>', '<table_name>', '<column_name>')
```

La fonction renvoie un jeu de résultats comportant les colonnes suivantes :

| Colonne           | Type de données  | Description                                                                                                                                                                              |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALIDITY_SIZE     | Nullable(UInt32) | La taille d'une valeur bitmap qui indique si chaque ligne de la colonne a une valeur non nulle. Ce bitmap sert à suivre la présence ou l'absence de valeurs nulles dans les données de la colonne. |
| COMPRESSED_SIZE   | UInt32           | La taille des données de la colonne après compression.                                                                                                                                   |
| UNCOMPRESSED_SIZE | UInt32           | La taille des données de la colonne avant application de l'encodage.                                                                                                                     |
| LEVEL_ONE         | String           | L'encodage principal ou initial appliqué à la colonne.                                                                                                                                   |
| LEVEL_TWO         | Nullable(String) | Une méthode d'encodage secondaire ou récursive appliquée à la colonne après l'encodage initial.                                                                                          |

## Exemples SQL

```sql
-- Create a table with an integer column 'c' and apply 'Lz4' compression
CREATE TABLE t(c INT) STORAGE_FORMAT = 'native' COMPRESSION = 'lz4';

-- Insert data into the table.
INSERT INTO t SELECT number FROM numbers(2048);

-- Analyze the encoding for column 'c' in table 't'
SELECT LEVEL_ONE, LEVEL_TWO, COUNT(*) 
FROM FUSE_ENCODING('default', 't', 'c') 
GROUP BY LEVEL_ONE, LEVEL_TWO;

level_one   |level_two|count(*)|
------------+---------+--------+
DeltaBitpack|         |       1|

--  Insert 2,048 rows with the value 1 into the table 't'
INSERT INTO t (c)
SELECT 1
FROM numbers(2048);

SELECT LEVEL_ONE, LEVEL_TWO, COUNT(*) 
FROM FUSE_ENCODING('default', 't', 'c') 
GROUP BY LEVEL_ONE, LEVEL_TWO;

level_one   |level_two|count(*)|
------------+---------+--------+
OneValue    |         |       1|
DeltaBitpack|         |       1|
```
