---
title: DLOG10 (Lakehouse v2)
description: DLOG10 — `LOG10`의 별칭입니다. [LOG10](../log10/)을 참조하십시오.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog10.md
---

`LOG10`의 별칭입니다. [LOG10](../log10/)을 참조하십시오.

## Analyze 구문

```python
func.dlog10(1000)
```

## Analyze 예제

```python
func.dlog10(1000)

┌─────┐
│ 3.0 │
└─────┘
```

## SQL 구문

```sql
DLOG10(<x>)
```

## SQL 예제

```sql
SELECT DLOG10(1000);

┌─────┐
│ 3.0 │
└─────┘
```
