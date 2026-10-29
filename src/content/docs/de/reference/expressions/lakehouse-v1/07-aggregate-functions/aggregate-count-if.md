---
title: COUNT_IF (Lakehouse v1)
description: COUNT_IF – das Suffix _IF kann an den Namen jeder Aggregatfunktion angehängt werden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-count-if.md
---

Das Suffix `_IF` kann an den Namen jeder Aggregatfunktion angehängt werden. In diesem Fall akzeptiert die Aggregatfunktion ein zusätzliches Argument – eine Bedingung.

## Analyze-Syntax

```python
func.count_if(<column>, <cond>)
```

## Analyze-Beispiele

```python
func.count_if(table.status, table.status=='Completed').alias('completed_orders')

| completed_orders |
|------------------|
|        3         |
```

## SQL-Beispiel
```sql
COUNT_IF(<column>, <cond>)
```

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
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

**Abfragedemo: Abgeschlossene Bestellungen zählen**
```sql
SELECT COUNT_IF(status, status = 'completed') AS completed_orders
FROM orders;
```

**Ergebnis**
```sql
| completed_orders |
|------------------|
|        3         |
```
