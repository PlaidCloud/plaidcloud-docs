---
title: JSON_ARRAY_TRANSFORM (Lakehouse v1)
description: JSON_ARRAY_TRANSFORM — przekształca każdy element tablicy JSON za pomocą określonego wyrażenia Lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-transform.md
---

Przekształca każdy element tablicy JSON za pomocą określonego wyrażenia Lambda. Więcej informacji o wyrażeniach Lambda znajdziesz w sekcji Wyrażenia Lambda.

## Składnia SQL

```sql
JSON_ARRAY_TRANSFORM(<json_array>, <lambda_expression>)
```

## Aliasy

- [JSON_ARRAY_APPLY](../json-array-apply)
- [JSON_ARRAY_MAP](../json-array-map)

## Typ zwracany

Tablica JSON.

## Przykłady SQL

W tym przykładzie każdy element liczbowy tablicy jest mnożony przez 10, co przekształca oryginalną tablicę w `[10, 20, 30, 40]`:

```sql
SELECT JSON_ARRAY_TRANSFORM(
    [1, 2, 3, 4]::JSON,
    data -> (data::Int * 10)
);

-[ RECORD 1 ]-----------------------------------
json_array_transform([1, 2, 3, 4]::VARIANT, data -> data::Int32 * 10): [10,20,30,40]
```
