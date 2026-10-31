---
title: COLUMN_COMPRESSED_SIZE (Lakehouse v2)
description: COLUMN_COMPRESSED_SIZE — retorna o tamanho compactado, em bytes, de um valor de coluna.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-compressed-size.md
---

Retorna o tamanho compactado, em bytes, de um valor de coluna.

## Sintaxe do Analyze

```python
func.column_compressed_size(get_column(table, 'data'))
```

## Exemplos do Analyze

```python
func.column_compressed_size(get_column(table, 'data'))

┌─────┐
│ 128 │
└─────┘
```

## Sintaxe SQL

```sql
COLUMN_COMPRESSED_SIZE(<expr>)
```

## Exemplos de SQL

```sql
SELECT COLUMN_COMPRESSED_SIZE(data) FROM records LIMIT 1;

┌─────┐
│ 128 │
└─────┘
```
