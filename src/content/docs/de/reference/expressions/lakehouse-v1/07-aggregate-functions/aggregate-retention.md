---
title: RETENTION (Lakehouse v1)
description: RETENTION – Aggregatfunktion.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-retention.md
---

Aggregatfunktion

Die Funktion RETENTION() nimmt als Argumente 1 bis 32 Bedingungen vom Typ UInt8 entgegen, die angeben, ob eine bestimmte Bedingung für das Ereignis erfüllt wurde.

Als Argument kann jede beliebige Bedingung angegeben werden (wie in WHERE).

Die Bedingungen mit Ausnahme der ersten gelten paarweise: Das Ergebnis der zweiten ist wahr, wenn die erste und die zweite wahr sind, das der dritten, wenn die erste und die dritte wahr sind, usw.

## Analyze-Syntax

```python
func.retention(<cond1> , <cond2> , ..., <cond32>)
```

## Analyze-Beispiele

```python
table.user_id, func.retention(table.event_type=='signup', table.event_type='login', table.event_type='purchase').alias('sales_amounts')

| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```

## SQL-Syntax

```sql
RETENTION( <cond1> , <cond2> , ..., <cond32> );
```

## Argumente

| Argumente | Beschreibung                                |
|-----------|---------------------------------------------|
| `<cond>`  | Ein Ausdruck, der ein boolesches Ergebnis liefert |

## Rückgabetyp

Das Array aus 1 oder 0.

## SQL-Beispiele

**Tabelle erstellen und Beispieldaten einfügen**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_date DATE,
  event_type VARCHAR
);

INSERT INTO user_events (id, user_id, event_date, event_type)
VALUES (1, 1, '2022-01-01', 'signup'),
       (2, 1, '2022-01-02', 'login'),
       (3, 2, '2022-01-01', 'signup'),
       (4, 2, '2022-01-03', 'purchase'),
       (5, 3, '2022-01-01', 'signup'),
       (6, 3, '2022-01-02', 'login');
```

**Abfragedemo: Benutzerbindung anhand von Registrierungs-, Anmelde- und Kaufereignissen berechnen**
```sql
SELECT
  user_id,
  RETENTION(event_type = 'signup', event_type = 'login', event_type = 'purchase') AS retention
FROM user_events
GROUP BY user_id;
```

**Ergebnis**
```sql
| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```
