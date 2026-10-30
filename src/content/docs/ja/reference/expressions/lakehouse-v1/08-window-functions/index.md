---
title: ウィンドウ関数 (Lakehouse v1)
description: "Lakehouse v1 の SQL ウィンドウ関数: 行のウィンドウに対して計算します — 順位付け、累計、先行値、後続値。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/index.md
---

## 概要 

ウィンドウ関数は、関連する行のグループ（「ウィンドウ」）に対して動作します。

入力の各行に対して、ウィンドウ関数は 1 行を出力します。出力は、関数に渡された特定の行と、ウィンドウ内の他の行の値に依存します。

順序に依存するウィンドウ関数には、主に次の 2 種類があります。

* `Rank-related functions`: 順位関連の関数は、行の「順位」に基づいて情報を一覧にします。たとえば、年間利益の降順で店舗に順位を付けると、最も利益の大きい店舗が 1 位、2 番目に利益の大きい店舗が 2 位、というようになります。

* `Window frame functions`: ウィンドウフレーム関数を使用すると、ウィンドウ内の行のサブセットに対して、累計や移動平均の計算などのローリング演算を実行できます。

## ウィンドウをサポートする関数の一覧

次の表に、すべてのウィンドウ関数を示します。

| 関数名                                                         | カテゴリー     | ウィンドウ | ウィンドウフレーム | 備考 |
|-----------------------------------------------------------------------|--------------|--------|--------------|-------|
| [ARRAY_AGG](../07-aggregate-functions/aggregate-array-agg)            | 汎用      | ✔      |              |       |
| [AVG](../07-aggregate-functions/aggregate-avg)                        | 汎用      | ✔      | ✔            |       |
| [AVG_IF](../07-aggregate-functions/aggregate-avg-if)                  | 汎用      | ✔      | ✔            |       |
| [COUNT](../07-aggregate-functions/aggregate-count)                    | 汎用      | ✔      | ✔            |       |
| [COUNT_IF](../07-aggregate-functions/aggregate-count-if)              | 汎用      | ✔      | ✔            |       |
| [COVAR_POP](../07-aggregate-functions/aggregate-covar-pop)            | 汎用      | ✔      |              |       |
| [COVAR_SAMP](../07-aggregate-functions/aggregate-covar-samp)          | 汎用      | ✔      |              |       |
| [MAX](../07-aggregate-functions/aggregate-max)                        | 汎用      | ✔      | ✔            |       |
| [MAX_IF](../07-aggregate-functions/aggregate-max-if)                  | 汎用      | ✔      | ✔            |       |
| [MIN](../07-aggregate-functions/aggregate-min)                        | 汎用      | ✔      | ✔            |       |
| [MIN_IF](../07-aggregate-functions/aggregate-min-if)                  | 汎用      | ✔      | ✔            |       |
| [STDDEV_POP](../07-aggregate-functions/aggregate-stddev-pop)          | 汎用      | ✔      | ✔            |       |
| [STDDEV_SAMP](../07-aggregate-functions/aggregate-stddev-samp)        | 汎用      | ✔      | ✔            |       |
| [MEDIAN](../07-aggregate-functions/aggregate-median)                  | 汎用      | ✔      | ✔            |       |
| [QUANTILE_CONT](../07-aggregate-functions/aggregate-quantile-cont)    | 汎用      | ✔      | ✔            |       |
| [QUANTILE_DISC](../07-aggregate-functions/aggregate-quantile-disc)    | 汎用      | ✔      | ✔            |       |
| [KURTOSIS](../07-aggregate-functions/aggregate-kurtosis)              | 汎用      | ✔      | ✔            |       |
| [SKEWNESS](../07-aggregate-functions/aggregate-skewness)              | 汎用      | ✔      | ✔            |       |
| [SUM](../07-aggregate-functions/aggregate-sum)                        | 汎用      | ✔      | ✔            |       |
| [SUM_IF](../07-aggregate-functions/aggregate-sum-if)                  | 汎用      | ✔      | ✔            |       |
| [CUME_DIST](cume-dist)                                                | 順位関連 | ✔      |              |       |
| [PERCENT_RANK](percent-rank/)                                         | 順位関連 | ✔      | ✔            |       |
| [DENSE_RANK](dense-rank)                                              | 順位関連 | ✔      | ✔            |       |
| [RANK](rank)                                                          | 順位関連 | ✔      | ✔            |       |
| [ROW_NUMBER](row-number)                                              | 順位関連 | ✔      |              |       |
| [NTILE](ntile)                                                        | 順位関連 | ✔      |              |       |
| [FIRST_VALUE](first-value)                                            | 順位関連  | ✔     | ✔            |       |
| [FIRST](first)                                                        | 順位関連 | ✔     | ✔            |       |
| [LAST_VALUE](last-value)                                              | 順位関連 | ✔     | ✔            |       |
| [LAST](last)                                                          | 順位関連 | ✔     | ✔            |       |
| [NTH_VALUE](nth-value)                                                | 順位関連 | ✔     | ✔            |       |
| [LEAD](lead)                                                          | 順位関連 | ✔     |              |       |
| [LAG](lag)                                                            | 順位関連 | ✔     |              |       |

## ウィンドウの構文

```sql
<function> ( [ <arguments> ] ) OVER ( { named window | inline window } )

named window ::=
    { window_name | ( window_name ) }

inline window ::=
    [ PARTITION BY <expression_list> ]
    [ ORDER BY <expression_list> ]
    [ window frame ]
```
`named window` は、`SELECT` 文の `WINDOW` 句で定義されるウィンドウです。例: `SELECT a, SUM(a) OVER w FROM t WINDOW w AS ( inline window )`。

