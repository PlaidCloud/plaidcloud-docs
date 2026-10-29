---
title: BITNOT (Lakehouse v2)
description: BITNOT — renvoie le NON bit à bit d'une valeur numérique.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitnot.md
---

Renvoie le NON bit à bit d'une valeur numérique.

## Syntaxe Analyze

```python
func.bitnot(<x>)
```

## Exemples Analyze

```python
func.bitnot(0)

┌──────┐
│ '-1'  │
└──────┘
```

## Syntaxe SQL

```sql
BITNOT(<x>)
```

## Exemples SQL

```sql
SELECT BITNOT(0);

┌────┐
│ -1  │
└────┘
```
