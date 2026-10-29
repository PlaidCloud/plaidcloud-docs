---
title: TRIM_BOTH (Lakehouse v1)
description: TRIM_BOTH supprime toutes les occurrences de la chaîne de suppression indiquée au début, à la fin ou des deux côtés de la chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-both.md
---

Supprime toutes les occurrences de la chaîne de suppression indiquée au début, à la fin ou des deux côtés de la chaîne.

Voir aussi : [TRIM](../trim)

## Syntaxe Analyze

```python
func.trim_both(<string>, <trim_string>)
```

## Exemples Analyze

```python
func.trim_both('xxdatabendxx', 'x')
┌──────────────────────────────────────┐
│ func.trim_both('xxdatabendxx', 'x')  │
├──────────────────────────────────────┤
│ databend                             │
└──────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TRIM_BOTH(<string>, <trim_string>)
```

## Exemples SQL

```sql
SELECT TRIM_BOTH('xxdatabendxx', 'xxx'), TRIM_BOTH('xxdatabendxx', 'xx'), TRIM_BOTH('xxdatabendxx', 'x');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_both('xxdatabendxx', 'xxx') │ trim_both('xxdatabendxx', 'xx') │ trim_both('xxdatabendxx', 'x') │
├──────────────────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ xxdatabendxx                     │ databend                        │ databend                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
