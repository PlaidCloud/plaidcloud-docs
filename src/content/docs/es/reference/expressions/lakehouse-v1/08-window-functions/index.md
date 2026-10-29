---
title: Funciones de ventana (Lakehouse v1)
description: "Funciones de ventana SQL de Lakehouse v1: calculan sobre ventanas de filas (clasificación, totales acumulados, valores siguientes y anteriores)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/index.md
---

## Descripción general

Una función de ventana opera sobre un grupo (“ventana”) de filas relacionadas.

Para cada fila de entrada, una función de ventana devuelve una fila de salida que depende de la fila concreta que se pasa a la función y de los valores de las demás filas de la ventana.

Hay dos tipos principales de funciones de ventana sensibles al orden:

* `Rank-related functions`: las funciones relacionadas con la clasificación muestran información según la “posición” de una fila. Por ejemplo, si se clasifican las tiendas en orden descendente según la ganancia anual, la tienda con más ganancia ocupará la posición 1, la segunda tienda más rentable ocupará la posición 2, y así sucesivamente.

* `Window frame functions`: las funciones de marco de ventana permiten realizar operaciones móviles, como calcular un total acumulado o un promedio móvil, sobre un subconjunto de las filas de la ventana.

## Lista de funciones que admiten ventanas

La siguiente lista muestra todas las funciones de ventana.

| Nombre de la función                                                  | Categoría    | Ventana | Marco de ventana | Notas |
|-----------------------------------------------------------------------|--------------|--------|--------------|-------|
| [ARRAY_AGG](../07-aggregate-functions/aggregate-array-agg)            | General      | ✔      |              |       |
| [AVG](../07-aggregate-functions/aggregate-avg)                        | General      | ✔      | ✔            |       |
| [AVG_IF](../07-aggregate-functions/aggregate-avg-if)                  | General      | ✔      | ✔            |       |
| [COUNT](../07-aggregate-functions/aggregate-count)                    | General      | ✔      | ✔            |       |
| [COUNT_IF](../07-aggregate-functions/aggregate-count-if)              | General      | ✔      | ✔            |       |
| [COVAR_POP](../07-aggregate-functions/aggregate-covar-pop)            | General      | ✔      |              |       |
| [COVAR_SAMP](../07-aggregate-functions/aggregate-covar-samp)          | General      | ✔      |              |       |
| [MAX](../07-aggregate-functions/aggregate-max)                        | General      | ✔      | ✔            |       |
| [MAX_IF](../07-aggregate-functions/aggregate-max-if)                  | General      | ✔      | ✔            |       |
| [MIN](../07-aggregate-functions/aggregate-min)                        | General      | ✔      | ✔            |       |
| [MIN_IF](../07-aggregate-functions/aggregate-min-if)                  | General      | ✔      | ✔            |       |
| [STDDEV_POP](../07-aggregate-functions/aggregate-stddev-pop)          | General      | ✔      | ✔            |       |
| [STDDEV_SAMP](../07-aggregate-functions/aggregate-stddev-samp)        | General      | ✔      | ✔            |       |
| [MEDIAN](../07-aggregate-functions/aggregate-median)                  | General      | ✔      | ✔            |       |
| [QUANTILE_CONT](../07-aggregate-functions/aggregate-quantile-cont)    | General      | ✔      | ✔            |       |
| [QUANTILE_DISC](../07-aggregate-functions/aggregate-quantile-disc)    | General      | ✔      | ✔            |       |
| [KURTOSIS](../07-aggregate-functions/aggregate-kurtosis)              | General      | ✔      | ✔            |       |
| [SKEWNESS](../07-aggregate-functions/aggregate-skewness)              | General      | ✔      | ✔            |       |
| [SUM](../07-aggregate-functions/aggregate-sum)                        | General      | ✔      | ✔            |       |
| [SUM_IF](../07-aggregate-functions/aggregate-sum-if)                  | General      | ✔      | ✔            |       |
| [CUME_DIST](cume-dist)                                                | Rank-related | ✔      |              |       |
| [PERCENT_RANK](percent-rank/)                                         | Rank-related | ✔      | ✔            |       |
| [DENSE_RANK](dense-rank)                                              | Rank-related | ✔      | ✔            |       |
| [RANK](rank)                                                          | Rank-related | ✔      | ✔            |       |
| [ROW_NUMBER](row-number)                                              | Rank-related | ✔      |              |       |
| [NTILE](ntile)                                                        | Rank-related | ✔      |              |       |
| [FIRST_VALUE](first-value)                                            | Rank-related  | ✔     | ✔            |       |
| [FIRST](first)                                                        | Rank-related 	| ✔     | ✔            |       |
| [LAST_VALUE](last-value)                                              | Rank-related 	| ✔     | ✔            |       |
| [LAST](last)                                                          | Rank-related 	| ✔     | ✔            |       |
| [NTH_VALUE](nth-value)                                                | Rank-related 	| ✔     | ✔            |       |
| [LEAD](lead)                                                          | Rank-related 	| ✔     |              |       |
| [LAG](lag)                                                            | Rank-related 	| ✔     |              |       |

