---
title: BIN (Lakehouse v1)
description: BIN — devuelve una representación en cadena del valor binario de N.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bin.md
---

Devuelve una representación en cadena del valor binario de N.

## Sintaxis de Analyze

```python
func.bin(<expr>)
```

## Ejemplos de Analyze

```python
func.bin(12)
┌──────────────┐
│ func.bin(12) │
├──────────────┤
│ 1100         │
└──────────────┘
```

## Sintaxis SQL

```sql
BIN(<expr>)
```

## Argumentos

| Argumentos | Descripción |
|-----------|-------------|
| `<expr>`  | El número. |

## Tipo de retorno

`VARCHAR`

## Ejemplos de SQL

```sql
SELECT BIN(12);
┌─────────┐
│ BIN(12) │
├─────────┤
│ 1100    │
└─────────┘
```
