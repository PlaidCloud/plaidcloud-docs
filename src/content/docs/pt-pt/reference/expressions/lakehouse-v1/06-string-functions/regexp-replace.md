---
title: REGEXP_REPLACE (Lakehouse v1)
description: REGEXP_REPLACE — substitui as ocorrências na cadeia de caracteres expr que correspondem à expressão regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-replace.md
---

Substitui as ocorrências na cadeia de caracteres `expr` que correspondem à expressão regular especificada pelo padrão `pat` pela cadeia de substituição `repl` e devolve a cadeia de caracteres resultante. Se `expr`, `pat` ou `repl` for NULL, o valor devolvido é NULL.

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

| Argumentos | Descrição                                                                                                                       |
|------------|---------------------------------------------------------------------------------------------------------------------------------|
| expr       | A cadeia de caracteres expr a corresponder                                                                                      |
| pat        | A expressão regular                                                                                                             |
| repl       | A cadeia de substituição                                                                                                        |
| pos        | Opcional. A posição em expr a partir da qual iniciar a pesquisa. Se omitido, o valor predefinido é 1.                           |
| occurrence | Opcional. Qual a ocorrência de uma correspondência a substituir. Se omitido, o valor predefinido é 0 (o que significa "substituir todas as ocorrências"). |
| match_type | Opcional. Uma cadeia de caracteres que especifica como efetuar a correspondência. O significado é o descrito para REGEXP_LIKE(). |

## Tipo de Retorno

`VARCHAR`

## Exemplos SQL

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
