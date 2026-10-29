---
title: COUNT_IF (Lakehouse v1)
description: COUNT_IF — sufiks _IF można dopisać do nazwy dowolnej funkcji agregującej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-count-if.md
---

Sufiks `_IF` można dopisać do nazwy dowolnej funkcji agregującej. W takim przypadku funkcja agregująca przyjmuje dodatkowy argument – warunek.

## Składnia Analyze

```python
func.count_if(<column>, <cond>)
```

## Przykłady Analyze

```python
func.count_if(table.status, table.status=='Completed').alias('completed_orders')

| completed_orders |
|------------------|
|        3         |
```

## Przykład SQL
```sql
COUNT_IF(<column>, <cond>)
```

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE orders (
  id INT,
  customer_id INT,
  status VARCHAR,
  total FLOAT
);

INSERT INTO orders (id, customer_id, status, total)
VALUES (1, 1, 'completed', 100),
       (2, 2, 'completed', 200),
       (3, 1, 'pending', 150),
       (4, 3, 'completed', 250),
       (5, 2, 'pending', 300);
```

**Przykład zapytania: zliczenie zrealizowanych zamówień**
```sql
SELECT COUNT_IF(status, status = 'completed') AS completed_orders
FROM orders;
```

**Wynik**
```sql
| completed_orders |
|------------------|
|        3         |
```
