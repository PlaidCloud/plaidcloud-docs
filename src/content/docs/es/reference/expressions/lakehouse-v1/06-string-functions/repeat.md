---
title: REPEAT (Lakehouse v1)
description: REPEAT — devuelve una cadena formada por la cadena str repetida count veces.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/repeat.md
---

Devuelve una cadena formada por la cadena str repetida count veces. Si count es menor que 1, devuelve una cadena vacía. Devuelve NULL si str o count son NULL.

## Sintaxis de Analyze

```python
func.repeat(<str>, <count>)
```

## Ejemplos de Analyze

```python
func.repeat(<str>, <count>)
┌─────────────────────────┐
│ func.repeat('plaid', 3) │
├─────────────────────────┤
│ plaidplaidplaid         │
└─────────────────────────┘
```

## Sintaxis SQL

```sql
REPEAT(<str>, <count>)
```

## Argumentos

| Argumentos | Descripción |
|-----------|-------------|
| `<str>`   | La cadena. |
| `<count>` | El número. |

## Ejemplos de SQL

```sql
SELECT REPEAT('databend', 3);
┌──────────────────────────┐
│ REPEAT('databend', 3)    │
├──────────────────────────┤
│ databenddatabenddatabend │
└──────────────────────────┘

SELECT REPEAT('databend', 0);
┌───────────────────────┐
│ REPEAT('databend', 0) │
├───────────────────────┤
│                       │
└───────────────────────┘

SELECT REPEAT('databend', NULL);
┌──────────────────────────┐
│ REPEAT('databend', NULL) │
├──────────────────────────┤
│                     NULL │
└──────────────────────────┘
```
