---
title: TRIM_LEADING (Lakehouse v1)
description: "TRIM_LEADING : supprime toutes les occurrences de la chaîne à retirer au début de la chaîne."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-leading.md
---

Supprime toutes les occurrences de la chaîne à retirer au début de la chaîne.

Voir aussi : 

- [LTRIM](../ltrim)
- [TRIM_TRAILING](../trim-trailing)

## Syntaxe Analyze

```python
func.trim_leading(<string>, <trim_string>)
```

## Exemples Analyze

```python
func.trim_leading('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_leading('xxdatabendxx', 'x')   │
├──────────────────────────────────────────┤
│ databendxx                               │
└──────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TRIM_LEADING(<string>, <trim_string>)
```

## Exemples SQL

```sql
SELECT TRIM_LEADING('xxdatabend', 'xxx'), TRIM_LEADING('xxdatabend', 'xx'), TRIM_LEADING('xxdatabend', 'x');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_leading('xxdatabend', 'xxx') │ trim_leading('xxdatabend', 'xx') │ trim_leading('xxdatabend', 'x') │
├───────────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ xxdatabend                        │ databend                         │ databend                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
