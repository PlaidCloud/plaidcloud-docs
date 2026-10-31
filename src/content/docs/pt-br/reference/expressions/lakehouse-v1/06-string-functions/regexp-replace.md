---
title: REGEXP_REPLACE (Lakehouse v1)
description: REGEXP_REPLACE — substitui as ocorrências na string expr que correspondem à expressão regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-replace.md
---

Substitui as ocorrências na string `expr` que correspondem à expressão regular especificada pelo padrão `pat` pela string de substituição `repl` e retorna a string resultante. Se `expr`, `pat` ou `repl` for NULL, o valor retornado é NULL.

## Sintaxe do Analyze

```python
func.regexp_replace(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Exemplos do Analyze

```python
func.regexp_replace('a b c', 'b', 'X')
┌────────────────────────────────────────┐
│ func.regexp_replace('a b c', 'b', 'X') │
├────────────────────────────────────────┤
│ a X c                                  │
└────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
REGEXP_REPLACE(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Argumentos

| Argumentos | Descrição                                                                                                                         |
|------------|-----------------------------------------------------------------------------------------------------------------------------------|
| expr       | A string expr a ser comparada                                                                                                     |
| pat        | A expressão regular                                                                                                               |
| repl       | A string de substituição                                                                                                          |
| pos        | Opcional. A posição em expr em que a busca começa. Se omitido, o padrão é 1.                                                      |
| occurrence | Opcional. Qual ocorrência de uma correspondência deve ser substituída. Se omitido, o padrão é 0 (que significa "substituir todas as ocorrências"). |
| match_type | Opcional. Uma string que especifica como realizar a correspondência. O significado é o descrito para REGEXP_LIKE().               |

## Tipo de retorno

`VARCHAR`

## Exemplos de SQL

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
