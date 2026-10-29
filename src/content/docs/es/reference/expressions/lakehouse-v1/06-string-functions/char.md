---
title: CHAR (Lakehouse v1)
description: CHAR — devuelve el carácter correspondiente a cada entero indicado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/char.md
---

Devuelve el carácter correspondiente a cada entero indicado.

## Sintaxis de Analyze

```python
func.char(N,...)
```

## Ejemplos de Analyze

```python
func.char(77,121,83,81,76)
┌─────────────────────────────┐
│ func.char(77,121,83,81,76) │
├─────────────────────────────┤
│ 4D7953514C                  │
└─────────────────────────────┘
```

## Sintaxis SQL

```sql
CHAR(N, ...)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| N         | Columna numérica |

## Tipo de retorno

`BINARY`

## Ejemplos de SQL

Este ejemplo muestra tanto el valor binario devuelto como su representación en cadena.

```sql
SELECT CHAR(77,121,83,81,76) as a, a::String;
┌────────────────────────┐
│      a     │ a::string │
│   Binary   │   String  │
├────────────┼───────────┤
│ 4D7953514C │ MySQL     │
└────────────────────────┘
```
