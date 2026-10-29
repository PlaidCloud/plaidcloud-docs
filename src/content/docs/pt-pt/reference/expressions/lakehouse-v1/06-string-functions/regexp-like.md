---
title: REGEXP_LIKE (Lakehouse v1)
description: REGEXP_LIKE — a função REGEXP_LIKE é utilizada para verificar se a cadeia de caracteres corresponde à expressão regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-like.md
---

A função REGEXP_LIKE é utilizada para verificar se a cadeia de caracteres corresponde à expressão regular.

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

| Argumentos     | Descrição                                                                                 |
|----------------|-------------------------------------------------------------------------------------------|
| `<expr>`       | A cadeia de caracteres expr a corresponder                                                |
| `<pat>`        | A expressão regular                                                                       |
| `[match_type]` | Opcional. O argumento match_type é uma cadeia de caracteres que especifica como efetuar a correspondência |

`match_type` pode conter qualquer um ou todos os seguintes caracteres:

* `c`: correspondência com distinção entre maiúsculas e minúsculas.
* `i`: correspondência sem distinção entre maiúsculas e minúsculas.
* `m`: modo de várias linhas. Reconhece terminadores de linha dentro da cadeia de caracteres. O comportamento predefinido é fazer corresponder terminadores de linha apenas no início e no fim da expressão de cadeia de caracteres.
* `n`: o caráter `.` corresponde a terminadores de linha. Por predefinição, a correspondência de `.` termina no fim de uma linha.
* `u`: terminações de linha apenas Unix. Não é suportado atualmente.

## Tipo de Retorno

`BIGINT`
Devolve `1` se a cadeia de caracteres expr corresponder à expressão regular especificada pelo padrão pat, e `0` caso contrário. Se expr ou pat for NULL, o valor devolvido é NULL.

## Exemplos SQL

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
