---
title: LTRIM (Lakehouse v1)
description: LTRIM — remove do lado esquerdo da cadeia de caracteres todas as ocorrências de qualquer caráter presente na cadeia de remoção especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ltrim.md
---

Remove do lado esquerdo da cadeia de caracteres todas as ocorrências de qualquer caráter presente na cadeia de remoção especificada.

Veja também: 

- [TRIM_LEADING](../trim-leading)
- [RTRIM](../rtrim)

## Sintaxe do Analyze

```python
func.ltrim(<string>, <trim_string>)
```

## Exemplos do Analyze

```python
func.ltrim('xxdatabend', 'x')
┌────────────────────────────────┐
│ func.ltrim('xxdatabend', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## Sintaxe SQL

```sql
LTRIM(<string>, <trim_string>)
```

## Exemplos SQL

```sql
SELECT LTRIM('xxdatabend', 'xx'), LTRIM('xxdatabend', 'xy');

┌───────────────────────────────────────────────────────┐
│ ltrim('xxdatabend', 'xx') │ ltrim('xxdatabend', 'xy') │
├───────────────────────────┼───────────────────────────┤
│ databend                  │ databend                  │
└───────────────────────────────────────────────────────┘
```
