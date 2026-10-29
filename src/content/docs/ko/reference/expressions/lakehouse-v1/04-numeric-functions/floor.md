---
title: FLOOR (Lakehouse v1)
description: FLOOR — 수를 내림합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/floor.md
---

수를 내림합니다.

## Analyze 구문

```python
func.floor( <x> )
```

## Analyze 예시

```python
func.floor(1.23)

┌──────────────────┐
│ func.floor(1.23) │
├──────────────────┤
│                1 │
└──────────────────┘
```

## SQL 구문

```sql
FLOOR( <x> )
```

## SQL 예시

```sql
SELECT FLOOR(1.23);

┌─────────────┐
│ floor(1.23) │
├─────────────┤
│           1 │
└─────────────┘
```
