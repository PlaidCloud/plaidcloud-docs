---
title: MAX_IF (Lakehouse v1)
description: MAX_IF – das Suffix _IF kann an den Namen jeder Aggregatfunktion angehängt werden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max-if.md
---

Das Suffix `_IF` kann an den Namen jeder Aggregatfunktion angehängt werden. In diesem Fall akzeptiert die Aggregatfunktion ein zusätzliches Argument – eine Bedingung.

## Analyze-Syntax

```python
func.max_if(<column>, <cond>)
```

## Analyze-Beispiele

```python
func.max_if(table.revenue, table.salesperson_id==1).alias('max_revenue_salesperson_1')

| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```

## SQL-Beispiel

```sql
MAX_IF(<column>, <cond>)
```

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
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

**Abfragedemo: Maximalen Umsatz für den Vertriebsmitarbeiter mit ID 1 ermitteln**

```sql
SELECT MAX_IF(revenue, salesperson_id = 1) AS max_revenue_salesperson_1
FROM sales;
```

**Ergebnis**
```sql
| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```
