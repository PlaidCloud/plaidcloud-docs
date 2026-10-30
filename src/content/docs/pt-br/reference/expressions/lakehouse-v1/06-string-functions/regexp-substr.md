---
title: REGEXP_SUBSTR (Lakehouse v1)
description: REGEXP_SUBSTR — retorna a substring da string expr que corresponde à expressão regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-substr.md
---

Retorna a substring da string `expr` que corresponde à expressão regular especificada pelo padrão `pat`, ou NULL se não houver correspondência. Se expr ou pat for NULL, o valor retornado é NULL.

## Sintaxe do Analyze

```python
func.regexp_substr(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Exemplos do Analyze

```python
func.regexp_substr('abc def ghi', '[a-z]+')
┌─────────────────────────────────────────────┐
│ func.regexp_substr('abc def ghi', '[a-z]+') │
├─────────────────────────────────────────────┤
│ abc                                         │
└─────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
REGEXP_SUBSTR(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Argumentos

| Argumentos | Descrição                                                                                                    |
|------------|--------------------------------------------------------------------------------------------------------------|
| expr       | A string expr a ser comparada                                                                                |
| pat        | A expressão regular                                                                                          |
| pos        | Opcional. A posição em expr em que a busca começa. Se omitido, o padrão é 1.                                 |
| occurrence | Opcional. Qual ocorrência de uma correspondência deve ser buscada. Se omitido, o padrão é 1.                 |
| match_type | Opcional. Uma string que especifica como realizar a correspondência. O significado é o descrito para REGEXP_LIKE(). |

## Tipo de retorno

`VARCHAR`

## Exemplos de SQL

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
