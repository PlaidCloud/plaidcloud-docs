---
title: TO_YEAR (Lakehouse v1)
description: TO_YEAR — konwertuje datę lub datę z czasem (timestamp/datetime) na liczbę UInt16 zawierającą numer roku.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-year.md
---

Konwertuje datę lub datę z czasem (timestamp/datetime) na liczbę UInt16 zawierającą numer roku (n.e.).

## Składnia Analyze

```python
func.to_year(<expr>)
```

## Przykłady Analyze

```python
func.now(), func.to_year(func.now()), func.year(func.now())

┌───────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_year(func.now()) │ func.year(func.now()) │
├────────────────────────────┼──────────────────────────┼───────────────────────┤
│ 2024-03-14 23:37:03.895166 │                     2024 │                  2024 │
└───────────────────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_YEAR(<expr>)
```

## Argumenty

| Argumenty | Opis           |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Aliasy

- [YEAR](../year)

## Typ zwracany

 `SMALLINT`

## Przykłady SQL

```sql
SELECT NOW(), TO_YEAR(NOW()), YEAR(NOW());

┌───────────────────────────────────────────────────────────┐
│            now()           │ to_year(now()) │ year(now()) │
├────────────────────────────┼────────────────┼─────────────┤
│ 2024-03-14 23:37:03.895166 │           2024 │        2024 │
└───────────────────────────────────────────────────────────┘
```
