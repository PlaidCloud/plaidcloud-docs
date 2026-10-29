---
title: STRCMP (Lakehouse v2)
description: "Utilisez la fonction de chaîne STRCMP dans PlaidCloud Lakehouse. Compare deux chaînes dans l'ordre lexicographique. Renvoie 0 si elles sont égales, -1 si str1 < str2, 1 si str1 > str2."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strcmp.md
---

Compare deux chaînes dans l'ordre lexicographique. Renvoie 0 si elles sont égales, -1 si str1 &lt; str2, 1 si str1 > str2.

## Syntaxe Analyze

```python
func.strcmp(<str1>, <str2>)
```

## Exemples Analyze

```python
func.strcmp('abc', 'abd')

┌────┐
│ -1  │
└────┘
```

## Syntaxe SQL

```sql
STRCMP(<str1>, <str2>)
```

## Exemples SQL

```sql
SELECT STRCMP('abc', 'abd');

┌────┐
│ -1  │
└────┘
```
