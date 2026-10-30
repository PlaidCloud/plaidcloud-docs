---
title: INSPECT_PARQUET (Lakehouse v1)
description: INSPECT_PARQUET — 스테이징된 Parquet 파일의 포괄적인 메타데이터를 테이블로 가져옵니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/02-inspect-parquet.md
---

스테이징된 Parquet 파일의 포괄적인 메타데이터를 테이블로 가져옵니다. 테이블에는 다음 열이 포함됩니다.

| 열                               | 설명                                                           |
|----------------------------------|----------------------------------------------------------------|
| created_by                       | Parquet 파일을 생성한 주체 또는 출처 |
| num_columns                      | Parquet 파일의 열 수                      |
| num_rows                         | Parquet 파일의 전체 행 또는 레코드 수        |
| num_row_groups                   | Parquet 파일 내 행 그룹 수                |
| serialized_size                  | 디스크상의 Parquet 파일 크기(압축)              |
| max_row_groups_size_compressed   | 가장 큰 행 그룹의 크기(압축)                 |
| max_row_groups_size_uncompressed | 가장 큰 행 그룹의 크기(압축 해제)               |

## SQL 구문

```sql
INSPECT_PARQUET('@<path-to-file>')
```

## SQL 예제

이 예제는 스테이징된 샘플 Parquet 파일 [books.parquet](https://datafuse-1253727613.cos.ap-hongkong.myqcloud.com/data/books.parquet)에서 메타데이터를 가져옵니다. 이 파일에는 두 개의 레코드가 있습니다.

```text title='books.parquet'
Transaction Processing,Jim Gray,1992
Readings in Database Systems,Michael Stonebraker,2004
```

```sql
-- Show the staged file
LIST @my_internal_stage;

┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│      name     │  size  │        md5       │         last_modified         │      creator     │
├───────────────┼────────┼──────────────────┼───────────────────────────────┼──────────────────┤
│ books.parquet │    998 │ NULL             │ 2023-04-19 19:34:51.303 +0000 │ NULL             │
└──────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve metadata from the staged file
SELECT * FROM INSPECT_PARQUET('@my_internal_stage/books.parquet');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│             created_by             │ num_columns │ num_rows │ num_row_groups │ serialized_size │ max_row_groups_size_compressed │ max_row_groups_size_uncompressed │
├────────────────────────────────────┼─────────────┼──────────┼────────────────┼─────────────────┼────────────────────────────────┼──────────────────────────────────┤
│ parquet-cpp version 1.5.1-SNAPSHOT │           3 │        2 │              1 │             998 │                            332 │                              320 │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
