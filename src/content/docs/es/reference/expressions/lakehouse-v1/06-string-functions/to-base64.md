---
title: TO_BASE64 (Lakehouse v1)
description: TO_BASE64 — convierte el argumento de cadena a su forma codificada en base64 y devuelve el resultado como una cadena de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/to-base64.md
---

Convierte el argumento de cadena a su forma codificada en base64 y devuelve el resultado como una cadena de caracteres.
Si el argumento no es una cadena, se convierte en una cadena antes de realizar la conversión.
El resultado es NULL si el argumento es NULL.

## Sintaxis de Analyze

```python
func.to_base64(<v>)
```

## Ejemplos de Analyze

```python
func.to_base64('abc')
┌───────────────────────┐
│ func.to_base64('abc') │
├───────────────────────┤
│ YWJj                  │
└───────────────────────┘
```

## Sintaxis SQL

```sql
TO_BASE64(<v>)
```

## Argumentos

| Argumentos | Descripción |
|-----------|-------------|
| `<v>`     | El valor.  |

## Tipo de retorno

`VARCHAR`

## Ejemplos de SQL

```sql
SELECT TO_BASE64('abc');
┌──────────────────┐
│ TO_BASE64('abc') │
├──────────────────┤
│ YWJj             │
└──────────────────┘
```
