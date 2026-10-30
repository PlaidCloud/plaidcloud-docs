---
title: H3_LINE (Lakehouse v1)
description: H3_LINE — devuelve la línea de índices entre los dos índices H3 dados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-line.md
---

Devuelve la línea de índices entre los dos índices [H3](https://eng.uber.com/h3/) dados.

## Sintaxis de Analyze

```python
func.h3_line(h3, a_h3)
```

## Ejemplos de Analyze

```python
func.h3_line(599119489002373119, 599119491149856767)

┌──────────────────────────────────────────────────────┐
│ func.h3_line(599119489002373119, 599119491149856767) │
├──────────────────────────────────────────────────────┤
│ [599119489002373119,599119491149856767]              │
└──────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_LINE(h3, a_h3)
```

## Ejemplos de SQL

```sql
SELECT H3_LINE(599119489002373119, 599119491149856767);

┌─────────────────────────────────────────────────┐
│ h3_line(599119489002373119, 599119491149856767) │
├─────────────────────────────────────────────────┤
│ [599119489002373119,599119491149856767]         │
└─────────────────────────────────────────────────┘
```
