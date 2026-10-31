---
title: FUSE_ENCODING (Lakehouse v1)
description: FUSE_ENCODING — retorna os tipos de codificação aplicados a uma coluna específica de uma tabela.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-encoding.md
---

Retorna os tipos de codificação aplicados a uma coluna específica de uma tabela. Ajuda você a entender como os dados são compactados e armazenados em formato nativo na tabela.

## Sintaxe SQL

```sql
FUSE_ENCODING('<database_name>', '<table_name>', '<column_name>')
```

A função retorna um conjunto de resultados com as seguintes colunas:

| Coluna            | Tipo de dados    | Descrição                                                                                                                                                                              |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALIDITY_SIZE     | Nullable(UInt32) | O tamanho de um valor de bitmap que indica se cada linha da coluna tem um valor não nulo. Esse bitmap é usado para rastrear a presença ou ausência de valores nulos nos dados da coluna. |
| COMPRESSED_SIZE   | UInt32           | O tamanho dos dados da coluna após a compactação.                                                                                                                                           |
| UNCOMPRESSED_SIZE | UInt32           | O tamanho dos dados da coluna antes de aplicar a codificação.                                                                                                                                    |
| LEVEL_ONE         | String           | A codificação primária ou inicial aplicada à coluna.                                                                                                                                   |
| LEVEL_TWO         | Nullable(String) | Um método de codificação secundário ou recursivo aplicado à coluna após a codificação inicial.                                                                                               |

## Exemplos de SQL

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
