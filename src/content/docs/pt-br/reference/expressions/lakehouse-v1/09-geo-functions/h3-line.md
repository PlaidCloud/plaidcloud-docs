---
title: H3_LINE (Lakehouse v1)
description: H3_LINE — retorna a linha de índices entre os dois índices H3 informados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-line.md
---

Retorna a linha de índices entre os dois índices [H3](https://eng.uber.com/h3/) informados.

## Sintaxe do Analyze

```python
func.h3_line(h3, a_h3)
```

## Exemplos do Analyze

```python
func.h3_line(599119489002373119, 599119491149856767)

┌──────────────────────────────────────────────────────┐
│ func.h3_line(599119489002373119, 599119491149856767) │
├──────────────────────────────────────────────────────┤
│ [599119489002373119,599119491149856767]              │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
H3_LINE(h3, a_h3)
```

## Exemplos de SQL

```sql
SELECT H3_LINE(599119489002373119, 599119491149856767);

┌─────────────────────────────────────────────────┐
│ h3_line(599119489002373119, 599119491149856767) │
├─────────────────────────────────────────────────┤
│ [599119489002373119,599119491149856767]         │
└─────────────────────────────────────────────────┘
```
