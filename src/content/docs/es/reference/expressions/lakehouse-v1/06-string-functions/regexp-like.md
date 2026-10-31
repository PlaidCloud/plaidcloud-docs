---
title: REGEXP_LIKE (Lakehouse v1)
description: REGEXP_LIKE — la función REGEXP_LIKE se usa para comprobar si la cadena coincide con la expresión regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-like.md
---

La función REGEXP_LIKE se usa para comprobar si la cadena coincide con la expresión regular.

## Sintaxis de Analyze

```python
func.regexp_like(<expr>, <pat[, match_type]>)
```

## Ejemplos de Analyze

```python
func.regexp_like('a', '^[a-d]')
┌─────────────────────────────────┐
│ func.regexp_like('a', '^[a-d]') │
├─────────────────────────────────┤
│                               1 │
└─────────────────────────────────┘
```

## Sintaxis SQL

```sql
REGEXP_LIKE(<expr>, <pat[, match_type]>)
```

## Argumentos

| Argumentos      | Descripción                                                                       |
|----------------|-----------------------------------------------------------------------------------|
| `<expr>`       | La cadena expr que se va a comparar                                                |
| `<pat>`        | La expresión regular                                                            |
| `[match_type]` | Opcional. El argumento match_type es una cadena que especifica cómo se realiza la coincidencia |

`match_type` puede contener cualquiera de los siguientes caracteres, o todos ellos:

* `c`: coincidencia con distinción entre mayúsculas y minúsculas.
* `i`: coincidencia sin distinción entre mayúsculas y minúsculas.
* `m`: modo de varias líneas. Reconoce los terminadores de línea dentro de la cadena. El comportamiento predeterminado es hacer coincidir los terminadores de línea solo al inicio y al final de la expresión de cadena.
* `n`: el carácter `.` coincide con los terminadores de línea. De forma predeterminada, la coincidencia de `.` se detiene al final de una línea.
* `u`: finales de línea solo de Unix. Actualmente no se admite.

## Tipo de retorno

`BIGINT`
Devuelve `1` si la cadena expr coincide con la expresión regular especificada por el patrón pat; de lo contrario, devuelve `0`. Si expr o pat es NULL, el valor devuelto es NULL.

## Ejemplos de SQL

```sql
SELECT REGEXP_LIKE('a', '^[a-d]');
┌────────────────────────────┐
│ REGEXP_LIKE('a', '^[a-d]') │
├────────────────────────────┤
│                          1 │
└────────────────────────────┘

SELECT REGEXP_LIKE('abc', 'ABC');
┌───────────────────────────┐
│ REGEXP_LIKE('abc', 'ABC') │
├───────────────────────────┤
│                         1 │
└───────────────────────────┘

SELECT REGEXP_LIKE('abc', 'ABC', 'c');
┌────────────────────────────────┐
│ REGEXP_LIKE('abc', 'ABC', 'c') │
├────────────────────────────────┤
│                              0 │
└────────────────────────────────┘

SELECT REGEXP_LIKE('new*\n*line', 'new\\*.\\*line');

┌───────────────────────────────────────────┐
│ REGEXP_LIKE('new*\n*line', 'new\*.\*line')│
├───────────────────────────────────────────┤
│                                         0 │
└───────────────────────────────────────────┘

SELECT REGEXP_LIKE('new*\n*line', 'new\\*.\\*line', 'n');

┌────────────────────────────────────────────────┐
│ REGEXP_LIKE('new*\n*line', 'new\*.\*line', 'n')│
├────────────────────────────────────────────────┤
│                                              1 │
└────────────────────────────────────────────────┘
```
