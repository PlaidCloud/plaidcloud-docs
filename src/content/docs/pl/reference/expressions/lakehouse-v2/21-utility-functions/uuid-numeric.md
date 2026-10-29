---
title: UUID_NUMERIC (Lakehouse v2)
description: UUID_NUMERIC — zwraca losowy UUID jako 128-bitową wartość LARGEINT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-numeric.md
---

Zwraca losowy UUID jako 128-bitową wartość LARGEINT.

## Składnia Analyze

```python
func.uuid_numeric()
```

## Przykłady Analyze

```python
func.uuid_numeric()

┌────────────┐
│ (largeint)  │
└────────────┘
```

## Składnia SQL

```sql
UUID_NUMERIC()
```

## Przykłady SQL

```sql
SELECT UUID_NUMERIC();

┌─────────────────────────────────────────┐
│ 113304629137197850819971302868472922876  │
└─────────────────────────────────────────┘
```
