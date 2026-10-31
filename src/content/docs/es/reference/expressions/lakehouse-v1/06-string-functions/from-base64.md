---
title: FROM_BASE64 (Lakehouse v1)
description: FROM_BASE64 — toma una cadena codificada con las reglas de codificación base64 y devuelve el resultado decodificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/from-base64.md
---

Toma una cadena codificada con las reglas de codificación base64 y devuelve el resultado decodificado como binario.
El resultado es NULL si el argumento es NULL o no es una cadena base64 válida.

## Sintaxis de Analyze

```python
func.from_base64(<expr>)
```

## Ejemplos de Analyze

```python
func.from_base64('YWJj')
┌──────────────────────────┐
│ func.from_base64('YWJj') │
├──────────────────────────┤
│ abc                      │
└──────────────────────────┘
```

## Sintaxis SQL

```sql
FROM_BASE64(<expr>)
```

## Argumentos

| Argumentos | Descripción       |
|-----------|-------------------|
| `<expr>`  | El valor de cadena. |

## Tipo de retorno

`BINARY`

## Ejemplos de SQL

```sql
SELECT TO_BASE64('abc'), FROM_BASE64(TO_BASE64('abc')) as b, b::String;
┌───────────────────────────────────────┐
│ to_base64('abc') │    b   │ b::string │
│      String      │ Binary │   String  │
├──────────────────┼────────┼───────────┤
│ YWJj             │ 616263 │ abc       │
└───────────────────────────────────────┘
```
