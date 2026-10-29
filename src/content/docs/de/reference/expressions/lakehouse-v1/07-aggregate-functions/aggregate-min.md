---
title: MIN (Lakehouse v1)
description: MIN – gibt den Minimalwert aus einer Wertemenge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min.md
---

Aggregatfunktion.

Die Funktion MIN() gibt den Minimalwert aus einer Wertemenge zurück.

## Analyze-Syntax

```python
func.min(<column>)
```

## Analyze-Beispiele

```python
table.station_id, func.min(table.price).alias('min_price')

| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```

## SQL-Syntax

```sql
MIN(<expr>)
```

## Argumente

| Argumente | Beschreibung   |
|-----------|----------------|
| `<expr>`  | Beliebiger Ausdruck |

## Rückgabetyp

Der Minimalwert im Typ des Werts.

## SQL-Beispiele

---
title: MIN
---

Aggregatfunktion.

Die Funktion MIN() gibt den Minimalwert aus einer Wertemenge zurück.

## SQL-Syntax

```sql
MIN(expression)
```

## Argumente

| Argumente   | Beschreibung |
| ----------- | ----------- |
| expression  | Beliebiger Ausdruck |

## Rückgabetyp

Der Minimalwert im Typ des Werts.

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
```sql
CREATE TABLE gas_prices (
  id INT,
  station_id INT,
  price FLOAT
);

INSERT INTO gas_prices (id, station_id, price)
VALUES (1, 1, 3.50),
       (2, 1, 3.45),
       (3, 1, 3.55),
       (4, 2, 3.40),
       (5, 2, 3.35);
```

**Abfragedemo: Minimalen Benzinpreis für Station 1 ermitteln**
```sql
SELECT station_id, MIN(price) AS min_price
FROM gas_prices
WHERE station_id = 1
GROUP BY station_id;
```

**Ergebnis**
```sql
| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```
