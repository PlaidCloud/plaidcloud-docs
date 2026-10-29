---
title: RTRIM (Lakehouse v1)
description: RTRIM — remove todas as ocorrências de qualquer caractere presente na string de remoção especificada do lado direito da string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rtrim.md
---

Remove todas as ocorrências de qualquer caractere presente na string de remoção especificada do lado direito da string.

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

## Exemplos de SQL

```sql
SELECT RTRIM('databendxx', 'x'), RTRIM('databendxx', 'xy');

┌──────────────────────────────────────────────────────┐
│ rtrim('databendxx', 'x') │ rtrim('databendxx', 'xy') │
├──────────────────────────┼───────────────────────────┤
│ databend                 │ databend                  │
└──────────────────────────────────────────────────────┘
```
