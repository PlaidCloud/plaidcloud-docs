---
title: TO_BOOLEAN (Lakehouse v1)
description: "TO_BOOLEAN : convertit une valeur en type de données BOOLEAN."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-boolean.md
---

Convertit une valeur en type de données BOOLEAN.

## Syntaxe Analyze

```python
func.to_boolean( <expr> )
```

## Exemples Analyze

```python
func.to_boolean('true')

┌──────────────────────────┐
│ func.to_boolean('true')  │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## Syntaxe SQL

```sql
TO_BOOLEAN( <expr> )
```

## Exemples SQL

```sql
SELECT TO_BOOLEAN('true');

┌────────────────────┐
│ to_boolean('true') │
├────────────────────┤
│ true               │
└────────────────────┘
```
