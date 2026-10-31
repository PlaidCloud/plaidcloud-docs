---
title: HUMANIZE_NUMBER (Lakehouse v1)
description: HUMANIZE_NUMBER — renvoie un nombre lisible.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-number.md
---

Renvoie un nombre lisible.

## Syntaxe Analyze

```python
func.humanize_number(x);
```

## Exemples Analyze

```python
func.humanize_number(1000 * 1000)
┌─────────────────────────────────────┐
│ func.humanize_number((1000 * 1000)) │
├─────────────────────────────────────┤
│ 1 million                           │
└─────────────────────────────────────┘
```

## Syntaxe SQL

```sql
HUMANIZE_NUMBER(x);
```

## Arguments

| Arguments | Description                |
|-----------|----------------------------|
| x         | La taille numérique.       |


## Type de retour

Chaîne.

## Exemples SQL

```sql
SELECT HUMANIZE_NUMBER(1000 * 1000)
┌─────────────────────────┐
│ HUMANIZE_NUMBER((1000 * 1000)) │
├─────────────────────────┤
│ 1 million               │
└─────────────────────────┘
```
