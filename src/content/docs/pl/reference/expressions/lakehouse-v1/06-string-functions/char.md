---
title: CHAR (Lakehouse v1)
description: CHAR — zwraca znak odpowiadający każdej przekazanej liczbie całkowitej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/char.md
---

Zwraca znak odpowiadający każdej przekazanej liczbie całkowitej.

## Składnia Analyze

```python
func.char(N,...)
```

## Przykłady Analyze

```python
func.char(77,121,83,81,76)
┌─────────────────────────────┐
│ func.char(77,121,83,81,76) │
├─────────────────────────────┤
│ 4D7953514C                  │
└─────────────────────────────┘
```

## Składnia SQL

```sql
CHAR(N, ...)
```

## Argumenty

| Argumenty | Opis             |
|-----------|------------------|
| N         | Kolumna liczbowa |

## Typ zwracany

`BINARY`

## Przykłady SQL

Ten przykład pokazuje zarówno zwróconą wartość binarną, jak i jej reprezentację tekstową.

```sql
SELECT CHAR(77,121,83,81,76) as a, a::String;
┌────────────────────────┐
│      a     │ a::string │
│   Binary   │   String  │
├────────────┼───────────┤
│ 4D7953514C │ MySQL     │
└────────────────────────┘
```
