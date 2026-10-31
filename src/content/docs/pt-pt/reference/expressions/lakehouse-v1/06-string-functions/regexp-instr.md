---
title: REGEXP_INSTR (Lakehouse v1)
description: REGEXP_INSTR — devolve o índice inicial da subcadeia da cadeia de caracteres expr que corresponde à expressão regular especificada pelo padrão pat, ou 0 se não houver correspondência.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-instr.md
---

Devolve o índice inicial da subcadeia da cadeia de caracteres `expr` que corresponde à expressão regular especificada pelo padrão `pat`, ou `0` se não houver correspondência. Se `expr` ou `pat` for NULL, o valor devolvido é NULL. Os índices de caracteres começam em `1`.

## Sintaxe do Analyze

```python
func.regexp_instr(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Exemplos do Analyze

```python
func.regexp_instr('dog cat dog', 'dog')
┌─────────────────────────────────────────┐
│ func.regexp_instr('dog cat dog', 'dog') │
├─────────────────────────────────────────┤
│                                       1 │
└─────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
REGEXP_INSTR(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Argumentos

| Argumentos    | Descrição                                                                                                                                                                                                                                                                                  |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expr          | A cadeia de caracteres expr a corresponder                                                                                                                                                                                                                                                 |
| pat           | A expressão regular                                                                                                                                                                                                                                                                        |
| pos           | Opcional. A posição em expr a partir da qual iniciar a pesquisa. Se omitido, o valor predefinido é 1.                                                                                                                                                                                      |
| occurrence    | Opcional. Qual a ocorrência de uma correspondência a pesquisar. Se omitido, o valor predefinido é 1.                                                                                                                                                                                       |
| return_option | Opcional. Que tipo de posição devolver. Se este valor for 0, REGEXP_INSTR() devolve a posição do primeiro caráter da subcadeia correspondente. Se este valor for 1, REGEXP_INSTR() devolve a posição a seguir à subcadeia correspondente. Se omitido, o valor predefinido é 0.               |
| match_type    | Opcional. Uma cadeia de caracteres que especifica como efetuar a correspondência. O significado é o descrito para REGEXP_LIKE().                                                                                                                                                           |

## Tipo de Retorno

Um valor de tipo de dados numérico.

## Exemplos SQL

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
