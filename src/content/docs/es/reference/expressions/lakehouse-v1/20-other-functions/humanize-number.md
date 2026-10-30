---
title: HUMANIZE_NUMBER (Lakehouse v1)
description: HUMANIZE_NUMBER devuelve un número legible.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-number.md
---

Devuelve un número legible.

## Sintaxis de Analyze

```python
func.humanize_number(x);
```

## Ejemplos de Analyze

```python
func.humanize_number(1000 * 1000)
┌─────────────────────────────────────┐
│ func.humanize_number((1000 * 1000)) │
├─────────────────────────────────────┤
│ 1 million                           │
└─────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
HUMANIZE_NUMBER(x);
```

## Argumentos

| Argumentos | Descripción                |
|-----------|----------------------------|
| x         | El tamaño numérico.        |


## Tipo de retorno

Cadena.

## Ejemplos de SQL

```sql
SELECT HUMANIZE_NUMBER(1000 * 1000)
┌─────────────────────────┐
│ HUMANIZE_NUMBER((1000 * 1000)) │
├─────────────────────────┤
│ 1 million               │
└─────────────────────────┘
```
