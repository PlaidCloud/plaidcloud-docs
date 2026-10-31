---
title: REPEAT (Lakehouse v2)
description: REPEAT — repete uma cadeia um número especificado de vezes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/repeat.md
---

Repete uma cadeia um número especificado de vezes.

## Sintaxe do Analyze

```python
func.repeat(<str>, <n>)
```

## Exemplos do Analyze

```python
func.repeat('ab', 3)

┌──────────┐
│ 'ababab'  │
└──────────┘
```

## Sintaxe SQL

```sql
REPEAT(<str>, <n>)
```

## Exemplos SQL

```sql
SELECT REPEAT('ab', 3);

┌────────┐
│ ababab  │
└────────┘
```
