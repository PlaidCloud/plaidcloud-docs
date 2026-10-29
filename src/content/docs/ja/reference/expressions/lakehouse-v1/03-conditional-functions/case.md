---
title: CASE (Lakehouse v1)
description: CASE — IF/THENのロジックを処理します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/case.md
---

IF/THENのロジックを処理します。少なくとも1組の`WHEN`文と`THEN`文で構成します。すべての`CASE`文は、`END`キーワードで終了する必要があります。`ELSE`文は省略可能で、`WHEN`文と`THEN`文で明示的に指定されていない値を処理できます。

## SQLの構文

```python
case(
    (<condition_1>, <value_1>),
    (<condition_2>, <value_2>),
    [ ... ]
    [ else_=<value_n>]
)
```

## Analyzeの例

### 単純な例
この例では、人物の名前を返します。まず、名の列に値があるかどうかを確認します（「if」）。値がある場合は、名と姓を連結して返します（「then」）。名がない場合は、姓のみを返します（「else」）。

```python
case(
    (table.first_name.is_not(None), func.concat(table.first_name, table.last_name)), 
    else_=table.last_name
)
```

### 複数の条件を使用した、より複雑な例
この例では、数量に応じた価格を返します。注文の数量が100を超える「場合」は、顧客に特別価格を適用します。最初の条件を満たさない場合は、2番目の条件に進みます。数量が10を超える（11～100）場合は、顧客に大口価格を適用します。それ以外の場合は、顧客に通常価格を適用します。

```python
case( 
    (order_table.qty > 100, item_table.specialprice), 
    (order_table.qty > 10, item_table.bulkprice), 
    else_=item_table.regularprice
)
```

この例では、人物の名の頭文字を返します。ユーザー名がwendyの場合はWを返します。それ以外でユーザー名がjackの場合はJを返します。それ以外の場合はEを返します。

```python
case( 
    (users_table.name == "wendy", "W"), 
    (users_table.name == "jack", "J"), 
    else_='E'
)
```

上記は、次のように省略形で記述することもできます。

```python
case(
    {"wendy": "W", "jack": "J"}, 
    value=users_table.name, 
    else_='E' 
)
```

### その他の例
この例は、Table:Lookupステップのもので、table1.dock_finalの値がNullの場合に、「dock_final」列を更新します。
```python
case(
    (table1.dock_final == Null, table2.dock_final),
    else_ = table1.dock_final
)
```

この例は、Table:Lookupステップのもので、table1の「Marketing Channel」が'none'ではない場合、または「Serial Number」に'_'が含まれている場合に、「Marketing Channel」列を更新します。
```python
case(
    (get_column(table1, 'Marketing Channel') != 'none', get_column(table1, 'Marketing Channel')),
    (get_column(table1, 'Serial Number').contains('_'), get_column(table1, 'Marketing Channel')),
    (get_column(table2, 'Marketing Channel').is_not(Null), get_column(table2, 'Marketing Channel')), 
    else_ = 'none'
)
```

## SQLの構文

```sql
CASE
    WHEN <condition_1> THEN <value_1>
  [ WHEN <condition_2> THEN <value_2> ]
  [ ... ]
  [ ELSE <value_n> ]
END AS <column_name>
```

## SQLの例

この例では、CASE文を使用して従業員の給与を分類し、動的に割り当てた「SalaryCategory」という名前の列とともに詳細を表示します。

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
