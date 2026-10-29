---
title: UUID_NUMERIC (Lakehouse v2)
description: UUID_NUMERIC — Retorna um UUID aleatório como um valor LARGEINT de 128 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-numeric.md
---

Retorna um UUID aleatório como um valor LARGEINT de 128 bits.

## Sintaxe do Analyze

```python
func.uuid_numeric()
```

## Exemplos do Analyze

```python
func.uuid_numeric()

┌────────────┐
│ (largeint)  │
└────────────┘
```

## Sintaxe SQL

```sql
UUID_NUMERIC()
```

## Exemplos de SQL

```sql
SELECT UUID_NUMERIC();

┌─────────────────────────────────────────┐
│ 113304629137197850819971302868472922876  │
└─────────────────────────────────────────┘
```
