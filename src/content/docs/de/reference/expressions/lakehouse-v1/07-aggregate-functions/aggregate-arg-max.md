---
title: ARG_MAX (Lakehouse v1)
description: ARG_MAX – berechnet den arg-Wert zum größten val-Wert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-max.md
---

Berechnet den `arg`-Wert zum größten `val`-Wert. Wenn es mehrere `arg`-Werte für die größten `val`-Werte gibt, wird der erste dieser gefundenen Werte zurückgegeben.

## Analyze-Syntax

```python
func.arg_max(<expr>)
```

## Analyze-Beispiele

```python
func.arg_max(table.product, table.price).alias('max_price_product')

| max_price_product |
| ----------------- |
| Product C         |
```

## SQL-Syntax

```sql
ARG_MAX(<arg>, <val>)
```

## Argumente

| Argumente | Beschreibung                                                                                      |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | Argument eines beliebigen Datentyps, den PlaidCloud Lakehouse unterstützt |
| `<val>`   | Wert eines beliebigen Datentyps, den PlaidCloud Lakehouse unterstützt     |

## Rückgabetyp

`arg`-Wert, der dem größten `val`-Wert entspricht.

 entspricht dem `arg`-Typ.

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**

Erstellen wir eine Tabelle mit dem Namen „sales“ und fügen einige Beispieldaten ein:
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

**Abfrage: Funktion ARG_MAX() verwenden**

Nun verwenden wir die Funktion ARG_MAX(), um das Produkt mit dem höchsten Preis zu finden:
```sql
SELECT ARG_MAX(product, price) AS max_price_product
FROM sales;
```

Das Ergebnis sollte wie folgt aussehen:
```sql
| max_price_product |
| ----------------- |
| Product C         |
```
