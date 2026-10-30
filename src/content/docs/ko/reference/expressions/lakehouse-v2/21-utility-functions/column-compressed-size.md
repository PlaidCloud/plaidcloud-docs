---
title: COLUMN_COMPRESSED_SIZE (Lakehouse v2)
description: COLUMN_COMPRESSED_SIZE — 열 값의 압축된 크기를 바이트 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-compressed-size.md
---

열 값의 압축된 크기를 바이트 단위로 반환합니다.

## Analyze 구문

```python
func.column_compressed_size(get_column(table, 'data'))
```

## Analyze 예제

```python
func.column_compressed_size(get_column(table, 'data'))

┌─────┐
│ 128 │
└─────┘
```

## SQL 구문

```sql
COLUMN_COMPRESSED_SIZE(<expr>)
```

## SQL 예제

```sql
SELECT COLUMN_COMPRESSED_SIZE(data) FROM records LIMIT 1;

┌─────┐
│ 128 │
└─────┘
```
