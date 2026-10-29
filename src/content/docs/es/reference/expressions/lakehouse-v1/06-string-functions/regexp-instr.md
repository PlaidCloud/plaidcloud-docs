---
title: REGEXP_INSTR (Lakehouse v1)
description: REGEXP_INSTR — devuelve el índice inicial de la subcadena de la cadena expr que coincide con la expresión regular especificada por el patrón pat, o 0 si no hay coincidencia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-instr.md
---

Devuelve el índice inicial de la subcadena de la cadena `expr` que coincide con la expresión regular especificada por el patrón `pat`, o `0` si no hay coincidencia. Si `expr` o `pat` es NULL, el valor devuelto es NULL. Los índices de caracteres comienzan en `1`.

## Sintaxis de Analyze

```python
func.regexp_instr(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Ejemplos de Analyze

```python
func.regexp_instr('dog cat dog', 'dog')
┌─────────────────────────────────────────┐
│ func.regexp_instr('dog cat dog', 'dog') │
├─────────────────────────────────────────┤
│                                       1 │
└─────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
REGEXP_INSTR(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Argumentos

| Argumentos     | Descripción                                                                                                                                                                                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expr          | La cadena expr que se va a comparar                                                                                                                                                                                                                                     |
| pat           | La expresión regular                                                                                                                                                                                                                                                 |
| pos           | Opcional. La posición de expr en la que se inicia la búsqueda. Si se omite, el valor predeterminado es 1.                                                                                                                                                                             |
| occurrence    | Opcional. Qué aparición de una coincidencia se busca. Si se omite, el valor predeterminado es 1.                                                                                                                                                                                     |
| return_option | Opcional. Qué tipo de posición se devuelve. Si este valor es 0, REGEXP_INSTR() devuelve la posición del primer carácter de la subcadena coincidente. Si este valor es 1, REGEXP_INSTR() devuelve la posición siguiente a la subcadena coincidente. Si se omite, el valor predeterminado es 0. |
| match_type    | Opcional. Una cadena que especifica cómo se realiza la coincidencia. El significado es el descrito para REGEXP_LIKE().                                                                                                                                                              |

## Tipo de retorno

Un valor de tipo de datos numérico.

## Ejemplos de SQL

```sql
SELECT REGEXP_INSTR('dog cat dog', 'dog');
┌────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog') │
├────────────────────────────────────┤
│                                  1 │
└────────────────────────────────────┘

SELECT REGEXP_INSTR('dog cat dog', 'dog', 2);
┌───────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog', 2) │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{2}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{2}') │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{4}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{4}') │
├─────────────────────────────────────┤
│                                   8 │
└─────────────────────────────────────┘
```
