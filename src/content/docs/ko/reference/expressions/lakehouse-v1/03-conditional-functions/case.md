---
title: CASE (Lakehouse v1)
description: CASE — IF/THEN 논리를 처리합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/case.md
---

IF/THEN 논리를 처리합니다. 최소 한 쌍의 `WHEN` 및 `THEN` 문으로 구성되며, 모든 `CASE` 문은 `END` 키워드로 끝나야 합니다. `ELSE` 문은 선택 사항이며, `WHEN` 및 `THEN` 문에 명시적으로 지정되지 않은 값을 처리하는 방법을 제공합니다.

## SQL 구문

```python
case(
    (<condition_1>, <value_1>),
    (<condition_2>, <value_2>),
    [ ... ]
    [ else_=<value_n>]
)
```

## Analyze 예제

### 간단한 예제
이 예제는 사람의 이름을 반환합니다. 먼저 이름 열에 값이 있는지 확인합니다("if"). 값이 있으면 이름과 성을 연결하여 반환하고("then"), 이름이 없으면 성만 반환합니다("else").

```python
case(
    (table.first_name.is_not(None), func.concat(table.first_name, table.last_name)), 
    else_=table.last_name
)
```

### 여러 조건이 있는 더 복잡한 예제
이 예제는 수량에 따라 가격을 반환합니다. 주문 수량이 100을 초과하면("if") 고객에게 특별 가격을 적용합니다. 첫 번째 조건을 충족하지 않으면 두 번째 조건으로 넘어갑니다. 수량이 10을 초과하면(11-100) 고객에게 대량 구매 가격을 적용합니다. 그렇지 않으면 고객에게 일반 가격을 적용합니다.

```python
case( 
    (order_table.qty > 100, item_table.specialprice), 
    (order_table.qty > 10, item_table.bulkprice), 
    else_=item_table.regularprice
)
```

이 예제는 사람 이름의 첫 글자를 반환합니다. 사용자 이름이 wendy이면 W를 반환하고, jack이면 J를 반환하며, 그렇지 않으면 E를 반환합니다.

```python
case( 
    (users_table.name == "wendy", "W"), 
    (users_table.name == "jack", "J"), 
    else_='E'
)
```

위 내용은 다음과 같이 줄여서 쓸 수도 있습니다.

```python
case(
    {"wendy": "W", "jack": "J"}, 
    value=users_table.name, 
    else_='E' 
)
```

### 기타 예제
이 예제는 Table:Lookup 단계에서 가져온 것으로, table1.dock_final 값이 Null일 때 "dock_final" 열을 업데이트합니다.
```python
case(
    (table1.dock_final == Null, table2.dock_final),
    else_ = table1.dock_final
)
```

이 예제는 Table:Lookup 단계에서 가져온 것으로, table1의 "Marketing Channel"이 'none'이 아니거나 "Serial Number"에 '_'가 포함된 경우 "Marketing Channel" 열을 업데이트합니다.
```python
case(
    (get_column(table1, 'Marketing Channel') != 'none', get_column(table1, 'Marketing Channel')),
    (get_column(table1, 'Serial Number').contains('_'), get_column(table1, 'Marketing Channel')),
    (get_column(table2, 'Marketing Channel').is_not(Null), get_column(table2, 'Marketing Channel')), 
    else_ = 'none'
)
```

## SQL 구문

```sql
CASE
    WHEN <condition_1> THEN <value_1>
  [ WHEN <condition_2> THEN <value_2> ]
  [ ... ]
  [ ELSE <value_n> ]
END AS <column_name>
```

## SQL 예제

이 예제는 CASE 문을 사용하여 직원 급여를 분류하고, "SalaryCategory"라는 이름으로 동적으로 지정한 열에 세부 정보를 표시합니다.

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
