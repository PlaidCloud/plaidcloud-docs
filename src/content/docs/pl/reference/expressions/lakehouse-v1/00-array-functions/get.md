---
title: "GET (tablica, Lakehouse v1)"
description: GET — zwraca element tablicy według indeksu (liczonego od 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/get.md
---

Zwraca element tablicy według indeksu (liczonego od 1).

## Składnia Analyze

```python
func.get( <array>, <index> )
```

## Przykłady Analyze

```python
func.get([1, 2], 2)

┌─────────────────────┐
│ func.get([1, 2], 2) │
├─────────────────────┤
│                   2 │
└─────────────────────┘
```

## Składnia SQL

```sql
GET( <array>, <index> )
```

## Aliasy

- [ARRAY_GET](../array-get)

## Przykłady SQL

```sql
SELECT GET([1, 2], 2), ARRAY_GET([1, 2], 2);

┌───────────────────────────────────────┐
│ get([1, 2], 2) │ array_get([1, 2], 2) │
├────────────────┼──────────────────────┤
│              2 │                    2 │
└───────────────────────────────────────┘
```
