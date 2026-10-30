---
title: CASE (Lakehouse v1)
description: CASE – verarbeitet WENN/DANN-Logik (IF/THEN).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/case.md
---

Verarbeitet WENN/DANN-Logik (IF/THEN). Sie besteht aus mindestens einem Paar aus `WHEN`- und `THEN`-Anweisungen. Jede `CASE`-Anweisung muss mit dem Schlüsselwort `END` abgeschlossen werden. Die `ELSE`-Anweisung ist optional und bietet eine Möglichkeit, Werte zu erfassen, die in den `WHEN`- und `THEN`-Anweisungen nicht ausdrücklich angegeben sind.

## SQL-Syntax

```python
case(
    (<condition_1>, <value_1>),
    (<condition_2>, <value_2>),
    [ ... ]
    [ else_=<value_n>]
)
```

## Analyze-Beispiele

### Ein einfaches Beispiel
Dieses Beispiel gibt den Namen einer Person zurück. Zuerst wird geprüft, ob die Spalte für den Vornamen einen Wert enthält (das „Wenn“). Ist ein Wert vorhanden, werden Vorname und Nachname verkettet und zurückgegeben (das „Dann“). Ist kein Vorname vorhanden, wird nur der Nachname zurückgegeben (das „Sonst“).

```python
case(
    (table.first_name.is_not(None), func.concat(table.first_name, table.last_name)), 
    else_=table.last_name
)
```

### Ein komplexeres Beispiel mit mehreren Bedingungen
Dieses Beispiel gibt einen Preis abhängig von der Menge zurück. „Wenn“ die Menge in der Bestellung größer als 100 ist, erhält der Kunde den Sonderpreis. Wird die erste Bedingung nicht erfüllt, geht es mit der zweiten weiter. Ist die Menge größer als 10 (11–100), erhält der Kunde den Mengenpreis. Andernfalls erhält der Kunde den Normalpreis.

```python
case( 
    (order_table.qty > 100, item_table.specialprice), 
    (order_table.qty > 10, item_table.bulkprice), 
    else_=item_table.regularprice
)
```

Dieses Beispiel gibt den Anfangsbuchstaben des Vornamens einer Person zurück. Lautet der Name des Benutzers wendy, wird W zurückgegeben. Lautet der Name des Benutzers jack, wird J zurückgegeben. Andernfalls wird E zurückgegeben.

```python
case( 
    (users_table.name == "wendy", "W"), 
    (users_table.name == "jack", "J"), 
    else_='E'
)
```

Das Obige lässt sich auch in Kurzschreibweise formulieren:

```python
case(
    {"wendy": "W", "jack": "J"}, 
    value=users_table.name, 
    else_='E' 
)
```

### Weitere Beispiele
Dieses Beispiel stammt aus einem Table:Lookup-Schritt, in dem wir die Spalte „dock_final“ aktualisieren, wenn der Wert table1.dock_final Null ist.
```python
case(
    (table1.dock_final == Null, table2.dock_final),
    else_ = table1.dock_final
)
```

Dieses Beispiel stammt aus einem Table:Lookup-Schritt, in dem wir die Spalte „Marketing Channel“ aktualisieren, wenn „Marketing Channel“ in table1 nicht 'none' ist oder „Serial Number“ ein '_' enthält.
```python
case(
    (get_column(table1, 'Marketing Channel') != 'none', get_column(table1, 'Marketing Channel')),
    (get_column(table1, 'Serial Number').contains('_'), get_column(table1, 'Marketing Channel')),
    (get_column(table2, 'Marketing Channel').is_not(Null), get_column(table2, 'Marketing Channel')), 
    else_ = 'none'
)
```

## SQL-Syntax

```sql
CASE
    WHEN <condition_1> THEN <value_1>
  [ WHEN <condition_2> THEN <value_2> ]
  [ ... ]
  [ ELSE <value_n> ]
END AS <column_name>
```

## SQL-Beispiele

Dieses Beispiel kategorisiert Mitarbeitergehälter mit einer CASE-Anweisung und stellt die Details mit einer dynamisch zugewiesenen Spalte namens „SalaryCategory“ dar:

```sql
-- Create a sample table
CREATE TABLE Employee (
    EmployeeID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary INT
);

-- Insert some sample data
INSERT INTO Employee VALUES (1, 'John', 'Doe', 50000);
INSERT INTO Employee VALUES (2, 'Jane', 'Smith', 60000);
INSERT INTO Employee VALUES (3, 'Bob', 'Johnson', 75000);
INSERT INTO Employee VALUES (4, 'Alice', 'Williams', 90000);

-- Add a new column 'SalaryCategory' using CASE statement
-- Categorize employees based on their salary
SELECT
    EmployeeID,
    FirstName,
    LastName,
    Salary,
    CASE
        WHEN Salary < 60000 THEN 'Low'
        WHEN Salary >= 60000 AND Salary < 80000 THEN 'Medium'
        WHEN Salary >= 80000 THEN 'High'
        ELSE 'Unknown'
    END AS SalaryCategory
FROM
    Employee;

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│    employeeid   │     firstname    │     lastname     │      salary     │ salarycategory │
├─────────────────┼──────────────────┼──────────────────┼─────────────────┼────────────────┤
│               1 │ John             │ Doe              │           50000 │ Low            │
│               2 │ Jane             │ Smith            │           60000 │ Medium         │
│               4 │ Alice            │ Williams         │           90000 │ High           │
│               3 │ Bob              │ Johnson          │           75000 │ Medium         │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```
