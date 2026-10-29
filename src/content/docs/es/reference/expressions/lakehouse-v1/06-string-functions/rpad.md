---
title: RPAD (Lakehouse v1)
description: RPAD — devuelve la cadena str rellenada a la derecha con la cadena padstr hasta alcanzar una longitud de len caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rpad.md
---

Devuelve la cadena str rellenada a la derecha con la cadena padstr hasta alcanzar una longitud de len caracteres.
Si str es más larga que len, el valor devuelto se acorta a len caracteres.

## Sintaxis de Analyze

```python
func.rpad(<str>, <len>, <padstr>)
```

## Ejemplos de Analyze

```python
func.rpad('hi',5,'?')
┌───────────────────────┐
│ func.rpad('hi',5,'?') │
├───────────────────────┤
│ hi???                 │
└───────────────────────┘

func.rpad('hi',1,'?')
┌───────────────────────┐
│ func.rpad('hi',1,'?') │
├───────────────────────┤
│ h                     │
└───────────────────────┘
```

## Sintaxis SQL

```sql
RPAD(<str>, <len>, <padstr>)
```

## Argumentos

| Argumentos  | Descripción     |
|------------|-----------------|
| `<str>`    | La cadena.     |
| `<len>`    | La longitud.     |
| `<padstr>` | La cadena de relleno. |

## Tipo de retorno

`VARCHAR`

## Ejemplos de SQL

```sql
SELECT RPAD('hi',5,'?');
┌────────────────────┐
│ RPAD('hi', 5, '?') │
├────────────────────┤
│ hi???              │
└────────────────────┘

SELECT RPAD('hi',1,'?');
┌────────────────────┐
│ RPAD('hi', 1, '?') │
├────────────────────┤
│ h                  │
└────────────────────┘
```
