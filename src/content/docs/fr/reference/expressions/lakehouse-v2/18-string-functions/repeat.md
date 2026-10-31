---
title: REPEAT (Lakehouse v2)
description: REPEAT — répète une chaîne un nombre de fois donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/repeat.md
---

Répète une chaîne un nombre de fois donné.

## Syntaxe Analyze

```python
func.repeat(<str>, <n>)
```

## Exemples Analyze

```python
func.repeat('ab', 3)

┌──────────┐
│ 'ababab'  │
└──────────┘
```

## Syntaxe SQL

```sql
REPEAT(<str>, <n>)
```

## Exemples SQL

```sql
SELECT REPEAT('ab', 3);

┌────────┐
│ ababab  │
└────────┘
```
