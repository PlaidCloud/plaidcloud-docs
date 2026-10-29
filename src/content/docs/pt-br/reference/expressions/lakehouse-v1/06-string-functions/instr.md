---
title: INSTR (Lakehouse v1)
description: INSTR — retorna a posição da primeira ocorrência da substring substr na string str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/instr.md
---

Retorna a posição da primeira ocorrência da substring substr na string str.
É igual à forma de dois argumentos de LOCATE(), exceto que a ordem dos argumentos é invertida.

## Sintaxe do Analyze

```python
func.instr(<str>, <substr>)
```

## Exemplos do Analyze

```python
func.instr('foobarbar', 'bar')
┌────────────────────────────────┐
│ func.instr('foobarbar', 'bar') │
├────────────────────────────────┤
│                              4 │
└────────────────────────────────┘
```

## Sintaxe SQL

```sql
INSTR(<str>, <substr>)
```

## Argumentos

| Argumentos | Descrição         |
|------------|-------------------|
| `<str>`    | A string.         |
| `<substr>` | A substring.      |

## Tipo de retorno

`BIGINT`

## Exemplos de SQL

```sql
SELECT INSTR('foobarbar', 'bar');
┌───────────────────────────┐
│ INSTR('foobarbar', 'bar') │
├───────────────────────────┤
│                         4 │
└───────────────────────────┘

SELECT INSTR('xbar', 'foobar');
┌─────────────────────────┐
│ INSTR('xbar', 'foobar') │
├─────────────────────────┤
│                       0 │
└─────────────────────────┘
```
