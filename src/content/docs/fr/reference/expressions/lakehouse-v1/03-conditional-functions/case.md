---
title: CASE (Lakehouse v1)
description: "CASE : gère la logique SI/ALORS."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/case.md
---

Gère la logique SI/ALORS. Il est structuré avec au moins une paire d'instructions `WHEN` et `THEN`. Chaque instruction `CASE` doit se terminer par le mot-clé `END`. L'instruction `ELSE` est facultative : elle permet de capturer les valeurs non explicitement spécifiées dans les instructions `WHEN` et `THEN`.

## Syntaxe SQL

```python
case(
    (<condition_1>, <value_1>),
    (<condition_2>, <value_2>),
    [ ... ]
    [ else_=<value_n>]
)
```

## Exemples Analyze

### Un exemple simple
Cet exemple renvoie le nom d'une personne. Il commence par vérifier si la colonne du prénom contient une valeur (le « si »). S'il y a une valeur, il concatène le prénom avec le nom de famille et le renvoie (le « alors »). S'il n'y a pas de prénom, il renvoie uniquement le nom de famille (le « sinon »).

```python
case(
    (table.first_name.is_not(None), func.concat(table.first_name, table.last_name)), 
    else_=table.last_name
)
```

### Un exemple plus complexe avec plusieurs conditions
Cet exemple renvoie un prix en fonction de la quantité. « Si » la quantité de la commande est supérieure à 100, le client bénéficie du prix spécial. Si la première condition n'est pas satisfaite, on passe à la seconde. Si la quantité est supérieure à 10 (de 11 à 100), le client bénéficie du prix de gros. Sinon, le client bénéficie du prix normal.

```python
case( 
    (order_table.qty > 100, item_table.specialprice), 
    (order_table.qty > 10, item_table.bulkprice), 
    else_=item_table.regularprice
)
```

Cet exemple renvoie l'initiale du prénom de la personne. Si le nom de l'utilisateur est wendy, il renvoie W. Sinon, si le nom de l'utilisateur est jack, il renvoie J. Sinon, il renvoie E.

```python
case( 
    (users_table.name == "wendy", "W"), 
    (users_table.name == "jack", "J"), 
    else_='E'
)
```

Ce qui précède peut aussi s'écrire sous forme abrégée :

```python
case(
    {"wendy": "W", "jack": "J"}, 
    value=users_table.name, 
    else_='E' 
)
```

### Autres exemples
Dans cet exemple, issu d'une étape Table:Lookup, nous mettons à jour la colonne « dock_final » lorsque la valeur de table1.dock_final est Null.
```python
case(
    (table1.dock_final == Null, table2.dock_final),
    else_ = table1.dock_final
)
```

Cet exemple est issu d'une étape Table:Lookup où nous mettons à jour la colonne « Marketing Channel » lorsque « Marketing Channel » dans table1 n'est pas 'none' ou que le « Serial Number » contient un '_'.
```python
case(
    (get_column(table1, 'Marketing Channel') != 'none', get_column(table1, 'Marketing Channel')),
    (get_column(table1, 'Serial Number').contains('_'), get_column(table1, 'Marketing Channel')),
    (get_column(table2, 'Marketing Channel').is_not(Null), get_column(table2, 'Marketing Channel')), 
    else_ = 'none'
)
```

## Syntaxe SQL

```sql
CASE
    WHEN <condition_1> THEN <value_1>
  [ WHEN <condition_2> THEN <value_2> ]
  [ ... ]
  [ ELSE <value_n> ]
END AS <column_name>
```

## Exemples SQL

Cet exemple classe les salaires des employés à l'aide d'une instruction CASE et présente le détail avec une colonne attribuée dynamiquement, nommée « SalaryCategory » :

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
