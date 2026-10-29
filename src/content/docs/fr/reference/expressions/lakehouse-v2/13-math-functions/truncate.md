---
title: TRUNCATE (Lakehouse v2)
description: TRUNCATE — tronque un nombre à un nombre de décimales spécifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/truncate.md
---

Tronque un nombre à un nombre de décimales spécifié.

## Syntaxe Analyze

```python
func.truncate(<x>, <d>)
```

## Exemples Analyze

```python
func.truncate(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## Syntaxe SQL

```sql
TRUNCATE(<x>, <d>)
```

## Exemples SQL

```sql
SELECT TRUNCATE(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
