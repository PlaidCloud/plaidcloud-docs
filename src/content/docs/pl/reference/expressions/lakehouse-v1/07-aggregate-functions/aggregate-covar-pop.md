---
title: COVAR_POP (Lakehouse v1)
description: COVAR_POP — zwraca kowariancję z populacji dla zbioru par liczb.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-covar-pop.md
---

COVAR_POP zwraca kowariancję z populacji dla zbioru par liczb. 

## Składnia Analyze

```python
func.covar_pop(<expr1>, <expr2>)
```

## Przykłady Analyze

```python
func.covar_pop(table.units_sold, table.revenue).alias('covar_pop_units_revenue')

| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```

## Składnia SQL

```sql
COVAR_POP(<expr1>, <expr2>)
```

## Argumenty

| Argumenty |          Opis            |
|-----------| ------------------------ |
| `<expr1>` | Dowolne wyrażenie liczbowe |
| `<expr2>` | Dowolne wyrażenie liczbowe |

## Typ zwracany

float64

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE product_sales (
  id INT,
  product_id INT,
  units_sold INT,
  revenue FLOAT
);

INSERT INTO product_sales (id, product_id, units_sold, revenue)
VALUES (1, 1, 10, 1000),
       (2, 2, 20, 2000),
       (3, 3, 30, 3000),
       (4, 4, 40, 4000),
       (5, 5, 50, 5000);
```

**Przykład zapytania: obliczenie kowariancji z populacji między sprzedaną liczbą jednostek a przychodem**

```sql
SELECT COVAR_POP(units_sold, revenue) AS covar_pop_units_revenue
FROM product_sales;
```

**Wynik**
```sql
| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```
