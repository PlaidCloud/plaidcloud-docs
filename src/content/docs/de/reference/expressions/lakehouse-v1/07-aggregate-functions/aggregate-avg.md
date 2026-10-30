---
title: AVG (Lakehouse v1)
description: AVG – gibt den Durchschnittswert eines Ausdrucks zurück und ignoriert dabei NULL-Werte.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg.md
---

Aggregatfunktion.

Die Funktion AVG() gibt den Durchschnittswert eines Ausdrucks zurück.

**Hinweis:** NULL-Werte werden nicht mitgezählt.


## Analyze-Syntax

```python
func.avg(<column>)
```

## Analyze-Beispiele

```python
func.avg(table.price).alias('avg_price')

| avg_price |
| --------- |
| 20.4      |
```

## SQL-Syntax

```sql
AVG(<expr>)
```

## Argumente

| Argumente | Beschreibung             |
|-----------|--------------------------|
| `<expr>`  | Beliebiger numerischer Ausdruck |

## Rückgabetyp

double

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

**Abfrage: Funktion AVG() verwenden**

Nun verwenden wir die Funktion AVG(), um den Durchschnittspreis aller Produkte in der Tabelle „sales“ zu ermitteln:
```sql
SELECT AVG(price) AS avg_price
FROM sales;
```

Das Ergebnis sollte wie folgt aussehen:
```sql
| avg_price |
| --------- |
| 20.4      |
```
