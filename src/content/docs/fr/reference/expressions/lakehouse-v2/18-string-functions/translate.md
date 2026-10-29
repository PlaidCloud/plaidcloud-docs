---
title: TRANSLATE (Lakehouse v2)
description: TRANSLATE — remplace des caractères d'une chaîne selon une table de correspondance de caractères.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/translate.md
---

Remplace des caractères d'une chaîne selon une table de correspondance de caractères.

## Syntaxe Analyze

```python
func.translate(<str>, <from>, <to>)
```

## Exemples Analyze

```python
func.translate('hello', 'el', 'ip')

┌─────────┐
│ 'hippo'  │
└─────────┘
```

## Syntaxe SQL

```sql
TRANSLATE(<str>, <from>, <to>)
```

## Exemples SQL

```sql
SELECT TRANSLATE('hello', 'el', 'ip');

┌───────┐
│ hippo  │
└───────┘
```
