---
title: UNNEST (Lakehouse v1)
description: UNNEST – löst das Array auf und gibt die Menge der Elemente zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/unnest.md
---

Löst das Array auf und gibt die Menge der Elemente zurück.

## Analyze-Syntax

```python
func.unnest( <array> )
```

## Analyze-Beispiele

```python
func.unnest([1, 2])

┌──────────────────────┐
│  func.unnest([1, 2]) │
├──────────────────────┤
│                    1 │
│                    2 │
└──────────────────────┘
```

## SQL-Syntax

```sql
UNNEST( <array> )
```

## SQL-Beispiele

```sql
SELECT UNNEST([1, 2]);

┌─────────────────┐
│  unnest([1, 2]) │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘

-- UNNEST(array) can be used as a table function.
SELECT * FROM UNNEST([1, 2]);

┌─────────────────┐
│      value      │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘
```

## Ein praktisches Beispiel
In den folgenden Beispielen verwenden wir die Tabelle contacts, deren Spalte phones als Array von Text definiert ist.

```python
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (100), 
  phones TEXT []
);
```

Die Spalte phones ist ein eindimensionales Array, das verschiedene Telefonnummern enthält, die ein Kontakt haben kann.

Um ein mehrdimensionales Array zu definieren, fügen Sie die eckigen Klammern hinzu.

Beispielsweise können Sie ein zweidimensionales Array wie folgt definieren:

```python
column_name data_type [][]
```

Ein Beispiel für das Einfügen von Daten in diese Tabelle
```python
INSERT INTO contacts (name, phones)
VALUES('John Doe',ARRAY [ '(408)-589-5846','(408)-589-5555' ]);
```
oder
```python
INSERT INTO contacts (name, phones)
VALUES('Lily Bush','{"(408)-589-5841"}'),
      ('William Gate','{"(408)-589-5842","(408)-589-5843"}');
```

Die Funktion unnest() erweitert ein Array zu einer Liste von Zeilen. Die folgende Abfrage erweitert beispielsweise alle Telefonnummern des Arrays phones.

```python
SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;
```

Ausgabe:
|     name     |     unnest     |
|--------------|----------------|
| John Doe     | (408)-589-5846 |
| John Doe     | (408)-589-5555 |
| Lily Bush    | (408)-589-5841 |
| William Gate | (408)-589-5843 |
