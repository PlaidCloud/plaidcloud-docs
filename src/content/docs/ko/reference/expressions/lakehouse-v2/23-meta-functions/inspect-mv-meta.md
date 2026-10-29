---
title: INSPECT_MV_META (Lakehouse v2)
description: INSPECT_MV_META — 구체화된 뷰의 메타데이터를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-meta.md
---

구체화된 뷰의 메타데이터를 반환합니다.

## Analyze 구문

```python
func.inspect_mv_meta(<db>, <mv>)
```

## Analyze 예제

```python
func.inspect_mv_meta('mydb', 'my_mv')

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```

## SQL 구문

```sql
INSPECT_MV_META(<db>, <mv>)
```

## SQL 예제

```sql
SELECT * FROM TABLE(INSPECT_MV_META('mydb', 'my_mv'));

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```
