---
title: SUBSTRING_INDEX (Lakehouse v2)
description: "Use a função de string SUBSTRING_INDEX no PlaidCloud Lakehouse. Retorna uma substring de uma string, antes ou depois de um número especificado de ocorrências de um delimitador."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring-index.md
---

Retorna uma substring de uma string, antes ou depois de um número especificado de ocorrências de um delimitador.

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

## Exemplos de SQL

```sql
SELECT SUBSTRING_INDEX('www.example.com', '.', 2);

┌─────────────┐
│ www.example  │
└─────────────┘
```
