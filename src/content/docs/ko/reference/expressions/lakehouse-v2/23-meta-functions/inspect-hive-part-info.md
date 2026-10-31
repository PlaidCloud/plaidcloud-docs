---
title: INSPECT_HIVE_PART_INFO (Lakehouse v2)
description: INSPECT_HIVE_PART_INFO — 외부 테이블의 Hive 파티션 정보를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-hive-part-info.md
---

외부 테이블의 Hive 파티션 정보를 반환합니다.

## Analyze 구문

```python
func.inspect_hive_part_info(<catalog>, <db>, <table>)
```

## Analyze 예제

```python
func.inspect_hive_part_info('hive_catalog', 'db', 'tbl')

┌──────────────────┐
│ (partition info)  │
└──────────────────┘
```

## SQL 구문

```sql
INSPECT_HIVE_PART_INFO(<catalog>, <db>, <table>)
```

## SQL 예제

```sql
SELECT * FROM TABLE(INSPECT_HIVE_PART_INFO('hive_catalog', 'db', 'tbl'));

┌─────────────────────┐
│ (partition details)  │
└─────────────────────┘
```
