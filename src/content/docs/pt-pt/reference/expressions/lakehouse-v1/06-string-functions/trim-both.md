---
title: TRIM_BOTH (Lakehouse v1)
description: TRIM_BOTH — remove todas as ocorrências da cadeia de remoção especificada do início, do fim ou de ambos os lados da cadeia de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-both.md
---

Remove todas as ocorrências da cadeia de remoção especificada do início, do fim ou de ambos os lados da cadeia de caracteres.

Veja também: [TRIM](../trim)

## Sintaxe do Analyze

```python
func.trim_both(<string>, <trim_string>)
```

## Exemplos do Analyze

```python
func.trim_both('xxdatabendxx', 'x')
┌──────────────────────────────────────┐
│ func.trim_both('xxdatabendxx', 'x')  │
├──────────────────────────────────────┤
│ databend                             │
└──────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TRIM_BOTH(<string>, <trim_string>)
```

## Exemplos SQL

```sql
SELECT TRIM_BOTH('xxdatabendxx', 'xxx'), TRIM_BOTH('xxdatabendxx', 'xx'), TRIM_BOTH('xxdatabendxx', 'x');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_both('xxdatabendxx', 'xxx') │ trim_both('xxdatabendxx', 'xx') │ trim_both('xxdatabendxx', 'x') │
├──────────────────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ xxdatabendxx                     │ databend                        │ databend                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
