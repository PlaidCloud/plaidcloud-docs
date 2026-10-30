---
title: MAX (Lakehouse v1)
description: MAX – gibt den Maximalwert aus einer Wertemenge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max.md
---

Aggregatfunktion.

Die Funktion MAX() gibt den Maximalwert aus einer Wertemenge zurück.

## Analyze-Syntax

```python
func.max(<column>)
```

## Analyze-Beispiele

```python
table.city, func.max(table.temperature).alias('max_temperature')

|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```

## SQL-Syntax

```sql
MAX(<expr>)
```

## Argumente

| Argumente | Beschreibung |
|-----------| ----------- |
| `<expr>`  | Beliebiger Ausdruck |

## Rückgabetyp

Der Maximalwert im Typ des Werts.

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
```sql
CREATE TABLE temperatures (
  id INT,
  city VARCHAR,
  temperature FLOAT
);

INSERT INTO temperatures (id, city, temperature)
VALUES (1, 'New York', 30),
       (2, 'New York', 28),
       (3, 'New York', 32),
       (4, 'Los Angeles', 25),
       (5, 'Los Angeles', 27);
```

**Abfragedemo: Maximale Temperatur für New York City ermitteln**

```sql
SELECT city, MAX(temperature) AS max_temperature
FROM temperatures
WHERE city = 'New York'
GROUP BY city;
```

**Ergebnis**
```sql
|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```
