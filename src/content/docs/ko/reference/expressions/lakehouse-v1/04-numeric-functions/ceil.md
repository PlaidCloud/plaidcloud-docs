---
title: CEIL (Lakehouse v1)
description: CEIL — 수를 올림합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ceil.md
---

수를 올림합니다.

## Analyze 구문

```python
func.ceil( <x> )
```

## Analyze 예시

```python
func.ceil((- 1.23))

┌─────────────────────┐
│ func.ceil((- 1.23)) │
├─────────────────────┤
│                  -1 │ 
└─────────────────────┘
```

## SQL 구문

```sql
CEIL( <x> )
```

## 별칭

- [CEILING](../ceiling)

## SQL 예시

```sql
SELECT CEILING(-1.23), CEIL(-1.23);

┌────────────────────────────────────┐
│ ceiling((- 1.23)) │ ceil((- 1.23)) │
├───────────────────┼────────────────┤
│                -1 │             -1 │
└────────────────────────────────────┘
```
