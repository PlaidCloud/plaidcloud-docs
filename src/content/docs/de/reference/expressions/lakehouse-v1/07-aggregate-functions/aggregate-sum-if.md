---
title: SUM_IF (Lakehouse v1)
description: SUM_IF – das Suffix -If kann an den Namen jeder Aggregatfunktion angehängt werden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-sum-if.md
---

Das Suffix -If kann an den Namen jeder Aggregatfunktion angehängt werden. In diesem Fall akzeptiert die Aggregatfunktion ein zusätzliches Argument – eine Bedingung.

## Analyze-Syntax

```python
func.sum_if(<column>, <cond>)
```

## Analyze-Beispiele

```python
func.sum_if(table.amount, table.status=='Completed').alias('total_amount_completed')

| total_amount_completed |
|------------------------|
|         270.0          |
```

## SQL-Syntax

```sql
SUM_IF(<column>, <cond>)
```

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
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

**Abfragedemo: Gesamtbetrag der abgeschlossenen Bestellungen berechnen**
```sql
SELECT SUM_IF(amount, status = 'Completed') AS total_amount_completed
FROM order_data;
```

**Ergebnis**
```sql
| total_amount_completed |
|------------------------|
|         270.0          |
```
