---
title: CASE (Lakehouse v1)
description: CASE — gestiona la lógica IF/THEN.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/case.md
---

Gestiona la lógica IF/THEN. Se estructura con al menos un par de instrucciones `WHEN` y `THEN`. Toda instrucción `CASE` debe terminar con la palabra clave `END`. La instrucción `ELSE` es opcional y ofrece una forma de capturar los valores que no se especifican explícitamente en las instrucciones `WHEN` y `THEN`.

## Sintaxis de SQL

```python
case(
    (<condition_1>, <value_1>),
    (<condition_2>, <value_2>),
    [ ... ]
    [ else_=<value_n>]
)
```

## Ejemplos de Analyze

### Un ejemplo sencillo
Este ejemplo devuelve el nombre de una persona. Comienza comprobando si la columna del nombre de pila tiene un valor (el “if”). Si hay un valor, concatena el nombre de pila con el apellido y lo devuelve (el “then”). Si no hay nombre de pila, devuelve solo el apellido (el “else”).

```python
case(
    (table.first_name.is_not(None), func.concat(table.first_name, table.last_name)), 
    else_=table.last_name
)
```

### Un ejemplo más complejo con varias condiciones
Este ejemplo devuelve un precio según la cantidad. “If” la cantidad del pedido es superior a 100, se aplica al cliente el precio especial. Si no cumple la primera condición, se pasa a la segunda. Si la cantidad es superior a 10 (de 11 a 100), se aplica al cliente el precio por volumen. De lo contrario, se aplica al cliente el precio normal.

```python
case( 
    (order_table.qty > 100, item_table.specialprice), 
    (order_table.qty > 10, item_table.bulkprice), 
    else_=item_table.regularprice
)
```

Este ejemplo devuelve la inicial del nombre de pila de la persona. Si el nombre del usuario es wendy, devuelve W. Si el nombre del usuario es jack, devuelve J. En cualquier otro caso, devuelve E.

```python
case( 
    (users_table.name == "wendy", "W"), 
    (users_table.name == "jack", "J"), 
    else_='E'
)
```

Lo anterior también se puede escribir en forma abreviada así:

```python
case(
    {"wendy": "W", "jack": "J"}, 
    value=users_table.name, 
    else_='E' 
)
```

### Otros ejemplos
Este ejemplo procede de un paso Table:Lookup en el que se actualiza la columna “dock_final” cuando el valor de table1.dock_final es Null.
```python
case(
    (table1.dock_final == Null, table2.dock_final),
    else_ = table1.dock_final
)
```

Este ejemplo procede de un paso Table:Lookup en el que se actualiza la columna “Marketing Channel” cuando “Marketing Channel” de table1 no es 'none' o el “Serial Number” contiene un '_'.
```python
case(
    (get_column(table1, 'Marketing Channel') != 'none', get_column(table1, 'Marketing Channel')),
    (get_column(table1, 'Serial Number').contains('_'), get_column(table1, 'Marketing Channel')),
    (get_column(table2, 'Marketing Channel').is_not(Null), get_column(table2, 'Marketing Channel')), 
    else_ = 'none'
)
```

## Sintaxis de SQL

```sql
CASE
    WHEN <condition_1> THEN <value_1>
  [ WHEN <condition_2> THEN <value_2> ]
  [ ... ]
  [ ELSE <value_n> ]
END AS <column_name>
```

## Ejemplos de SQL

Este ejemplo clasifica los salarios de los empleados mediante una instrucción CASE y presenta los detalles con una columna asignada dinámicamente llamada “SalaryCategory”:

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
