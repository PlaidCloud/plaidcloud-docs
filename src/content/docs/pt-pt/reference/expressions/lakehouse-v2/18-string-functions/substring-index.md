---
title: SUBSTRING_INDEX (Lakehouse v2)
description: "Utilize a função de cadeia SUBSTRING_INDEX no PlaidCloud Lakehouse. Devolve uma subcadeia de uma cadeia antes ou depois de um número especificado de ocorrências do delimitador."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring-index.md
---

Devolve uma subcadeia de uma cadeia antes ou depois de um número especificado de ocorrências do delimitador.

## Sintaxe do Analyze

```python
func.substring_index(<str>, <delim>, <count>)
```

## Exemplos do Analyze

```python
func.substring_index('www.example.com', '.', 2)

┌───────────────┐
│ 'www.example'  │
└───────────────┘
```

## Sintaxe SQL

```sql
SUBSTRING_INDEX(<str>, <delim>, <count>)
```

## Exemplos SQL

```sql
SELECT SUBSTRING_INDEX('www.example.com', '.', 2);

┌─────────────┐
│ www.example  │
└─────────────┘
```
