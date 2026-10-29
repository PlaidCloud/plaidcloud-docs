---
title: COLUMN_COMPRESSED_SIZE (Lakehouse v2)
description: COLUMN_COMPRESSED_SIZE — renvoie la taille compressée, en octets, d'une valeur de colonne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-compressed-size.md
---

Renvoie la taille compressée, en octets, d'une valeur de colonne.

## Syntaxe Analyze

```python
func.column_compressed_size(get_column(table, 'data'))
```

## Exemples Analyze

```python
func.column_compressed_size(get_column(table, 'data'))

┌─────┐
│ 128 │
└─────┘
```

## Syntaxe SQL

```sql
COLUMN_COMPRESSED_SIZE(<expr>)
```

## Exemples SQL

```sql
SELECT COLUMN_COMPRESSED_SIZE(data) FROM records LIMIT 1;

┌─────┐
│ 128 │
└─────┘
```
