---
title: STRING_TO_H3 (Lakehouse v1)
description: STRING_TO_H3 — convierte la representación en cadena a la representación H3 (uint64).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/string-to-h3.md
---

Convierte la representación en cadena a la representación [H3](https://eng.uber.com/h3/) (uint64).

## Sintaxis de Analyze

```python
func.string_to_h3(h3)
```

## Ejemplos de Analyze

```python
func.string_to_h3('8d11aa6a38826ff')

┌──────────────────────────────────────┐
│ func.string_to_h3('8d11aa6a38826ff') │
├──────────────────────────────────────┤
│                   635318325446452991 │
└──────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
STRING_TO_H3(h3)
```

## Ejemplos de SQL

```sql
SELECT STRING_TO_H3('8d11aa6a38826ff');

┌─────────────────────────────────┐
│ string_to_h3('8d11aa6a38826ff') │
├─────────────────────────────────┤
│              635318325446452991 │
└─────────────────────────────────┘
```
