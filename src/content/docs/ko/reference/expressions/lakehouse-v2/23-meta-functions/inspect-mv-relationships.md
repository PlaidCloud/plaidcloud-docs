---
title: INSPECT_MV_RELATIONSHIPS (Lakehouse v2)
description: INSPECT_MV_RELATIONSHIPS — 구체화된 뷰의 종속 관계를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-relationships.md
---

구체화된 뷰의 종속 관계를 반환합니다.

## Analyze 구문

```python
func.inspect_mv_relationships(<db>, <mv>)
```

## Analyze 예제

```python
func.inspect_mv_relationships('mydb', 'my_mv')

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```

## SQL 구문

```sql
INSPECT_MV_RELATIONSHIPS(<db>, <mv>)
```

## SQL 예제

```sql
SELECT * FROM TABLE(INSPECT_MV_RELATIONSHIPS('mydb', 'my_mv'));

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```
