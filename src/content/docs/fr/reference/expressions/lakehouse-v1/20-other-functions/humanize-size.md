---
title: HUMANIZE_SIZE (Lakehouse v1)
description: HUMANIZE_SIZE — renvoie la taille lisible avec un suffixe (KiB, MiB, etc.).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-size.md
---

Renvoie la taille lisible avec un suffixe (KiB, MiB, etc.).

## Syntaxe Analyze

```python
func.humanize_size(x);
```

## Exemples Analyze

```python
func.humanize_size(1024 * 1024)
┌────────────────────────────────────────┐
│ func.func.humanize_size((1024 * 1024)) │
├────────────────────────────────────────┤
│ 1 MiB                                  │
└────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
HUMANIZE_SIZE(x);
```

## Arguments

| Arguments | Description                |
|-----------|----------------------------|
| x         | La taille numérique.       |


## Type de retour

Chaîne.

## Exemples SQL

```sql
SELECT HUMANIZE_SIZE(1024 * 1024)
┌─────────────────────────┐
│ HUMANIZE_SIZE((1024 * 1024)) │
├─────────────────────────┤
│ 1 MiB                    │
└─────────────────────────┘
```
