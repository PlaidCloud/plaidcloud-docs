---
title: INSTR (Lakehouse v2)
description: INSTR — devolve a posição da primeira ocorrência de uma subcadeia numa cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/instr.md
---

Devolve a posição da primeira ocorrência de uma subcadeia numa cadeia.

## Sintaxe do Analyze

```python
func.instr(<str>, <substr>)
```

## Exemplos do Analyze

```python
func.instr('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## Sintaxe SQL

```sql
INSTR(<str>, <substr>)
```

## Exemplos SQL

```sql
SELECT INSTR('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
