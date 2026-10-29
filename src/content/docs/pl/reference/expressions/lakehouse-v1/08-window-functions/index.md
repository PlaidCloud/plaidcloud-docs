---
title: Funkcje okna (Lakehouse v1)
description: "Funkcje okna SQL w Lakehouse v1: obliczenia na oknach wierszy — rankingi, sumy narastające, wyprzedzenia i opóźnienia."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/index.md
---

## Przegląd

Funkcja okna działa na grupie („oknie”) powiązanych wierszy.

Dla każdego wiersza wejściowego funkcja okna zwraca jeden wiersz wyjściowy, który zależy od konkretnego wiersza przekazanego do funkcji oraz od wartości pozostałych wierszy w oknie.

Istnieją dwa główne typy funkcji okna wrażliwych na kolejność:

* `Rank-related functions`: funkcje związane z rangą podają informacje na podstawie „rangi” wiersza. Na przykład przy uszeregowaniu sklepów malejąco według rocznego zysku sklep o największym zysku otrzyma rangę 1, drugi pod względem zysku sklep rangę 2 i tak dalej.

* `Window frame functions`: funkcje ramki okna umożliwiają wykonywanie operacji kroczących, takich jak obliczanie sumy narastającej lub średniej kroczącej, na podzbiorze wierszy w oknie.

## Lista funkcji obsługujących okna

Poniższa lista zawiera wszystkie funkcje okna.

| Nazwa funkcji                                                         | Kategoria    | Okno   | Ramka okna   | Uwagi |
|-----------------------------------------------------------------------|--------------|--------|--------------|-------|
| [ARRAY_AGG](../07-aggregate-functions/aggregate-array-agg)            | Ogólne       | ✔      |              |       |
| [AVG](../07-aggregate-functions/aggregate-avg)                        | Ogólne       | ✔      | ✔            |       |
| [AVG_IF](../07-aggregate-functions/aggregate-avg-if)                  | Ogólne       | ✔      | ✔            |       |
| [COUNT](../07-aggregate-functions/aggregate-count)                    | Ogólne       | ✔      | ✔            |       |
| [COUNT_IF](../07-aggregate-functions/aggregate-count-if)              | Ogólne       | ✔      | ✔            |       |
| [COVAR_POP](../07-aggregate-functions/aggregate-covar-pop)            | Ogólne       | ✔      |              |       |
| [COVAR_SAMP](../07-aggregate-functions/aggregate-covar-samp)          | Ogólne       | ✔      |              |       |
| [MAX](../07-aggregate-functions/aggregate-max)                        | Ogólne       | ✔      | ✔            |       |
| [MAX_IF](../07-aggregate-functions/aggregate-max-if)                  | Ogólne       | ✔      | ✔            |       |
| [MIN](../07-aggregate-functions/aggregate-min)                        | Ogólne       | ✔      | ✔            |       |
| [MIN_IF](../07-aggregate-functions/aggregate-min-if)                  | Ogólne       | ✔      | ✔            |       |
| [STDDEV_POP](../07-aggregate-functions/aggregate-stddev-pop)          | Ogólne       | ✔      | ✔            |       |
| [STDDEV_SAMP](../07-aggregate-functions/aggregate-stddev-samp)        | Ogólne       | ✔      | ✔            |       |
| [MEDIAN](../07-aggregate-functions/aggregate-median)                  | Ogólne       | ✔      | ✔            |       |
| [QUANTILE_CONT](../07-aggregate-functions/aggregate-quantile-cont)    | Ogólne       | ✔      | ✔            |       |
| [QUANTILE_DISC](../07-aggregate-functions/aggregate-quantile-disc)    | Ogólne       | ✔      | ✔            |       |
| [KURTOSIS](../07-aggregate-functions/aggregate-kurtosis)              | Ogólne       | ✔      | ✔            |       |
| [SKEWNESS](../07-aggregate-functions/aggregate-skewness)              | Ogólne       | ✔      | ✔            |       |
| [SUM](../07-aggregate-functions/aggregate-sum)                        | Ogólne       | ✔      | ✔            |       |
| [SUM_IF](../07-aggregate-functions/aggregate-sum-if)                  | Ogólne       | ✔      | ✔            |       |
| [CUME_DIST](cume-dist)                                                | Związane z rangą | ✔  |              |       |
| [PERCENT_RANK](percent-rank/)                                         | Związane z rangą | ✔  | ✔            |       |
| [DENSE_RANK](dense-rank)                                              | Związane z rangą | ✔  | ✔            |       |
| [RANK](rank)                                                          | Związane z rangą | ✔  | ✔            |       |
| [ROW_NUMBER](row-number)                                              | Związane z rangą | ✔  |              |       |
| [NTILE](ntile)                                                        | Związane z rangą | ✔  |              |       |
| [FIRST_VALUE](first-value)                                            | Związane z rangą | ✔  | ✔            |       |
| [FIRST](first)                                                        | Związane z rangą | ✔  | ✔            |       |
| [LAST_VALUE](last-value)                                              | Związane z rangą | ✔  | ✔            |       |
| [LAST](last)                                                          | Związane z rangą | ✔  | ✔            |       |
| [NTH_VALUE](nth-value)                                                | Związane z rangą | ✔  | ✔            |       |
| [LEAD](lead)                                                          | Związane z rangą | ✔  |              |       |
| [LAG](lag)                                                            | Związane z rangą | ✔  |              |       |

