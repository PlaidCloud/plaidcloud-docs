---
title: RTRIM (Lakehouse v1)
description: RTRIM supprime à droite de la chaîne toutes les occurrences de tout caractère présent dans la chaîne de suppression indiquée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rtrim.md
---

Supprime à droite de la chaîne toutes les occurrences de tout caractère présent dans la chaîne de suppression indiquée.

Voir aussi : 

- [TRIM_TRAILING](../trim-trailing)
- [LTRIM](../ltrim)

## Syntaxe Analyze

```python
func.rtrim(<string>, <trim_string>)
```

## Exemples Analyze

```python
func.rtrim('databend'xx, 'x')
┌────────────────────────────────┐
│ func.rtrim('databendxx', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## Syntaxe SQL

```sql
RTRIM(<string>, <trim_string>)
```

## Exemples SQL

```sql
SELECT RTRIM('databendxx', 'x'), RTRIM('databendxx', 'xy');

┌──────────────────────────────────────────────────────┐
│ rtrim('databendxx', 'x') │ rtrim('databendxx', 'xy') │
├──────────────────────────┼───────────────────────────┤
│ databend                 │ databend                  │
└──────────────────────────────────────────────────────┘
```
