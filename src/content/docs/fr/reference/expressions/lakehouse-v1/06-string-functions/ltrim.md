---
title: LTRIM (Lakehouse v1)
description: LTRIM supprime à gauche de la chaîne toutes les occurrences de tout caractère présent dans la chaîne de suppression indiquée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ltrim.md
---

Supprime à gauche de la chaîne toutes les occurrences de tout caractère présent dans la chaîne de suppression indiquée.

Voir aussi : 

- [TRIM_LEADING](../trim-leading)
- [RTRIM](../rtrim)

## Syntaxe Analyze

```python
func.ltrim(<string>, <trim_string>)
```

## Exemples Analyze

```python
func.ltrim('xxdatabend', 'x')
┌────────────────────────────────┐
│ func.ltrim('xxdatabend', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## Syntaxe SQL

```sql
LTRIM(<string>, <trim_string>)
```

## Exemples SQL

```sql
SELECT LTRIM('xxdatabend', 'xx'), LTRIM('xxdatabend', 'xy');

┌───────────────────────────────────────────────────────┐
│ ltrim('xxdatabend', 'xx') │ ltrim('xxdatabend', 'xy') │
├───────────────────────────┼───────────────────────────┤
│ databend                  │ databend                  │
└───────────────────────────────────────────────────────┘
```
