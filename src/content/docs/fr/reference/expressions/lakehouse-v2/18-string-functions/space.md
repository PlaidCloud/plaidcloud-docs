---
title: SPACE (Lakehouse v2)
description: SPACE — renvoie une chaîne composée d'un nombre donné d'espaces.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/space.md
---

Renvoie une chaîne composée d'un nombre donné d'espaces.

## Syntaxe Analyze

```python
func.space(<n>)
```

## Exemples Analyze

```python
func.space(5)

┌─────────┐
│ '     '  │
└─────────┘
```

## Syntaxe SQL

```sql
SPACE(<n>)
```

## Exemples SQL

```sql
SELECT CONCAT('>', SPACE(5), '<');

┌─────────┐
│ >     <  │
└─────────┘
```
