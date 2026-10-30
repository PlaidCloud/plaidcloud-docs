---
title: COVAR_POP (Lakehouse v1)
description: COVAR_POP – COVAR_POP gibt die Kovarianz der Grundgesamtheit für eine Menge von Zahlenpaaren zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-covar-pop.md
---

COVAR_POP gibt die Kovarianz der Grundgesamtheit für eine Menge von Zahlenpaaren zurück. 

## Analyze-Syntax

```python
func.covar_pop(<expr1>, <expr2>)
```

## Analyze-Beispiele

```python
func.covar_pop(table.units_sold, table.revenue).alias('covar_pop_units_revenue')

| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```

## SQL-Syntax

```sql
COVAR_POP(<expr1>, <expr2>)
```

## Argumente

| Argumente |        Beschreibung      |
|-----------| ------------------------ |
| `<expr1>` | Beliebiger numerischer Ausdruck |
| `<expr2>` | Beliebiger numerischer Ausdruck |

## Rückgabetyp

float64

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
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

**Abfragedemo: Kovarianz der Grundgesamtheit zwischen verkauften Einheiten und Umsatz berechnen**

```sql
SELECT COVAR_POP(units_sold, revenue) AS covar_pop_units_revenue
FROM product_sales;
```

**Ergebnis**
```sql
| covar_pop_units_revenue |
|-------------------------|
|        20000.0          |
```
