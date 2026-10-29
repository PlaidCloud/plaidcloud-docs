---
title: CASE (Lakehouse v1)
description: CASE trata a lógica IF/THEN.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/case.md
---

Trata a lógica IF/THEN. É estruturado com pelo menos um par de instruções `WHEN` e `THEN`. Toda instrução `CASE` deve ser concluída com a palavra-chave `END`. A instrução `ELSE` é opcional e oferece uma forma de capturar valores não especificados explicitamente nas instruções `WHEN` e `THEN`.

## Sintaxe SQL

```python
case(
    (<condition_1>, <value_1>),
    (<condition_2>, <value_2>),
    [ ... ]
    [ else_=<value_n>]
)
```

## Exemplos do Analyze

### Um Exemplo Simples
Este exemplo retorna o nome de uma pessoa. Ele começa verificando se a coluna de primeiro nome tem um valor (o "if"). Se houver um valor, concatena o primeiro nome com o sobrenome e o retorna (o "then"). Se não houver primeiro nome, retorna somente o sobrenome (o "else").

```python
case(
    (table.first_name.is_not(None), func.concat(table.first_name, table.last_name)), 
    else_=table.last_name
)
```

### Um Exemplo Mais Complexo com Várias Condições
Este exemplo retorna um preço com base na quantidade. "If" a quantidade no pedido for maior que 100, dá ao cliente o preço especial. Se a primeira condição não for atendida, passa para a segunda. Se a quantidade for maior que 10 (de 11 a 100), dá ao cliente o preço de atacado. Caso contrário, dá ao cliente o preço normal.

```python
case( 
    (order_table.qty > 100, item_table.specialprice), 
    (order_table.qty > 10, item_table.bulkprice), 
    else_=item_table.regularprice
)
```

Este exemplo retorna a primeira inicial do primeiro nome da pessoa. Se o nome do usuário for wendy, retorna W. Caso contrário, se o nome do usuário for jack, retorna J. Caso contrário, retorna E.

```python
case( 
    (users_table.name == "wendy", "W"), 
    (users_table.name == "jack", "J"), 
    else_='E'
)
```

O exemplo acima também pode ser escrito de forma abreviada:

```python
case(
    {"wendy": "W", "jack": "J"}, 
    value=users_table.name, 
    else_='E' 
)
```

### Outros Exemplos
Neste exemplo, de uma etapa Table:Lookup, atualizamos a coluna "dock_final" quando o valor de table1.dock_final é Null.
```python
case(
    (table1.dock_final == Null, table2.dock_final),
    else_ = table1.dock_final
)
```

Este exemplo é de uma etapa Table:Lookup em que atualizamos a coluna "Marketing Channel" quando "Marketing Channel" em table1 não é 'none' ou quando "Serial Number" contém um '_'.
```python
case(
    (get_column(table1, 'Marketing Channel') != 'none', get_column(table1, 'Marketing Channel')),
    (get_column(table1, 'Serial Number').contains('_'), get_column(table1, 'Marketing Channel')),
    (get_column(table2, 'Marketing Channel').is_not(Null), get_column(table2, 'Marketing Channel')), 
    else_ = 'none'
)
```

## Sintaxe SQL

```sql
CASE
    WHEN <condition_1> THEN <value_1>
  [ WHEN <condition_2> THEN <value_2> ]
  [ ... ]
  [ ELSE <value_n> ]
END AS <column_name>
```

## Exemplos de SQL

Este exemplo categoriza salários de funcionários com uma instrução CASE e apresenta os detalhes com uma coluna atribuída dinamicamente chamada "SalaryCategory":

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
