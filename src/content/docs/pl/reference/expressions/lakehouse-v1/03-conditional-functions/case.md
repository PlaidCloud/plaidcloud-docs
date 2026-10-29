---
title: CASE (Lakehouse v1)
description: CASE — obsługuje logikę JEŻELI/WTEDY.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/case.md
---

Obsługuje logikę JEŻELI/WTEDY. Składa się z co najmniej jednej pary instrukcji `WHEN` i `THEN`. Każda instrukcja `CASE` musi być zakończona słowem kluczowym `END`. Instrukcja `ELSE` jest opcjonalna i pozwala obsłużyć wartości, które nie zostały jawnie określone w instrukcjach `WHEN` i `THEN`.

## Składnia SQL

```python
case(
    (<condition_1>, <value_1>),
    (<condition_2>, <value_2>),
    [ ... ]
    [ else_=<value_n>]
)
```

## Przykłady Analyze

### Prosty przykład
Ten przykład zwraca nazwisko osoby. Najpierw sprawdza, czy kolumna z imieniem ma wartość („jeżeli”). Jeśli wartość istnieje, łączy imię z nazwiskiem i zwraca wynik („wtedy”). Jeśli imienia nie ma, zwraca samo nazwisko („w przeciwnym razie”).

```python
case(
    (table.first_name.is_not(None), func.concat(table.first_name, table.last_name)), 
    else_=table.last_name
)
```

### Bardziej złożony przykład z wieloma warunkami
Ten przykład zwraca cenę zależną od ilości. „Jeżeli” ilość w zamówieniu jest większa niż 100, klient otrzymuje cenę specjalną. Jeśli pierwszy warunek nie jest spełniony, sprawdzany jest drugi. Jeśli ilość jest większa niż 10 (11–100), klient otrzymuje cenę hurtową. W przeciwnym razie klient otrzymuje cenę regularną.

```python
case( 
    (order_table.qty > 100, item_table.specialprice), 
    (order_table.qty > 10, item_table.bulkprice), 
    else_=item_table.regularprice
)
```

Ten przykład zwraca pierwszą literę imienia osoby. Jeśli użytkownik ma na imię wendy, zwraca W. W przeciwnym razie, jeśli ma na imię jack, zwraca J. W pozostałych przypadkach zwraca E.

```python
case( 
    (users_table.name == "wendy", "W"), 
    (users_table.name == "jack", "J"), 
    else_='E'
)
```

Powyższy zapis można również skrócić do postaci:

```python
case(
    {"wendy": "W", "jack": "J"}, 
    value=users_table.name, 
    else_='E' 
)
```

### Inne przykłady
Ten przykład pochodzi z kroku Table Lookup, w którym aktualizujemy kolumnę „dock_final”, gdy wartość table1.dock_final jest równa Null.
```python
case(
    (table1.dock_final == Null, table2.dock_final),
    else_ = table1.dock_final
)
```

Ten przykład pochodzi z kroku Table Lookup, w którym aktualizujemy kolumnę „Marketing Channel”, gdy „Marketing Channel” w table1 jest inne niż 'none' lub „Serial Number” zawiera znak '_'.
```python
case(
    (get_column(table1, 'Marketing Channel') != 'none', get_column(table1, 'Marketing Channel')),
    (get_column(table1, 'Serial Number').contains('_'), get_column(table1, 'Marketing Channel')),
    (get_column(table2, 'Marketing Channel').is_not(Null), get_column(table2, 'Marketing Channel')), 
    else_ = 'none'
)
```

## Składnia SQL

```sql
CASE
    WHEN <condition_1> THEN <value_1>
  [ WHEN <condition_2> THEN <value_2> ]
  [ ... ]
  [ ELSE <value_n> ]
END AS <column_name>
```

## Przykłady SQL

Ten przykład kategoryzuje wynagrodzenia pracowników za pomocą instrukcji CASE i przedstawia szczegóły z dynamicznie przypisaną kolumną o nazwie „SalaryCategory”:

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
