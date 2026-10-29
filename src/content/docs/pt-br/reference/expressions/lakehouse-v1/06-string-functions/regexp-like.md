---
title: REGEXP_LIKE (Lakehouse v1)
description: REGEXP_LIKE — a função REGEXP_LIKE é usada para verificar se a string corresponde à expressão regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-like.md
---

A função REGEXP_LIKE é usada para verificar se a string corresponde à expressão regular.

## Sintaxe do Analyze

```python
func.regexp_like(<expr>, <pat[, match_type]>)
```

## Exemplos do Analyze

```python
func.regexp_like('a', '^[a-d]')
┌─────────────────────────────────┐
│ func.regexp_like('a', '^[a-d]') │
├─────────────────────────────────┤
│                               1 │
└─────────────────────────────────┘
```

## Sintaxe SQL

```sql
REGEXP_LIKE(<expr>, <pat[, match_type]>)
```

## Argumentos

| Argumentos     | Descrição                                                                              |
|----------------|----------------------------------------------------------------------------------------|
| `<expr>`       | A string expr a ser comparada                                                          |
| `<pat>`        | A expressão regular                                                                    |
| `[match_type]` | Opcional. O argumento match_type é uma string que especifica como realizar a correspondência |

`match_type` pode conter qualquer um ou todos os seguintes caracteres:

* `c`: correspondência que diferencia maiúsculas de minúsculas.
* `i`: correspondência que não diferencia maiúsculas de minúsculas.
* `m`: modo de várias linhas. Reconhece terminadores de linha dentro da string. O comportamento padrão é fazer a correspondência de terminadores de linha apenas no início e no fim da expressão de string.
* `n`: o caractere `.` corresponde a terminadores de linha. O padrão é que a correspondência de `.` pare no fim de uma linha.
* `u`: finais de linha somente Unix. Não é compatível no momento.

## Tipo de retorno

`BIGINT`
Retorna `1` se a string expr corresponder à expressão regular especificada pelo padrão pat; caso contrário, retorna `0`. Se expr ou pat for NULL, o valor retornado é NULL.

## Exemplos de SQL

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
