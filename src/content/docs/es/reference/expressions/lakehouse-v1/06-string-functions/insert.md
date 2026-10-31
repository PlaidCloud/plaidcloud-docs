---
title: INSERT (Lakehouse v1)
description: INSERT — devuelve la cadena str con la subcadena que comienza en la posición pos y tiene len caracteres reemplazada por newstr.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/insert.md
---

Devuelve la cadena str con la subcadena que comienza en la posición pos y tiene len caracteres de longitud reemplazada por la cadena newstr. Devuelve la cadena original si pos no está dentro de la longitud de la cadena. Reemplaza el resto de la cadena desde la posición pos si len no está dentro de la longitud del resto de la cadena. Devuelve NULL si algún argumento es NULL.

## Sintaxis de Analyze

```python
func.insert(<str>, <pos>, <len>, <newstr>)
```

## Ejemplos de Analyze

```python
func.insert('Quadratic', 3, 4, 'What')
┌────────────────────────────────────────┐
│ func.insert('Quadratic', 3, 4, 'What') │
├────────────────────────────────────────┤
│ QuWhattic                              │
└────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
INSERT(<str>, <pos>, <len>, <newstr>)
```

## Argumentos

| Argumentos  | Descripción     |
|------------|-----------------|
| `<str>`    | La cadena.     |
| `<pos>`    | La posición.   |
| `<len>`    | La longitud.     |
| `<newstr>` | La nueva cadena. |

## Tipo de retorno

`VARCHAR`

## Ejemplos de SQL

```sql
SELECT INSERT('Quadratic', 3, 4, 'What');
┌───────────────────────────────────┐
│ INSERT('Quadratic', 3, 4, 'What') │
├───────────────────────────────────┤
│ QuWhattic                         │
└───────────────────────────────────┘

SELECT INSERT('Quadratic', -1, 4, 'What');
┌───────────────────────────────────────┐
│ INSERT('Quadratic', (- 1), 4, 'What') │
├───────────────────────────────────────┤
│ Quadratic                             │
└───────────────────────────────────────┘

SELECT INSERT('Quadratic', 3, 100, 'What');
┌─────────────────────────────────────┐
│ INSERT('Quadratic', 3, 100, 'What') │
├─────────────────────────────────────┤
│ QuWhat                              │
└─────────────────────────────────────┘

┌────────────────────────────────────────────┬────────┐
│ INSERT('123456789', number, number, 'aaa') │ number │
├────────────────────────────────────────────┼────────┤
│ 123456789                                  │      0 │
│ aaa23456789                                │      1 │
│ 1aaa456789                                 │      2 │
│ 12aaa6789                                  │      3 │
│ 123aaa89                                   │      4 │
│ 1234aaa                                    │      5 │
│ 12345aaa                                   │      6 │
│ 123456aaa                                  │      7 │
│ 1234567aaa                                 │      8 │
│ 12345678aaa                                │      9 │
│ 123456789                                  │     10 │
│ 123456789                                  │     11 │
│ 123456789                                  │     12 │
└────────────────────────────────────────────┴────────┘
```
