---
title: HUMANIZE_SIZE (Lakehouse v1)
description: HUMANIZE_SIZE devuelve el tamaño legible con un sufijo (KiB, MiB, etc.).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-size.md
---

Devuelve el tamaño legible con un sufijo (KiB, MiB, etc.).

## Sintaxis de Analyze

```python
func.humanize_size(x);
```

## Ejemplos de Analyze

```python
func.humanize_size(1024 * 1024)
┌────────────────────────────────────────┐
│ func.func.humanize_size((1024 * 1024)) │
├────────────────────────────────────────┤
│ 1 MiB                                  │
└────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
HUMANIZE_SIZE(x);
```

## Argumentos

| Argumentos | Descripción                |
|-----------|----------------------------|
| x         | El tamaño numérico.        |


## Tipo de retorno

Cadena.

## Ejemplos de SQL

```sql
SELECT HUMANIZE_SIZE(1024 * 1024)
┌─────────────────────────┐
│ HUMANIZE_SIZE((1024 * 1024)) │
├─────────────────────────┤
│ 1 MiB                    │
└─────────────────────────┘
```
