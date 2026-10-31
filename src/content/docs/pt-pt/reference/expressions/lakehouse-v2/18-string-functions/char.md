---
title: CHAR (Lakehouse v2)
description: CHAR — devolve o caráter correspondente a um determinado código ASCII.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char.md
---

Devolve o caráter correspondente a um determinado código ASCII.

## Sintaxe do Analyze

```python
func.char(<code>)
```

## Exemplos do Analyze

```python
func.char(65)

┌─────┐
│ 'A'  │
└─────┘
```

## Sintaxe SQL

```sql
CHAR(<code>)
```

## Exemplos SQL

```sql
SELECT CHAR(65);

┌───┐
│ A  │
└───┘
```
