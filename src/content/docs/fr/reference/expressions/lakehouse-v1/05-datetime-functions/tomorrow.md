---
title: TOMORROW (Lakehouse v1)
description: TOMORROW renvoie la date de demain, équivalent à today() + 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/tomorrow.md
---

Renvoie la date de demain, équivalent à `today() + 1`.

## Syntaxe Analyze

```python
func.tomorrow()
```

## Exemples Analyze

```python
func.tomorrow()
┌─────────────────┐
│ func.tomorrow() │
├─────────────────┤
│ 2021-09-03      │
└─────────────────┘
```

## Syntaxe SQL

```sql
TOMORROW()
```

## Type de retour

`DATE`, renvoie la date au format « YYYY-MM-DD ».

## Exemples SQL

```sql
SELECT TOMORROW();
┌────────────┐
│ TOMORROW() │
├────────────┤
│ 2021-09-04 │
└────────────┘

SELECT TODAY()+1;
┌───────────────┐
│ (TODAY() + 1) │
├───────────────┤
│ 2021-09-04    │
└───────────────┘
```