## Składnia okna

```sql
<function> ( [ <arguments> ] ) OVER ( { named window | inline window } )

named window ::=
    { window_name | ( window_name ) }

inline window ::=
    [ PARTITION BY <expression_list> ]
    [ ORDER BY <expression_list> ]
    [ window frame ]
```
`named window` to okno zdefiniowane w klauzuli `WINDOW` instrukcji `SELECT`, np.: `SELECT a, SUM(a) OVER w FROM t WINDOW w AS ( inline window )`.

`<function>` to jedna z następujących: ([funkcja agregująca](../07-aggregate-functions), funkcja rankingowa, funkcja wartości).

Klauzula `OVER` określa, że funkcja jest używana jako funkcja okna.

Podklauzula `PARTITION BY` pozwala grupować wiersze w podgrupy, na przykład według miasta, roku itd. Klauzula `PARTITION BY` jest opcjonalna. Można analizować całą grupę wierszy bez dzielenia jej na podgrupy.

Klauzula `ORDER BY` porządkuje wiersze w oknie. 

Klauzula `window frame` określa typ ramki okna i jej zakres. Klauzula `window frame` jest opcjonalna. Jeśli pominiesz klauzulę `window frame`, domyślnym typem ramki okna jest `RANGE`, a domyślnym zakresem ramki okna `UNBOUNDED PRECEDING AND CURRENT ROW`.


## Składnia ramki okna

`window frame` może być jednym z następujących typów:

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


## Przykłady SQL

**Utwórz tabelę**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**Wstaw dane**
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

**Przykład 1: Ranking pracowników według wynagrodzenia**

W tym przykładzie używamy funkcji RANK() do uszeregowania pracowników według wynagrodzenia w kolejności malejącej. Najwyższe wynagrodzenie otrzyma rangę 1, a najniższe — najwyższy numer rangi.
```sql
SELECT employee_id, first_name, last_name, department, salary, RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```

Wynik:

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



**Przykład 2: Obliczanie łącznego wynagrodzenia na dział**

W tym przykładzie używamy funkcji SUM() z PARTITION BY do obliczenia łącznego wynagrodzenia wypłacanego w każdym dziale. Każdy wiersz pokaże dział i łączne wynagrodzenie tego działu.
```sql
SELECT department, SUM(salary) OVER (PARTITION BY department) AS total_salary
FROM employees;
```

Wynik:

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


**Przykład 3: Obliczanie sumy narastającej wynagrodzeń na dział**

W tym przykładzie używamy funkcji SUM() ze skumulowaną ramką okna do obliczenia sumy narastającej wynagrodzeń w każdym dziale. Suma narastająca jest liczona na podstawie wynagrodzenia pracownika uporządkowanego według jego employee_id.
```sql
SELECT employee_id, first_name, last_name, department, salary, 
       SUM(salary) OVER (PARTITION BY department ORDER BY employee_id
                         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM employees;
```

Wynik:

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
