---
title: MAX_IF (Lakehouse v1)
description: MAX_IF — sufiks _IF można dopisać do nazwy dowolnej funkcji agregującej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max-if.md
---

Sufiks `_IF` można dopisać do nazwy dowolnej funkcji agregującej. W takim przypadku funkcja agregująca przyjmuje dodatkowy argument – warunek.

## Składnia Analyze

```python
func.max_if(<column>, <cond>)
```

## Przykłady Analyze

```python
func.max_if(table.revenue, table.salesperson_id==1).alias('max_revenue_salesperson_1')

| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```

## Przykład SQL

```sql
MAX_IF(<column>, <cond>)
```

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE sales (
  id INT,
  salesperson_id INT,
  product_id INT,
  revenue FLOAT
);

INSERT INTO sales (id, salesperson_id, product_id, revenue)
VALUES (1, 1, 1, 1000),
       (2, 1, 2, 2000),
       (3, 1, 3, 3000),
       (4, 2, 1, 1500),
       (5, 2, 2, 2500);
```

**Przykład zapytania: znalezienie maksymalnego przychodu sprzedawcy o identyfikatorze 1**

```sql
SELECT MAX_IF(revenue, salesperson_id = 1) AS max_revenue_salesperson_1
FROM sales;
```

**Wynik**
```sql
| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```
