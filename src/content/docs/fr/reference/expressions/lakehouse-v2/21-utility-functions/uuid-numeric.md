---
title: UUID_NUMERIC (Lakehouse v2)
description: UUID_NUMERIC — renvoie un UUID aléatoire sous la forme d'une valeur LARGEINT de 128 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-numeric.md
---

Renvoie un UUID aléatoire sous la forme d'une valeur LARGEINT de 128 bits.

## Syntaxe Analyze

```python
func.uuid_numeric()
```

## Exemples Analyze

```python
func.uuid_numeric()

┌────────────┐
│ (largeint)  │
└────────────┘
```

## Syntaxe SQL

```sql
UUID_NUMERIC()
```

## Exemples SQL

```sql
SELECT UUID_NUMERIC();

┌─────────────────────────────────────────┐
│ 113304629137197850819971302868472922876  │
└─────────────────────────────────────────┘
```
