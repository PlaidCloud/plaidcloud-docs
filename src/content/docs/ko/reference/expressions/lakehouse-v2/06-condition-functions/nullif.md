---
title: NULLIF (Lakehouse v2)
description: NULLIF — 두 식이 같으면 NULL을, 그렇지 않으면 첫 번째 식을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/nullif.md
---

두 식이 같으면 NULL을, 그렇지 않으면 첫 번째 식을 반환합니다.

## Analyze 구문

```python
func.nullif(get_column(table, 'value'), 0)
```

## Analyze 예제

```python
func.nullif(get_column(table, 'divisor'), 0)
```

## SQL 구문

```sql
NULLIF(<value>, 0)
```

## SQL 예제

```sql
SELECT 100 / NULLIF(divisor, 0) AS safe_division FROM calculations;

┌───────────────┐
│ safe_division │
├───────────────┤
│         50.00 │
│          NULL │
│         25.00 │
└───────────────┘
```
