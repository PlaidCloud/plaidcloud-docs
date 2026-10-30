---
title: FUSE_ENCODING (Lakehouse v1)
description: FUSE_ENCODING — 테이블의 특정 열에 적용된 인코딩 유형을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-encoding.md
---

테이블의 특정 열에 적용된 인코딩 유형을 반환합니다. 테이블 내에서 데이터가 네이티브 형식으로 압축되고 저장되는 방식을 이해하는 데 도움이 됩니다.

## SQL 구문

```sql
FUSE_ENCODING('<database_name>', '<table_name>', '<column_name>')
```

이 함수는 다음 열로 구성된 결과 집합을 반환합니다.

| 열 | 데이터 유형 | 설명 |
|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VALIDITY_SIZE     | Nullable(UInt32) | 열의 각 행에 null이 아닌 값이 있는지를 나타내는 비트맵 값의 크기입니다. 이 비트맵은 열 데이터에서 null 값의 존재 여부를 추적하는 데 사용됩니다. |
| COMPRESSED_SIZE   | UInt32           | 압축 후 열 데이터의 크기입니다. |
| UNCOMPRESSED_SIZE | UInt32           | 인코딩을 적용하기 전 열 데이터의 크기입니다. |
| LEVEL_ONE         | String           | 열에 적용된 기본(초기) 인코딩입니다. |
| LEVEL_TWO         | Nullable(String) | 초기 인코딩 이후 열에 적용된 보조(재귀) 인코딩 방법입니다. |

## SQL 예제

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
