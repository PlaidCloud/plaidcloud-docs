---
title: SUM_IF (Lakehouse v1)
description: SUM_IF — sufiks -If można dopisać do nazwy dowolnej funkcji agregującej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-sum-if.md
---

Sufiks -If można dopisać do nazwy dowolnej funkcji agregującej. W takim przypadku funkcja agregująca przyjmuje dodatkowy argument – warunek.

## Składnia Analyze

```python
func.sum_if(<column>, <cond>)
```

## Przykłady Analyze

```python
func.sum_if(table.amount, table.status=='Completed').alias('total_amount_completed')

| total_amount_completed |
|------------------------|
|         270.0          |
```

## Składnia SQL

```sql
SUM_IF(<column>, <cond>)
```

## Przykłady SQL

**Tworzenie tabeli i wstawianie przykładowych danych**
```sql
CREATE TABLE order_data (
  id INT,
  customer_id INT,
  amount FLOAT,
  status VARCHAR
);

INSERT INTO order_data (id, customer_id, amount, status)
VALUES (1, 1, 100, 'Completed'),
       (2, 2, 50, 'Completed'),
       (3, 3, 80, 'Cancelled'),
       (4, 4, 120, 'Completed'),
       (5, 5, 75, 'Cancelled');
```

**Przykład zapytania: obliczenie łącznej kwoty zrealizowanych zamówień**
```sql
SELECT SUM_IF(amount, status = 'Completed') AS total_amount_completed
FROM order_data;
```

**Wynik**
```sql
| total_amount_completed |
|------------------------|
|         270.0          |
```