`<function>` には、（[集計関数](../07-aggregate-functions)、順位関数、値関数）のいずれかを指定します。

`OVER` 句は、その関数がウィンドウ関数として使用されることを指定します。

`PARTITION BY` サブ句を使用すると、行を市区町村別や年別などのサブグループにグループ化できます。`PARTITION BY` 句はオプションです。行のグループ全体を、サブグループに分割せずに分析することもできます。

`ORDER BY` 句は、ウィンドウ内の行を並べ替えます。

`window frame` 句は、ウィンドウフレームの種類とウィンドウフレームの範囲を指定します。`window frame` 句はオプションです。`window frame` 句を省略すると、デフォルトのウィンドウフレームの種類は `RANGE`、デフォルトのウィンドウフレームの範囲は `UNBOUNDED PRECEDING AND CURRENT ROW` になります。


## ウィンドウフレームの構文

`window frame` には、次のいずれかの種類を指定できます。

```sql
cumulativeFrame ::=
    {
       { ROWS | RANGE } BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
     | { ROWS | RANGE } BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING
    }
```

```sql
slidingFrame ::=
    {
       ROWS BETWEEN <N> { PRECEDING | FOLLOWING } AND <N> { PRECEDING | FOLLOWING }
     | ROWS BETWEEN UNBOUNDED PRECEDING AND <N> { PRECEDING | FOLLOWING }
     | ROWS BETWEEN <N> { PRECEDING | FOLLOWING } AND UNBOUNDED FOLLOWING
    }
```


## SQLの例

**テーブルを作成する**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**データを挿入する**
```sql
INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 75000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 90000),
  (4, 'Sara', 'Williams', 'Sales', 60000),
  (5, 'Tom', 'Brown', 'HR', 82000),
  (6, 'Ava', 'Davis', 'Sales', 62000),
  (7, 'Olivia', 'Taylor', 'IT', 72000),
  (8, 'Emily', 'Anderson', 'HR', 77000),
  (9, 'Sophia', 'Lee', 'Sales', 58000),
  (10, 'Ella', 'Thomas', 'IT', 67000);
```

**例 1: 給与で従業員に順位を付ける**

この例では、RANK() 関数を使用して、給与の降順で従業員に順位を付けます。最も高い給与が 1 位になり、最も低い給与が最大の順位番号になります。
```sql
SELECT employee_id, first_name, last_name, department, salary, RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```

結果:

| employee_id | first_name | last_name | department | salary | rank |
|-------------|------------|-----------|------------|--------|------|
| 3           | Mike       | Johnson   | IT         | 90000  | 1    |
| 2           | Jane       | Smith     | HR         | 85000  | 2    |
| 5           | Tom        | Brown     | HR         | 82000  | 3    |
| 8           | Emily      | Anderson  | HR         | 77000  | 4    |
| 1           | John       | Doe       | IT         | 75000  | 5    |
| 7           | Olivia     | Taylor    | IT         | 72000  | 6    |
| 10          | Ella       | Thomas    | IT         | 67000  | 7    |
| 6           | Ava        | Davis     | Sales      | 62000  | 8    |
| 4           | Sara       | Williams  | Sales      | 60000  | 9    |
| 9           | Sophia     | Lee       | Sales      | 58000  | 10   |



**例 2: 部門ごとの給与合計を計算する**

この例では、SUM() 関数を PARTITION BY とともに使用して、部門ごとに支払われる給与の合計を計算します。各行には、部門とその部門の給与合計が表示されます。
```sql
SELECT department, SUM(salary) OVER (PARTITION BY department) AS total_salary
FROM employees;
```

結果:

| department | total_salary |
|------------|--------------|
| HR         | 244000       |
| HR         | 244000       |
| HR         | 244000       |
| IT         | 304000       |
| IT         | 304000       |
| IT         | 304000       |
| IT         | 304000       |
| Sales      | 180000       |
| Sales      | 180000       |
| Sales      | 180000       |


**例 3: 部門ごとの給与の累計を計算する**

この例では、SUM() 関数を累積ウィンドウフレームとともに使用して、各部門内の給与の累計を計算します。累計は、employee_id 順に並べた従業員の給与に基づいて計算されます。
```sql
SELECT employee_id, first_name, last_name, department, salary, 
       SUM(salary) OVER (PARTITION BY department ORDER BY employee_id
                         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM employees;
```

結果:

| employee_id | first_name | last_name | department | salary | running_total |
|-------------|------------|-----------|------------|--------|---------------|
| 2           | Jane       | Smith     | HR         | 85000  | 85000         |
| 5           | Tom        | Brown     | HR         | 82000  | 167000        |
| 8           | Emily      | Anderson  | HR         | 77000  | 244000        |
| 1           | John       | Doe       | IT         | 75000  | 75000         |
| 3           | Mike       | Johnson   | IT         | 90000  | 165000        |
| 7           | Olivia     | Taylor    | IT         | 72000  | 237000        |
| 10          | Ella       | Thomas    | IT         | 67000  | 304000        |
| 4           | Sara       | Williams  | Sales      | 60000  | 60000         |
| 6           | Ava        | Davis     | Sales      | 62000  | 122000        |
| 9           | Sophia     | Lee       | Sales      | 58000  | 180000        |
