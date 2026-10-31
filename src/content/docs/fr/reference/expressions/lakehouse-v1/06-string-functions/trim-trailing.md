---
title: TRIM_TRAILING (Lakehouse v1)
description: "TRIM_TRAILING : supprime toutes les occurrences de la chaîne à retirer à la fin de la chaîne."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-trailing.md
---

Supprime toutes les occurrences de la chaîne à retirer à la fin de la chaîne.

Voir aussi : 

- [RTRIM](../rtrim)
- [TRIM_LEADING](../trim-leading)

## Syntaxe Analyze

```python
func.trim_trailing(<string>, <trim_string>)
```

## Exemples Analyze

```python
func.trim_trailing('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_trailing('xxdatabendxx', 'x')  │
├──────────────────────────────────────────┤
│ xxdatabend                               │
└──────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TRIM_TRAILING(<string>, <trim_string>)
```

## Exemples SQL

```sql
SELECT TRIM_TRAILING('databendxx', 'xxx'), TRIM_TRAILING('databendxx', 'xx'), TRIM_TRAILING('databendxx', 'x');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_trailing('databendxx', 'xxx') │ trim_trailing('databendxx', 'xx') │ trim_trailing('databendxx', 'x') │
├────────────────────────────────────┼───────────────────────────────────┼──────────────────────────────────┤
│ databendxx                         │ databend                          │ databend                         │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
