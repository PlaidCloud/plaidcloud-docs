---
title: FUSE_ENCODING (Lakehouse v1)
description: FUSE_ENCODING：返回应用于表中特定列的编码类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-encoding.md
---

返回应用于表中特定列的编码类型。它可帮助您了解数据在表中如何以原生格式压缩和存储。

## SQL 语法

```sql
FUSE_ENCODING('<database_name>', '<table_name>', '<column_name>')
```

该函数返回包含以下列的结果集：

| 列 | 数据类型 | 说明 |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALIDITY_SIZE | Nullable(UInt32) | 位图值的大小，该位图指示列中每一行是否有非空值，用于跟踪列数据中空值的有无。 |
| COMPRESSED_SIZE | UInt32 | 压缩后列数据的大小。 |
| UNCOMPRESSED_SIZE | UInt32 | 应用编码前列数据的大小。 |
| LEVEL_ONE | String | 应用于该列的主要（初始）编码。 |
| LEVEL_TWO | Nullable(String) | 在初始编码之后应用于该列的次级（递归）编码方法。 |

## SQL 示例

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
