---
title: NOW (Lakehouse v1)
description: NOW — renvoie la date et l'heure actuelles.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/now.md
---

Renvoie la date et l'heure actuelles.

## Syntaxe Analyze

```python
func.now()
```

## Exemples Analyze

```python
┌─────────────────────────────────────────────────────────┐
│  func.current_timestamp()  │         func.now()         │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
NOW()
```

## Type de retour

TIMESTAMP

## Alias

- [CURRENT_TIMESTAMP](../current-timestamp)

## Exemples SQL

Cet exemple renvoie la date et l'heure actuelles :

```sql
SELECT CURRENT_TIMESTAMP(), NOW();

┌─────────────────────────────────────────────────────────┐
│     current_timestamp()    │            now()           │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```
