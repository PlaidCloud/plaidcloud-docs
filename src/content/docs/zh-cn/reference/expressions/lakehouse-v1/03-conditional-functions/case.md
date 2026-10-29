---
title: CASE (Lakehouse v1)
description: CASE：处理 IF/THEN 逻辑。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/case.md
---

处理 IF/THEN 逻辑。它至少由一对 `WHEN` 和 `THEN` 语句构成。每个 `CASE` 语句都必须以 `END` 关键字结束。`ELSE` 语句是可选的，用于捕获 `WHEN` 和 `THEN` 语句中未明确指定的值。

## SQL 语法

```python
case(
    (<condition_1>, <value_1>),
    (<condition_2>, <value_2>),
    [ ... ]
    [ else_=<value_n>]
)
```

## Analyze 示例

### 简单示例
此示例返回一个人的姓名。它首先检查名字列是否有值（“if”）。如果有值，则将名字与姓氏拼接后返回（“then”）。如果没有名字，则只返回姓氏（“else”）。

```python
case(
    (table.first_name.is_not(None), func.concat(table.first_name, table.last_name)), 
    else_=table.last_name
)
```

### 包含多个条件的较复杂示例
此示例根据数量返回价格。“如果”订单中的数量超过 100，则给予客户特价。如果不满足第一个条件，则检查第二个条件。如果数量大于 10（11-100），则给予客户批量价格。否则给予客户常规价格。

```python
case( 
    (order_table.qty > 100, item_table.specialprice), 
    (order_table.qty > 10, item_table.bulkprice), 
    else_=item_table.regularprice
)
```

此示例返回此人名字的首字母。如果用户名为 wendy，则返回 W。否则，如果用户名为 jack，则返回 J。否则返回 E。

```python
case( 
    (users_table.name == "wendy", "W"), 
    (users_table.name == "jack", "J"), 
    else_='E'
)
```

以上写法也可以简写为：

```python
case(
    {"wendy": "W", "jack": "J"}, 
    value=users_table.name, 
    else_='E' 
)
```

### 其他示例
此示例来自 Table Lookup 步骤，当 table1.dock_final 的值为 Null 时，更新“dock_final”列。
```python
case(
    (table1.dock_final == Null, table2.dock_final),
    else_ = table1.dock_final
)
```

此示例来自 Table Lookup 步骤，当 table1 中的“Marketing Channel”不是 'none'，或“Serial Number”包含 '_' 时，更新“Marketing Channel”列。
```python
case(
    (get_column(table1, 'Marketing Channel') != 'none', get_column(table1, 'Marketing Channel')),
    (get_column(table1, 'Serial Number').contains('_'), get_column(table1, 'Marketing Channel')),
    (get_column(table2, 'Marketing Channel').is_not(Null), get_column(table2, 'Marketing Channel')), 
    else_ = 'none'
)
```

## SQL 语法

```sql
CASE
    WHEN <condition_1> THEN <value_1>
  [ WHEN <condition_2> THEN <value_2> ]
  [ ... ]
  [ ELSE <value_n> ]
END AS <column_name>
```

## SQL 示例

此示例使用 CASE 语句对员工薪资进行分类，并通过动态分配的名为“SalaryCategory”的列展示详细信息：

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
