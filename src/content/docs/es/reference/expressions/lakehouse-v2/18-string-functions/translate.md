---
title: TRANSLATE (Lakehouse v2)
description: TRANSLATE — Reemplaza caracteres de una cadena según una asignación de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/translate.md
---

Reemplaza caracteres de una cadena según una asignación de caracteres.

## Sintaxis de Analyze

```python
func.translate(<str>, <from>, <to>)
```

## Ejemplos de Analyze

```python
func.translate('hello', 'el', 'ip')

┌─────────┐
│ 'hippo'  │
└─────────┘
```

## Sintaxis de SQL

```sql
TRANSLATE(<str>, <from>, <to>)
```

## Ejemplos de SQL

```sql
SELECT TRANSLATE('hello', 'el', 'ip');

┌───────┐
│ hippo  │
└───────┘
```
