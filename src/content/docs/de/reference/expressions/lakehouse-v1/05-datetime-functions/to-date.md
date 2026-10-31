---
title: TO_DATE (Lakehouse v1)
description: TO_DATE – wandelt einen Ausdruck in ein Datum um, einschließlich folgender Fälle.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-date.md
---

Wandelt einen Ausdruck in ein Datum um, unter anderem durch:

- **Umwandeln einer Zeichenfolge im Zeitstempelformat in ein Datum**: Extrahiert ein Datum aus der angegebenen Zeichenfolge.

- **Umwandeln einer Ganzzahl in ein Datum**: Interpretiert die Ganzzahl als Anzahl der Tage vor (bei negativen Zahlen) oder nach (bei positiven Zahlen) der Unix-Epoche (Mitternacht am 1. Januar 1970). Bitte beachten Sie, dass ein Datumswert von `1000-01-01` bis `9999-12-31` reicht. PlaidCloud Lakehouse gibt einen Fehler zurück, wenn Sie "SELECT TO_DATE(9999999999999999999)" ausführen.

- **Umwandeln einer Zeichenfolge in ein Datum mit dem angegebenen Format**: Die Funktion nimmt zwei Argumente entgegen und wandelt die erste Zeichenfolge anhand des in der zweiten Zeichenfolge angegebenen Formats in ein Datum um. Um das Datums- und Zeitformat in PlaidCloud Lakehouse anzupassen, können Spezifizierer verwendet werden. Eine vollständige Liste der unterstützten Spezifizierer finden Sie unter Formatierung von Datum und Uhrzeit.

