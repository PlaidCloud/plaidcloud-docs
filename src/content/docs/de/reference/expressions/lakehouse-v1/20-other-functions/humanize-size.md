---
title: HUMANIZE_SIZE (Lakehouse v1)
description: HUMANIZE_SIZE gibt die lesbare Größe mit einem Suffix (KiB, MiB usw.) zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-size.md
---

Gibt die lesbare Größe mit einem Suffix (KiB, MiB usw.) zurück.

## Analyze-Syntax

```python
func.humanize_size(x);
```

## Analyze-Beispiele

```python
func.humanize_size(1024 * 1024)
┌────────────────────────────────────────┐
│ func.func.humanize_size((1024 * 1024)) │
├────────────────────────────────────────┤
│ 1 MiB                                  │
└────────────────────────────────────────┘
```

## SQL-Syntax

```sql
HUMANIZE_SIZE(x);
```

## Argumente

| Argumente | Beschreibung               |
|-----------|----------------------------|
| x         | Der numerische Wert der Größe. |


## Rückgabetyp

Zeichenfolge.

## SQL-Beispiele

```sql
SELECT HUMANIZE_SIZE(1024 * 1024)
┌─────────────────────────┐
│ HUMANIZE_SIZE((1024 * 1024)) │
├─────────────────────────┤
│ 1 MiB                    │
└─────────────────────────┘
```
