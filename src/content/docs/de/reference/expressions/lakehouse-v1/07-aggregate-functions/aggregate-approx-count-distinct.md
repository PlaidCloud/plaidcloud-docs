---
title: APPROX_COUNT_DISTINCT (Lakehouse v1)
description: APPROX_COUNT_DISTINCT – schätzt die Anzahl der eindeutigen Werte in einem Datensatz mit dem HyperLogLog-Algorithmus.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-approx-count-distinct.md
---

Schätzt die Anzahl der eindeutigen Werte in einem Datensatz mit dem [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)-Algorithmus. 

Der HyperLogLog-Algorithmus liefert mit wenig Speicher und Zeit eine Näherung der Anzahl eindeutiger Elemente. Erwägen Sie den Einsatz dieser Funktion bei großen Datensätzen, bei denen ein geschätztes Ergebnis akzeptabel ist. Im Austausch gegen etwas Genauigkeit ist dies eine schnelle und effiziente Methode, um Anzahlen eindeutiger Werte zu ermitteln.

Für ein exaktes Ergebnis verwenden Sie [COUNT_DISTINCT](../aggregate-count-distinct). Weitere Erläuterungen finden Sie unter [Beispiele](#sql-beispiele).

## Analyze-Syntax

```python
func.approx_count_distinct(<expr>)
```

## Analyze-Beispiele

```python
func.approx_count_distinct(table.user_id).alias('approx_distinct_user_count')

| approx_distinct_user_count |
|----------------------------|
|             4              |
```

## SQL-Syntax

```sql
APPROX_COUNT_DISTINCT(<expr>)
```

## Rückgabetyp

Ganzzahl.

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_name VARCHAR
);

INSERT INTO user_events (id, user_id, event_name)
VALUES (1, 1, 'Login'),
       (2, 2, 'Login'),
       (3, 3, 'Login'),
       (4, 1, 'Logout'),
       (5, 2, 'Logout'),
       (6, 4, 'Login'),
       (7, 1, 'Login');
```

**Abfragedemo: Anzahl der eindeutigen Benutzer-IDs schätzen**
```sql
SELECT APPROX_COUNT_DISTINCT(user_id) AS approx_distinct_user_count
FROM user_events;
```

**Ergebnis**
```sql
| approx_distinct_user_count |
|----------------------------|
|             4              |
```