## Sintaxis de ventana

```sql
<function> ( [ <arguments> ] ) OVER ( { named window | inline window } )

named window ::=
    { window_name | ( window_name ) }

inline window ::=
    [ PARTITION BY <expression_list> ]
    [ ORDER BY <expression_list> ]
    [ window frame ]
```
La `named window` es una ventana que se define en la cláusula `WINDOW` de la instrucción `SELECT`, por ejemplo: `SELECT a, SUM(a) OVER w FROM t WINDOW w AS ( inline window )`.

La `<function>` es una de las siguientes ([función de agregado](../07-aggregate-functions), función de clasificación, función de valor).

La cláusula `OVER` especifica que la función se usa como función de ventana.

La subcláusula `PARTITION BY` permite agrupar las filas en subgrupos, por ejemplo por ciudad, por año, etc. La cláusula `PARTITION BY` es opcional. Puede analizar un grupo completo de filas sin dividirlo en subgrupos.

La cláusula `ORDER BY` ordena las filas dentro de la ventana.

La cláusula `window frame` especifica el tipo y la extensión del marco de ventana. La cláusula `window frame` es opcional. Si omite la cláusula `window frame`, el tipo de marco de ventana predeterminado es `RANGE` y la extensión predeterminada del marco de ventana es `UNBOUNDED PRECEDING AND CURRENT ROW`.


## Sintaxis del marco de ventana

`window frame` puede ser de uno de los siguientes tipos:

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


## Ejemplos de SQL

**Crear la tabla**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**Insertar datos**
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

**Ejemplo 1: clasificar a los empleados por salario**

En este ejemplo, usamos la función RANK() para clasificar a los empleados según su salario en orden descendente. El salario más alto obtiene la posición 1 y el salario más bajo obtiene el número de posición más alto.
```sql
SELECT employee_id, first_name, last_name, department, salary, RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```

Resultado:

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



**Ejemplo 2: calcular el salario total por departamento**

En este ejemplo, usamos la función SUM() con PARTITION BY para calcular el salario total pagado por departamento. Cada fila muestra el departamento y el salario total de ese departamento.
```sql
SELECT department, SUM(salary) OVER (PARTITION BY department) AS total_salary
FROM employees;
```

Resultado:

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


**Ejemplo 3: calcular un total acumulado de salarios por departamento**

En este ejemplo, usamos la función SUM() con un marco de ventana acumulativo para calcular un total acumulado de salarios dentro de cada departamento. El total acumulado se calcula a partir del salario del empleado, ordenado por su employee_id.
```sql
SELECT employee_id, first_name, last_name, department, salary, 
       SUM(salary) OVER (PARTITION BY department ORDER BY employee_id
                         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM employees;
```

Resultado:

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
