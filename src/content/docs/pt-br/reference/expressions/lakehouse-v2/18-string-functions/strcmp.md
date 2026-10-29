---
title: STRCMP (Lakehouse v2)
description: "Use a função de string STRCMP no PlaidCloud Lakehouse. Compara duas strings lexicograficamente. Retorna 0 se forem iguais, -1 se str1 < str2, 1 se str1 > str2."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strcmp.md
---

Compara duas strings lexicograficamente. Retorna 0 se forem iguais, -1 se str1 &lt; str2, 1 se str1 > str2.

## Sintaxe do Analyze

```python
func.strcmp(<str1>, <str2>)
```

## Exemplos do Analyze

```python
func.strcmp('abc', 'abd')

┌────┐
│ -1  │
└────┘
```

## Sintaxe SQL

```sql
STRCMP(<str1>, <str2>)
```

## Exemplos de SQL

```sql
SELECT STRCMP('abc', 'abd');

┌────┐
│ -1  │
└────┘
```
