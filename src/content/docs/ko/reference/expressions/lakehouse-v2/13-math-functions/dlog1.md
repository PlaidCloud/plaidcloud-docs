---
title: DLOG1 (Lakehouse v2)
description: DLOG1 — `LN`의 별칭입니다. [LN](../ln/)을 참조하십시오.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog1.md
---

`LN`의 별칭입니다. [LN](../ln/)을 참조하십시오.

## Analyze 구문

```python
func.dlog1(2.718281828459045)
```

## Analyze 예제

```python
func.dlog1(2.718281828459045)

┌─────┐
│ 1.0 │
└─────┘
```

## SQL 구문

```sql
DLOG1(<x>)
```

## SQL 예제

```sql
SELECT DLOG1(2.718281828459045);

┌─────┐
│ 1.0 │
└─────┘
```
