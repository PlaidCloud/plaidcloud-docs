---
title: SPACE (Lakehouse v1)
description: SPACE renvoie une chaîne composée de N espaces.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/space.md
---

Renvoie une chaîne composée de N espaces.

## Syntaxe Analyze

```python
func.space(<n>)
```

## Exemples Analyze

```python
func.space(20)
┌─────────────────┐
│ func.space(20)  │
├─────────────────┤
│                 │
└─────────────────┘
```

## Syntaxe SQL

```sql
SPACE(<n>);
```

## Arguments

| Arguments | Description                |
|-----------|----------------------------|
| `<n>`     | Le nombre d'espaces        |

## Type de retour

Valeur de type de données chaîne.

## Exemples SQL

```sql
SELECT SPACE(20)
┌──────────────────────┐
│ SPACE(20)            │
├──────────────────────┤
│                      │
└──────────────────────┘
```
