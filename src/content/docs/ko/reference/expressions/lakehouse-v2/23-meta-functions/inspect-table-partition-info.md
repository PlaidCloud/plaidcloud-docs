---
title: INSPECT_TABLE_PARTITION_INFO (Lakehouse v2)
description: INSPECT_TABLE_PARTITION_INFO — 테이블의 파티션 정보를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-table-partition-info.md
---

테이블의 파티션 정보를 반환합니다.

## Analyze 구문

```python
func.inspect_table_partition_info(<catalog>, <db>, <table>)
```

## Analyze 예제

```python
func.inspect_table_partition_info('default', 'mydb', 'my_table')

┌──────────────┐
│ (partitions)  │
└──────────────┘
```

## SQL 구문

```sql
INSPECT_TABLE_PARTITION_INFO(<catalog>, <db>, <table>)
```

## SQL 예제

```sql
SELECT * FROM TABLE(INSPECT_TABLE_PARTITION_INFO('default', 'mydb', 'my_table'));

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```
