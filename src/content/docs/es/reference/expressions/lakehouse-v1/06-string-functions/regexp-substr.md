---
title: REGEXP_SUBSTR (Lakehouse v1)
description: REGEXP_SUBSTR — devuelve la subcadena de la cadena expr que coincide con la expresión regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-substr.md
---

Devuelve la subcadena de la cadena `expr` que coincide con la expresión regular especificada por el patrón `pat`, o NULL si no hay coincidencia. Si expr o pat es NULL, el valor devuelto es NULL.

## Sintaxis de Analyze

```python
func.regexp_substr(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Ejemplos de Analyze

```python
func.regexp_substr('abc def ghi', '[a-z]+')
┌─────────────────────────────────────────────┐
│ func.regexp_substr('abc def ghi', '[a-z]+') │
├─────────────────────────────────────────────┤
│ abc                                         │
└─────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
REGEXP_SUBSTR(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Argumentos

| Argumentos  | Descripción                                                                                               |
|------------|-----------------------------------------------------------------------------------------------------------|
| expr       | La cadena expr que se va a comparar                                                                        |
| pat        | La expresión regular                                                                                    |
| pos        | Opcional. La posición de expr en la que se inicia la búsqueda. Si se omite, el valor predeterminado es 1.                |
| occurrence | Opcional. Qué aparición de una coincidencia se busca. Si se omite, el valor predeterminado es 1.                        |
| match_type | Opcional. Una cadena que especifica cómo se realiza la coincidencia. El significado es el descrito para REGEXP_LIKE(). |

## Tipo de retorno

`VARCHAR`

## Ejemplos de SQL

```sql
SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+');
┌────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+') │
├────────────────────────────────────────┤
│ abc                                    │
└────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3);
┌──────────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3) │
├──────────────────────────────────────────────┤
│ ghi                                          │
└──────────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3);
┌──────────────────────────────────────────────────────────────────┐
│ REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3)            │
├──────────────────────────────────────────────────────────────────┤
│ 周周周周                                                         │
└──────────────────────────────────────────────────────────────────┘

```
