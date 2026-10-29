---
title: RTRIM (Lakehouse v1)
description: RTRIM — remove do lado direito da cadeia de caracteres todas as ocorrências de qualquer caráter presente na cadeia de remoção especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rtrim.md
---

Remove do lado direito da cadeia de caracteres todas as ocorrências de qualquer caráter presente na cadeia de remoção especificada.

Veja também: 

- [TRIM_TRAILING](../trim-trailing)
- [LTRIM](../ltrim)

## Sintaxe do Analyze

```python
func.rtrim(<string>, <trim_string>)
```

## Exemplos do Analyze

```python
func.rtrim('databend'xx, 'x')
┌────────────────────────────────┐
│ func.rtrim('databendxx', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## Sintaxe SQL

```sql
RTRIM(<string>, <trim_string>)
```

## Exemplos SQL

```sql
SELECT RTRIM('databendxx', 'x'), RTRIM('databendxx', 'xy');

┌──────────────────────────────────────────────────────┐
│ rtrim('databendxx', 'x') │ rtrim('databendxx', 'xy') │
├──────────────────────────┼───────────────────────────┤
│ databend                 │ databend                  │
└──────────────────────────────────────────────────────┘
```
