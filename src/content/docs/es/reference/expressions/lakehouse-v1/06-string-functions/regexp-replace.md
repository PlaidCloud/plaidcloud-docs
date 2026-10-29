---
title: REGEXP_REPLACE (Lakehouse v1)
description: REGEXP_REPLACE — reemplaza las apariciones en la cadena expr que coinciden con la expresión regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-replace.md
---

Reemplaza las apariciones en la cadena `expr` que coinciden con la expresión regular especificada por el patrón `pat` por la cadena de reemplazo `repl` y devuelve la cadena resultante. Si `expr`, `pat` o `repl` es NULL, el valor devuelto es NULL.

## Sintaxis de Analyze

```python
func.regexp_replace(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Ejemplos de Analyze

```python
func.regexp_replace('a b c', 'b', 'X')
┌────────────────────────────────────────┐
│ func.regexp_replace('a b c', 'b', 'X') │
├────────────────────────────────────────┤
│ a X c                                  │
└────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
REGEXP_REPLACE(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Argumentos

| Argumentos  | Descripción                                                                                                             |
|------------|-------------------------------------------------------------------------------------------------------------------------|
| expr       | La cadena expr que se va a comparar                                                                                      |
| pat        | La expresión regular                                                                                                  |
| repl       | La cadena de reemplazo                                                                                                  |
| pos        | Opcional. La posición de expr en la que se inicia la búsqueda. Si se omite, el valor predeterminado es 1.                              |
| occurrence | Opcional. Qué aparición de una coincidencia se reemplaza. Si se omite, el valor predeterminado es 0 (que significa «reemplazar todas las apariciones»). |
| match_type | Opcional. Una cadena que especifica cómo se realiza la coincidencia. El significado es el descrito para REGEXP_LIKE().               |

## Tipo de retorno

`VARCHAR`

## Ejemplos de SQL

```sql
SELECT REGEXP_REPLACE('a b c', 'b', 'X');
┌───────────────────────────────────┐
│ REGEXP_REPLACE('a b c', 'b', 'X') │
├───────────────────────────────────┤
│ a X c                             │
└───────────────────────────────────┘

SELECT REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3);
┌────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3) │
├────────────────────────────────────────────────────┤
│ abc def X                                          │
└────────────────────────────────────────────────────┘

SELECT REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2);
┌───────────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2)        │
├───────────────────────────────────────────────────────────┤
│ 周 周周 X                                                 │
└───────────────────────────────────────────────────────────┘
```
