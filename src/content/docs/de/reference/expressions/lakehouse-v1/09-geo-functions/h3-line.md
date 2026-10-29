---
title: H3_LINE (Lakehouse v1)
description: H3_LINE — gibt die Linie von Indizes zwischen den beiden angegebenen H3-Indizes zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-line.md
---

Gibt die Linie von Indizes zwischen den beiden angegebenen [H3](https://eng.uber.com/h3/)-Indizes zurück.

## Analyze-Syntax

```python
func.h3_line(h3, a_h3)
```

## Analyze-Beispiele

```python
func.h3_line(599119489002373119, 599119491149856767)

┌──────────────────────────────────────────────────────┐
│ func.h3_line(599119489002373119, 599119491149856767) │
├──────────────────────────────────────────────────────┤
│ [599119489002373119,599119491149856767]              │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_LINE(h3, a_h3)
```

## SQL-Beispiele

```sql
SELECT H3_LINE(599119489002373119, 599119491149856767);

┌─────────────────────────────────────────────────┐
│ h3_line(599119489002373119, 599119491149856767) │
├─────────────────────────────────────────────────┤
│ [599119489002373119,599119491149856767]         │
└─────────────────────────────────────────────────┘
```
