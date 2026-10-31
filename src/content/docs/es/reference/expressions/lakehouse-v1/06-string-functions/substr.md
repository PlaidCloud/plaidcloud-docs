---
title: SUBSTR (Lakehouse v1)
description: SUBSTR — extrae una cadena con un número específico de caracteres a partir de una posición determinada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/substr.md
---

Extrae una cadena con un número específico de caracteres a partir de una posición determinada de una cadena dada.

- Las formas sin el argumento `len` devuelven una subcadena de la cadena `str` que comienza en la posición `pos`.
- Las formas con el argumento `len` devuelven una subcadena de `len` caracteres de longitud de la cadena `str`, que comienza en la posición `pos`.

También es posible usar un valor negativo para `pos`. En ese caso, el inicio de la subcadena está a pos caracteres del final de la cadena, en lugar del principio. Se puede usar un valor negativo para `pos` en cualquiera de las formas de esta función. Un valor de 0 para `pos` devuelve una cadena vacía. La posición del primer carácter de la cadena de la que se va a extraer la subcadena se considera 1.

## Sintaxis de Analyze

```python
func.substr(<str>, <pos>, <len>)
```

## Ejemplos de Analyze

```python
func.substr('Quadratically', 5, 6)
┌────────────────────────────────────┐
│ func.substr('Quadratically', 5, 6) │
├────────────────────────────────────┤
│ ratica                             │
└────────────────────────────────────┘
```

## Sintaxis SQL

```sql
SUBSTR(<str>, <pos>)

SUBSTR(<str>, <pos>, <len>)
```

## Argumentos

| Argumentos | Descripción                                                                                |
|-----------|--------------------------------------------------------------------------------------------|
| `<str>`   | La cadena principal de la que se extraen los caracteres                                   |
| `<pos>`   | La posición (a partir de 1) en la que comienza la subcadena. Si es negativa, se cuenta desde el final |
| `<len>`   | La longitud máxima de la subcadena que se extrae                                             |

## Alias

- [SUBSTRING](../substring)
- [MID](../mid)

## Tipo de retorno

VARCHAR

## Ejemplos de SQL

```sql
SELECT
  SUBSTRING('Quadratically', 5),
  SUBSTR('Quadratically', 5),
  MID('Quadratically', 5);

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5) │ substring('quadratically' from 5) │ mid('quadratically', 5) │
├───────────────────────────────────┼───────────────────────────────────┼─────────────────────────┤
│ ratically                         │ ratically                         │ ratically               │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  SUBSTRING('Quadratically', 5, 6),
  SUBSTR('Quadratically', 5, 6),
  MID('Quadratically', 5, 6);

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5 for 6) │ substring('quadratically' from 5 for 6) │ mid('quadratically', 5, 6) │
├─────────────────────────────────────────┼─────────────────────────────────────────┼────────────────────────────┤
│ ratica                                  │ ratica                                  │ ratica                     │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
