---
title: REGEXP_INSTR (Lakehouse v1)
description: REGEXP_INSTR — retorna o índice inicial da substring da string expr que corresponde à expressão regular especificada pelo padrão pat, ou 0 se não houver correspondência.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-instr.md
---

Retorna o índice inicial da substring da string `expr` que corresponde à expressão regular especificada pelo padrão `pat`, ou `0` se não houver correspondência. Se `expr` ou `pat` for NULL, o valor retornado é NULL. Os índices de caracteres começam em `1`.

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

| Argumentos    | Descrição                                                                                                                                                                                                                                                                                         |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expr          | A string expr a ser comparada                                                                                                                                                                                                                                                                     |
| pat           | A expressão regular                                                                                                                                                                                                                                                                               |
| pos           | Opcional. A posição em expr em que a busca começa. Se omitido, o padrão é 1.                                                                                                                                                                                                                      |
| occurrence    | Opcional. Qual ocorrência de uma correspondência deve ser buscada. Se omitido, o padrão é 1.                                                                                                                                                                                                      |
| return_option | Opcional. Qual tipo de posição retornar. Se este valor for 0, REGEXP_INSTR() retorna a posição do primeiro caractere da substring correspondente. Se este valor for 1, REGEXP_INSTR() retorna a posição seguinte à substring correspondente. Se omitido, o padrão é 0.                               |
| match_type    | Opcional. Uma string que especifica como realizar a correspondência. O significado é o descrito para REGEXP_LIKE().                                                                                                                                                                               |

## Tipo de retorno

Um valor de tipo de dados numérico.

## Exemplos de SQL

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
