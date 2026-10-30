---
title: YESTERDAY (Lakehouse v1)
description: YESTERDAY renvoie la date d'hier, équivalent à today() - 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/yesterday.md
---

Renvoie la date d'hier, équivalent à `today() - 1`.

## Syntaxe Analyze

```python
func.yesterday()
```

## Exemples Analyze

```python
func.yesterday()
┌──────────────────┐
│ func.yesterday() │
├──────────────────┤
│ 2021-09-02       │
└──────────────────┘
```

## Syntaxe SQL

```sql
YESTERDAY()
```

## Type de retour

`DATE`, renvoie la date au format « YYYY-MM-DD ».

## Exemples SQL

```sql
SELECT YESTERDAY();
┌─────────────┐
│ YESTERDAY() │
├─────────────┤
│ 2021-09-02  │
└─────────────┘

SELECT TODAY()-1;
┌───────────────┐
│ (TODAY() - 1) │
├───────────────┤
│ 2021-09-02    │
└───────────────┘
```
