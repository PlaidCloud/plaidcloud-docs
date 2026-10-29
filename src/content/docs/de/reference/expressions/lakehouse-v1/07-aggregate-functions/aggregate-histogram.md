---
title: HISTOGRAM (Lakehouse v1)
description: HISTOGRAM – erzeugt ein Histogramm der Datenverteilung mit einer Bucket-Strategie gleicher Höhe.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-histogram.md
---

Erzeugt ein Histogramm der Datenverteilung mit einer Bucket-Strategie „gleicher Höhe“.

## Analyze-Syntax

```python
func.histogram(<expr>)
```

## Analyze-Beispiele
Details finden Sie im SQL-Beispiel.

## SQL-Syntax

```sql
HISTOGRAM(<expr>)

-- The following two forms are equivalent:
HISTOGRAM(<max_num_buckets>)(<expr>)
HISTOGRAM(<expr> [, <max_num_buckets>])
```

| Parameter         | Beschreibung                                                                        |
|-------------------|-------------------------------------------------------------------------------------|
| `expr`            | Der Datentyp von `expr` muss sortierbar sein.                                       |
| `max_num_buckets` | Optionale positive Ganzzahl, die die maximale Anzahl von Buckets angibt. Standard ist 128. |

## Rückgabetyp

Gibt entweder eine leere Zeichenfolge oder ein JSON-Objekt mit der folgenden Struktur zurück:

- **buckets**: Liste von Buckets mit detaillierten Informationen:
  - **lower**: Untergrenze des Buckets.
  - **upper**: Obergrenze des Buckets.
  - **count**: Anzahl der Elemente im Bucket.
  - **pre_sum**: Kumulierte Anzahl der Elemente bis zum aktuellen Bucket.
  - **ndv**: Anzahl der eindeutigen Werte im Bucket.

## SQL-Beispiele

Dieses Beispiel zeigt, wie die Funktion HISTOGRAM die Verteilung der `c_int`-Werte in der Tabelle `histagg` analysiert und Bucket-Grenzen, Anzahlen eindeutiger Werte, Elementanzahlen und kumulierte Anzahlen zurückgibt:

```sql
CREATE TABLE histagg (
  c_id INT,
  c_tinyint TINYINT,
  c_smallint SMALLINT,
  c_int INT
);

INSERT INTO histagg VALUES
  (1, 10, 20, 30),
  (1, 11, 21, 33),
  (1, 11, 12, 13),
  (2, 21, 22, 23),
  (2, 31, 32, 33),
  (2, 10, 20, 30);

SELECT HISTOGRAM(c_int) FROM histagg;

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                              histogram(c_int)                                                                                                             │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [{"lower":"13","upper":"13","ndv":1,"count":1,"pre_sum":0},{"lower":"23","upper":"23","ndv":1,"count":1,"pre_sum":1},{"lower":"30","upper":"30","ndv":1,"count":2,"pre_sum":2},{"lower":"33","upper":"33","ndv":1,"count":2,"pre_sum":4}] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Das Ergebnis wird als JSON-Array zurückgegeben:

```json
[
  {
    "lower": "13",
    "upper": "13",
    "ndv": 1,
    "count": 1,
    "pre_sum": 0
  },
  {
    "lower": "23",
    "upper": "23",
    "ndv": 1,
    "count": 1,
    "pre_sum": 1
  },
  {
    "lower": "30",
    "upper": "30",
    "ndv": 1,
    "count": 2,
    "pre_sum": 2
  },
  {
    "lower": "33",
    "upper": "33",
    "ndv": 1,
    "count": 2,
    "pre_sum": 4
  }
]
```

Dieses Beispiel zeigt, wie `HISTOGRAM(2)` die c_int-Werte in zwei Buckets gruppiert:

```sql
SELECT HISTOGRAM(2)(c_int) FROM histagg;
-- Or
SELECT HISTOGRAM(c_int, 2) FROM histagg;

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                  histogram(2)(c_int)                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [{"lower":"13","upper":"30","ndv":3,"count":4,"pre_sum":0},{"lower":"33","upper":"33","ndv":1,"count":2,"pre_sum":4}] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Das Ergebnis wird als JSON-Array zurückgegeben:

```json
[
  {
    "lower": "13",
    "upper": "30",
    "ndv": 3,
    "count": 4,
    "pre_sum": 0
  },
  {
    "lower": "33",
    "upper": "33",
    "ndv": 1,
    "count": 2,
    "pre_sum": 4
  }
]
```
