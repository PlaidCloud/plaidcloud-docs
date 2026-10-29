---
title: H3_TO_STRING (Lakehouse v1)
description: H3_TO_STRING — convierte la representación del índice H3 dado a su representación en cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-string.md
---

Convierte la representación del índice [H3](https://eng.uber.com/h3/) dado a su representación en cadena. 

## Sintaxis de Analyze

```python
func.h3_to_string(h3)
```

## Ejemplos de Analyze

```python
func.h3_to_string(635318325446452991)

┌───────────────────────────────────────┐
│ func.h3_to_string(635318325446452991) │
├───────────────────────────────────────┤
│ 8d11aa6a38826ff                       │
└───────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
H3_TO_STRING(h3)
```

## Ejemplos de SQL

```sql
SELECT H3_TO_STRING(635318325446452991);

┌──────────────────────────────────┐
│ h3_to_string(635318325446452991) │
├──────────────────────────────────┤
│ 8d11aa6a38826ff                  │
└──────────────────────────────────┘
```
