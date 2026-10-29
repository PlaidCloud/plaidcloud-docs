---
title: FUSE_ENCODING（Lakehouse v1）
description: FUSE_ENCODING — テーブル内の特定の列に適用されているエンコード方式を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-encoding.md
---

テーブル内の特定の列に適用されているエンコード方式を返します。テーブル内でデータがどのように圧縮され、ネイティブ形式で格納されているかを把握するのに役立ちます。

## SQLの構文

```sql
FUSE_ENCODING('<database_name>', '<table_name>', '<column_name>')
```

この関数は、次の列を持つ結果セットを返します。

| 列            | データ型        | 説明                                                                                                                                                                              |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALIDITY_SIZE     | Nullable(UInt32) | 列の各行がNULLでない値を持つかどうかを示すビットマップ値のサイズ。このビットマップは、列のデータにおけるNULL値の有無を追跡するために使用されます。 |
| COMPRESSED_SIZE   | UInt32           | 圧縮後の列データのサイズ。                                                                                                                                           |
| UNCOMPRESSED_SIZE | UInt32           | エンコードを適用する前の列データのサイズ。                                                                                                                                    |
| LEVEL_ONE         | String           | 列に適用される第1段階（最初）のエンコード。                                                                                                                                   |
| LEVEL_TWO         | Nullable(String) | 最初のエンコードの後に列に適用される、第2段階または再帰的なエンコード方式。                                                                                               |

## SQLの例

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