Datumsformate werden mit der `strftime`-Spezifikation angegeben.  Siehe die [Kurzreferenz](https://devhints.io/strftime).

Siehe auch: [TO_TIMESTAMP](../to-timestamp)

## Strftime-Parameter

### Kurzreferenz

#### Datum

| Beispiel        | Ausgabe                |
| ---             | ---                    |
| `%m/%d/%Y`      | `06/05/2013`           |
| `%A, %B %e, %Y` | `Sunday, June 5, 2013` |
| `%b %e %a`      | `Jun 5 Sun`            |

#### Uhrzeit

| Beispiel        | Ausgabe                |
| ---             | ---                    |
| `%H:%M`         | `23:05`                |
| `%I:%M %p`      | `11:05 PM`             |


### Datum

| Symbol | Beispiel                 | Bereich        |
| ---    | ---                      | ---            |
| `%a`   | `Sun`                    | **Wochentag**  |
| `%A`   | `Sunday`                 |                |
| `%w`   | `0`..`6` _(Sonntag ist 0)_ |              |
| ---    | ---                      | ---            |
| `%y`   | `13`                     | **Jahr**       |
| `%Y`   | `2013`                   |                |
| ---    | ---                      | ---            |
| `%b`   | `Jan`                    | **Monat**      |
| `%B`   | `January`                |                |
| `%m`   | `01`..`12`               |                |
| ---    | ---                      | ---            |
| `%d`   | `01`..`31`               | **Tag**        |
| `%e`   | `1`..`31`                |                |


### Uhrzeit

| Symbol | Beispiel     | Bereich                |
| ---    | ---          | ---                    |
| `%l`   | `1`          | Stunde                 |
| `%H`   | `00`..`23`   | Stunde (24 h)          |
| `%I`   | `01`..`12`   | Stunde (12 h)          |
| --     | ---          | ---                    |
| `%M`   | `00`..`59`   | Minute                 |
| `%S`   | `00`..`60`   | Sekunde                |
| ---    | ---          | ---                    |
| `%p`   | `AM`         | AM oder PM             |
| `%Z`   | `+08`        | Zeitzone               |
| ---    | ---          | ---                    |
| `%j`   | `001`..`366` | Tag des Jahres         |
| `%%`   | `%`          | Literales Zeichen %    |


## Analyze-Syntax

```python
func.to_date('<timestamp_expr>')
func.to_date(<integer>)
func.to_date('<string>', '<format>')
```

## Analyze-Beispiele

```python
func.typeof(func.to_date('2022-01-02')), func.typeof(func.str_to_date('2022-01-02'))

┌───────────────────────────────────────────────────────────────────────────────────────┐
│ func.typeof(func.to_date('2022-01-02')) │ func.typeof(func.str_to_date('2022-01-02')) │
├─────────────────────────────────────────┼─────────────────────────────────────────────┤
│ DATE                                    │ DATE                                        │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
-- Convert a timestamp-format string
TO_DATE('<timestamp_expr>')

-- Convert an integer
TO_DATE(<integer>)

-- Convert a string using the given format
TO_DATE('<string>', '<format>')
```

## Aliase

- [DATE](../date)
- [STR_TO_DATE](../str-to-date)

## Rückgabetyp

Die Funktion gibt ein Datum im Format "YYYY-MM-DD" zurück:

```sql
SELECT TYPEOF(TO_DATE('2022-01-02')), TYPEOF(STR_TO_DATE('2022-01-02'));

┌───────────────────────────────────────────────────────────────────┐
│ typeof(to_date('2022-01-02')) │ typeof(str_to_date('2022-01-02')) │
├───────────────────────────────┼───────────────────────────────────┤
│ DATE                          │ DATE                              │
└───────────────────────────────────────────────────────────────────┘
```

Um das zurückgegebene Datum wieder in eine Zeichenfolge umzuwandeln, verwenden Sie die Funktion [DATE_FORMAT](../date-format):

```sql
SELECT DATE_FORMAT(TO_DATE('2022-01-02')) AS dt, TYPEOF(dt);

┌─────────────────────────┐
│     dt     │ typeof(dt) │
├────────────┼────────────┤
│ 2022-01-02 │ VARCHAR    │
└─────────────────────────┘
```

## SQL-Beispiele

### SQL-Beispiele 1: Umwandeln einer Zeichenfolge im Zeitstempelformat

```sql
SELECT TO_DATE('2022-01-02T01:12:00+07:00'), STR_TO_DATE('2022-01-02T01:12:00+07:00');

┌─────────────────────────────────────────────────────────────────────────────────┐
│ to_date('2022-01-02t01:12:00+07:00') │ str_to_date('2022-01-02t01:12:00+07:00') │
├──────────────────────────────────────┼──────────────────────────────────────────┤
│ 2022-01-01                           │ 2022-01-01                               │
└─────────────────────────────────────────────────────────────────────────────────┘

SELECT TO_DATE('2022-01-02'), STR_TO_DATE('2022-01-02');

┌───────────────────────────────────────────────────┐
│ to_date('2022-01-02') │ str_to_date('2022-01-02') │
├───────────────────────┼───────────────────────────┤
│ 2022-01-02            │ 2022-01-02                │
└───────────────────────────────────────────────────┘
```

### SQL-Beispiele 2: Umwandeln einer Ganzzahl

```sql
SELECT TO_DATE(1), STR_TO_DATE(1), TO_DATE(-1), STR_TO_DATE(-1);

┌───────────────────────────────────────────────────────────────────┐
│ to_date(1) │ str_to_date(1) │ to_date((- 1)) │ str_to_date((- 1)) │
│    Date    │      Date      │      Date      │        Date        │
├────────────┼────────────────┼────────────────┼────────────────────┤
│ 1970-01-02 │ 1970-01-02     │ 1969-12-31     │ 1969-12-31         │
└───────────────────────────────────────────────────────────────────┘
```

### SQL-Beispiele 3: Umwandeln einer Zeichenfolge mit dem angegebenen Format

```sql
SELECT TO_DATE('12/25/2022','%m/%d/%Y'), STR_TO_DATE('12/25/2022','%m/%d/%Y');

┌───────────────────────────────────────────────────────────────────────────┐
│ to_date('12/25/2022', '%m/%d/%y') │ str_to_date('12/25/2022', '%m/%d/%y') │
├───────────────────────────────────┼───────────────────────────────────────┤
│ 2022-12-25                        │ 2022-12-25                            │
└───────────────────────────────────────────────────────────────────────────┘
```
