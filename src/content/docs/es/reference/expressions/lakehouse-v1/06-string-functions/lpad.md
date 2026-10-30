---
title: LPAD (Lakehouse v1)
description: LPAD — devuelve la cadena str rellenada a la izquierda con la cadena padstr hasta alcanzar una longitud de len caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lpad.md
---

Devuelve la cadena str rellenada a la izquierda con la cadena padstr hasta alcanzar una longitud de len caracteres.
Si str es más larga que len, el valor devuelto se acorta a len caracteres.

## Sintaxis de Analyze

```python
func.lpad(<str>, <len>, <padstr>)
```

## Ejemplos de Analyze

```python
func.lpad('hi',4,'??')
┌────────────────────────┐
│ func.lpad('hi',4,'??') │
├────────────────────────┤
│ ??hi                   │
└────────────────────────┘
```

```python
func.lpad('hi',1,'??')
┌────────────────────────┐
│ func.lpad('hi',1,'??') │
├────────────────────────┤
│ h                      │
└────────────────────────┘
```

## Sintaxis SQL

```sql
LPAD(<str>, <len>, <padstr>)
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
SELECT LPAD('hi',4,'??');
┌─────────────────────┐
│ LPAD('hi', 4, '??') │
├─────────────────────┤
│ ??hi                │
└─────────────────────┘

SELECT LPAD('hi',1,'??');
┌─────────────────────┐
│ LPAD('hi', 1, '??') │
├─────────────────────┤
│ h                   │
└─────────────────────┘
```
