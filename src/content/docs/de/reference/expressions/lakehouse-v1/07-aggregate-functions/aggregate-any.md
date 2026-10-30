---
title: ANY (Lakehouse v1)
description: ANY – gibt den ersten gefundenen Wert ungleich NULL aus einer Menge zurück; das Ergebnis ist unbestimmt, wenn die Ausführungsreihenfolge variiert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-any.md
---

Aggregatfunktion.

Die Funktion ANY() wählt den ersten gefundenen Wert (ungleich NULL) aus, es sei denn, alle Zeilen haben in dieser Spalte NULL-Werte. Die Abfrage kann in beliebiger Reihenfolge und bei jeder Ausführung sogar in einer anderen Reihenfolge ausgeführt werden, daher ist das Ergebnis dieser Funktion unbestimmt. Um ein bestimmtes Ergebnis zu erhalten, können Sie stattdessen die Funktion ‚min‘ oder ‚max‘ anstelle von ‚any‘ verwenden.

## Analyze-Syntax

```python
func.any(<expr>)
```

## Analyze-Beispiele

```python
func.any(table.product_name).alias('any_product_name')

| any_product_name |
|------------------|
| Laptop           |
```

## SQL-Syntax

```sql
ANY(<expr>)
```

## Argumente

| Argumente | Beschreibung   |
|-----------|----------------|
| `<expr>`  | Beliebiger Ausdruck |

## Rückgabetyp

Der erste gefundene Wert (ungleich NULL) im Typ des Werts. Wenn alle Werte NULL sind, ist der Rückgabewert NULL.

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
```sql
CREATE TABLE product_data (
  id INT,
  product_name VARCHAR NULL,
  price FLOAT NULL
);

INSERT INTO product_data (id, product_name, price)
VALUES (1, 'Laptop', 1000),
       (2, NULL, 800),
       (3, 'Keyboard', NULL),
       (4, 'Mouse', 25),
       (5, 'Monitor', 150);
```

**Abfragedemo: Ersten gefundenen Produktnamen ungleich NULL abrufen**
```sql
SELECT ANY(product_name) AS any_product_name
FROM product_data;
```

**Ergebnis**
```sql
| any_product_name |
|------------------|
| Laptop           |
```
