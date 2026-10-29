---
title: ENCODE_SORT_KEY (Lakehouse v2)
description: "Użyj funkcji narzędziowej ENCODE_SORT_KEY w PlaidCloud Lakehouse. Koduje wartości do binarnego klucza sortowania, który zachowuje kolejność sortowania. Przydatna dla złożonych kluczy sortowania."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/encode-sort-key.md
---

Koduje wartości do binarnego klucza sortowania, który zachowuje kolejność sortowania. Przydatna dla złożonych kluczy sortowania.

## Składnia Analyze

```python
func.encode_sort_key(get_column(table, 'col1'), get_column(table, 'col2'))
```

## Przykłady Analyze

```python
func.encode_sort_key(get_column(table, 'name'), get_column(table, 'age'))

┌───────────────────┐
│ (binary sort key) │
└───────────────────┘
```

## Składnia SQL

```sql
ENCODE_SORT_KEY(<expr1>[, <expr2>, ...])
```

## Przykłady SQL

```sql
SELECT HEX(ENCODE_SORT_KEY('Alice', 30));

┌────────────────────────┐
│ (hex-encoded sort key) │
└────────────────────────┘
```
