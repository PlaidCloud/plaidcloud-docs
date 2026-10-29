---
title: INSPECT_RELATED_MV (Lakehouse v2)
description: INSPECT_RELATED_MV — 테이블과 관련된 구체화된 뷰를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-related-mv.md
---

테이블과 관련된 구체화된 뷰를 반환합니다.

## Analyze 구문

```python
func.inspect_related_mv(<db>, <table>)
```

## Analyze 예제

```python
func.inspect_related_mv('mydb', 'my_table')

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```

## SQL 구문

```sql
INSPECT_RELATED_MV(<db>, <table>)
```

## SQL 예제

```sql
SELECT * FROM TABLE(INSPECT_RELATED_MV('mydb', 'my_table'));

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```
