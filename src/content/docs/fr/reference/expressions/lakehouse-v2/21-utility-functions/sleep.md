---
title: SLEEP (Lakehouse v2)
description: SLEEP — suspend l'exécution pendant un nombre de secondes donné. Renvoie 0 en cas de succès.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/sleep.md
---

Suspend l'exécution pendant un nombre de secondes donné. Renvoie 0 en cas de succès.

## Syntaxe Analyze

```python
func.sleep(<seconds>)
```

## Exemples Analyze

```python
func.sleep(1)

┌───┐
│ 0  │
└───┘
```

## Syntaxe SQL

```sql
SLEEP(<seconds>)
```

## Exemples SQL

```sql
SELECT SLEEP(1);

┌───┐
│ 0  │
└───┘
```
