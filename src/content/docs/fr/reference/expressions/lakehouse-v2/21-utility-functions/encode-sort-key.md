---
title: ENCODE_SORT_KEY (Lakehouse v2)
description: "Utilisez la fonction utilitaire ENCODE_SORT_KEY dans PlaidCloud Lakehouse. Encode des valeurs en une clé de tri binaire qui préserve l'ordre de tri. Utile pour les clés de tri composites."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/encode-sort-key.md
---

Encode des valeurs en une clé de tri binaire qui préserve l'ordre de tri. Utile pour les clés de tri composites.

## Syntaxe Analyze

```python
func.encode_sort_key(get_column(table, 'col1'), get_column(table, 'col2'))
```

## Exemples Analyze

```python
func.encode_sort_key(get_column(table, 'name'), get_column(table, 'age'))

┌───────────────────┐
│ (binary sort key) │
└───────────────────┘
```

## Syntaxe SQL

```sql
ENCODE_SORT_KEY(<expr1>[, <expr2>, ...])
```

## Exemples SQL

```sql
SELECT HEX(ENCODE_SORT_KEY('Alice', 30));

┌────────────────────────┐
│ (hex-encoded sort key) │
└────────────────────────┘
```
