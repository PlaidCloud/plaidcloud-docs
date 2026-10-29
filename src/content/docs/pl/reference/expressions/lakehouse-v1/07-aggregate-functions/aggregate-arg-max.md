---
title: ARG_MAX (Lakehouse v1)
description: ARG_MAX — oblicza wartość arg dla maksymalnej wartości val.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-max.md
---

Oblicza wartość `arg` dla maksymalnej wartości `val`. Jeśli dla maksymalnych wartości `val` istnieje kilka wartości `arg`, zwraca pierwszą z napotkanych.

## Składnia Analyze

```python
func.arg_max(<expr>)
```

## Przykłady Analyze

```python
func.arg_max(table.product, table.price).alias('max_price_product')

| max_price_product |
| ----------------- |
| Product C         |
```

## Składnia SQL

```sql
ARG_MAX(<arg>, <val>)
```

## Argumenty

| Argumenty | Opis                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | Argument dowolnego typu danych obsługiwanego przez PlaidCloud Lakehouse |
| `<val>`   | Wartość dowolnego typu danych obsługiwanego przez PlaidCloud Lakehouse  |

## Typ zwracany

Wartość `arg` odpowiadająca maksymalnej wartości `val`.

 odpowiada typowi `arg`.

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**

Utwórzmy tabelę o nazwie „sales” i wstawmy do niej przykładowe dane:
```sql
CREATE TABLE sales (
  id INTEGER,
  product VARCHAR(50),
  price FLOAT
);

INSERT INTO sales (id, product, price)
VALUES (1, 'Product A', 10.5),
       (2, 'Product B', 20.75),
       (3, 'Product C', 30.0),
       (4, 'Product D', 15.25),
       (5, 'Product E', 25.5);
```

**Zapytanie: użycie funkcji ARG_MAX()**

Użyjmy teraz funkcji ARG_MAX(), aby znaleźć produkt o maksymalnej cenie:
```sql
SELECT ARG_MAX(product, price) AS max_price_product
FROM sales;
```

Wynik powinien wyglądać następująco:
```sql
| max_price_product |
| ----------------- |
| Product C         |
```
